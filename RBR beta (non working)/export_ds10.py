from mido import Message, MidiFile, MidiTrack

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Simple scale from C4 to C5
notes = [60, 62, 64, 65, 67, 69, 71, 72]

for note in notes:
    track.append(Message('note_on', note=note, velocity=64, time=480))
    track.append(Message('note_off', note=note, velocity=64, time=480))

mid.save('ds10_export.mid')
