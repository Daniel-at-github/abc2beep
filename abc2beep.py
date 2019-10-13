#!/usr/bin/env python3
# coding: utf-8

import itertools
import pathlib

import click

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

def import_music21():
    """Disable music21 optional packages import warnings, only when
       the user haven't created ~/.music21rc. Then, create a temporal one
    """
    global music21
    music21rc_path = pathlib.Path('~/.music21rc').expanduser()
    exist_config = music21rc_path.exists()
    if not exist_config:
        with music21rc_path.open('w') as f:
            f.write('<settings encoding="utf-8">')
            f.write('<preference name="warnings" value="0" />')
            f.write('</settings>')
    import music21
    if not exist_config:
        music21rc_path.unlink()

@click.command()
@click.argument('path', metavar='[ABC_FILE]', type=click.Path(exists=True))
@click.argument('tempo', default='350', type=click.INT)
def main(path, tempo):
    import_music21()
    abcScore = music21.converter.parse(path)

    notes_list = [
        (note.pitch.frequency, note.duration.quarterLength, note.offset)
        for note in abcScore.flat
        if isinstance(note, music21.note.Note)
    ]
    beep_notes = [
        "  --new -f {: >8.2f} -l {: >8.2f} -D {: >8.2f}".format(
            float(note[0]),
            float(note[1] * tempo),
            float(max(0,((next_note[2] - note[1]) - note[2]) * tempo)))
        for note, next_note in pairwise(notes_list + [notes_list[-1]])
    ]
    beep_command = "beep \\\n" + " \\\n".join(beep_notes)
    print(beep_command)


if __name__ == '__main__':
    main()
