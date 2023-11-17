import mido
from mido import MidiFile

# Function to convert MIDI note numbers to frequency in Hertz
def midi_note_to_freq(note_number):
    A4 = 440
    return (A4 / 32) * (2 ** ((note_number - 9) / 12))

def mid2beep(midpath, tempo, track_index):

    # Load the MIDI file
    mid = MidiFile(midpath)

    # Select the track
    track = mid.tracks[track_index]

    events_list = []
    current_time = 0  # In milliseconds

    found_first = False # Need to know the first note in case it starts later in the track
    sum_time = 0 # Keep a running sum to compare for rests

    # Iterate over the track's events
    for msg in track:
        # Update current time with delta time converted to milliseconds
        current_time += mido.tick2second(msg.time, mid.ticks_per_beat, tempo) * 1000

        if msg.type == 'set_tempo':
            # If there is a tempo change, update the current tempo
            tempo = msg.tempo
        
        elif msg.type == 'note_on' and msg.velocity > 0:
            # When a note-on message with non-zero velocity is encountered,
            # we capture the note and its start time
            freq = midi_note_to_freq(msg.note)
            # Get the timestamp of the note-on event
            start_time = current_time

            # Set the beginning of sum_time to first note
            if not found_first:
                sum_time = start_time
                found_first = True

            # Append rest time if necessary
            if start_time > sum_time:
                break_duration = start_time - sum_time
                events_list.append([0, break_duration])
                sum_time += break_duration

            # Append the frequency and placeholder for duration to the list
            events_list.append([freq, None])

        elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
            # Find the corresponding note-on event and calculate its duration
            # NOTE: This assumes that every note-on has a corresponding note-off
            for event in reversed(events_list):
                if event[0] == midi_note_to_freq(msg.note) and event[1] is None:
                    event[1] = current_time - start_time
                    sum_time += event[1] # RYAN add to current time
                    break

    # Filter out the events without a duration (in case there are any)
    # Also parse to integers
    final_list = [[int(f[0]), int(f[1])] for f in events_list if f[1] is not None]

    return final_list