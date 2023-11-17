import winsound
import time

duration = {
    "whole": 1600,
    "half": 800,
    "quarter": 400,
    "eighth": 200,
    "sixteenth": 100
}

tone = {
    "G3": 196,
    "A3": 220,
    "Asharp3": 233,
    "B3": 247,
    "C4": 262,
    "Csharp4": 277,
    "Dsharp4": 311,
    "E4": 330,
    "F4": 349,
    "Fsharp4": 370,
    "G4": 392,
    "Gsharp4": 415,
    "A4": 440,
    "Asharp4": 466,
    "B4": 494,
    "C5": 523
}



def play(song):
    for note in song:
        if ((note[0] == 'rest') or (note[0] == 0)):
            time.sleep(note[1]/1000)
        else:
            winsound.Beep(note[0], note[1])