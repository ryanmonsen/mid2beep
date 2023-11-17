# mid2beep

This small Python script allows you to play sounds through your PC speaker. It uses winsound and mido.

If you are running Windows 10 64 bit, you need to install BeepXP: https://www.waldbauer.com/tmp/dl.php?download=beepxp64

## Examples:

**Fanfare.py** utilizes note and duration conversions found in Beep.py for simple melodies.

**MI.py** directly provides note frequency and duration (in milliseconds).

**AlloRondo.py** uses mid2beep to convert allo_rondo.mid to note frequency and duration, and then plays it.

## Regarding midi files:

PC Speakers are monophonic. This means you cannot play multiple notes at once. You must use arpeggios to approximate multiple notes. Due to this, I found it was easier to just compose from scratch while referencing sheet music than to attempt to modify a pre-existing polyphonic midi file.

See AlloRondo.py in action below, via YouTube:

[![Rondo Alla Turca](https://img.youtube.com/vi/zTppzzSkp-c/0.jpg)](https://www.youtube.com/watch?v=zTppzzSkp-c)
