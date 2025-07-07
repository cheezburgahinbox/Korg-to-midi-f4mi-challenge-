import sys
import os
from mido import MidiFile, MidiTrack, Message, MetaMessage, bpm2tempo

def convert_sav_to_midi(sav_path):
    print(f"\n🔍 Reading: {sav_path}")

    # Try reading file
    try:
        with open(sav_path, 'rb') as f:
            data = f.read()
    except FileNotFoundError:
        print("❌ File not found.")
        return

    # For now, just print first 16 bytes as a placeholder
    print(f"📦 First 16 bytes: {data[:16].hex()}")

    # === MIDI STUB SECTION ===
    print("🎼 Generating placeholder MIDI...")

    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    # Meta: tempo 120bpm
    tempo = bpm2tempo(120)
    track.append(MetaMessage('set_tempo', tempo=tempo, time=0))

    # Simulated melody from DS-10 (just placeholder)
    notes = [60, 62, 64, 65, 67, 69, 71, 72]  # C major scale
    for note in notes:
        track.append(Message('note_on', note=note, velocity=64, time=480))
        track.append(Message('note_off', note=note, velocity=64, time=480))

    # Save MIDI file
    midi_path = os.path.splitext(sav_path)[0] + '_export.mid'
    mid.save(midi_path)
    print(f"✅ MIDI exported to: {midi_path}\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("⚠️ Drag a .sav file onto this script, or run:\n  python ds10_export.py file.sav")
    else:
        convert_sav_to_midi(sys.argv[1])
