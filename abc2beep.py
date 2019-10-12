#!/usr/bin/env python3
# coding: utf-8

import itertools
import click
import music21

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

@click.command()
@click.argument('path', metavar='[ABC_FILE]', type=click.Path(exists=True))
@click.argument('tempo', default='350', type=click.INT)
def main(path, tempo):
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
