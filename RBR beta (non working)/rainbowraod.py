import sys
import os

def hexdump(data, start=0, length=512):
    print("\n🔍 First 512 Bytes (Hexdump):")
    for i in range(start, min(start+length, len(data)), 16):
        chunk = data[i:i+16]
        hex_line = ' '.join(f"{b:02X}" for b in chunk)
        ascii_line = ''.join(chr(b) if 32 <= b < 127 else '.' for b in chunk)
        print(f"{i:08X}: {hex_line:<48} {ascii_line}")

def detect_repeated_blocks(data, block_size=256, min_blocks=3):
    print("\n📊 Repeating Block Detection:")
    seen = {}
    for i in range(0, len(data) - block_size, block_size):
        chunk = data[i:i+block_size]
        key = chunk[:16]  # Use first 16 bytes as fingerprint
        if key in seen:
            seen[key].append(i)
        else:
            seen[key] = [i]

    for k, offsets in seen.items():
        if len(offsets) >= min_blocks:
            print(f"🔁 Repeating block (fingerprint {k.hex()}): {len(offsets)} times at offsets {offsets[:3]}...")

def extract_tempo_guess(data):
    print("\n⏱️ Tempo Guess (Searching for common BPM patterns like 0x78, 0x80):")
    tempo_bytes = [0x78, 0x80, 0x90]
    for i in range(len(data) - 1):
        if data[i] in tempo_bytes:
            print(f"Possible tempo byte: {data[i]:02X} at offset {i}")

def parse_ds10_stub(sav_path):
    print(f"\n📂 Opening DS-10 Save File: {sav_path}")
    try:
        with open(sav_path, 'rb') as f:
            data = f.read()
    except FileNotFoundError:
        print("❌ File not found.")
        return

    print(f"🧱 File Size: {len(data)} bytes")
    hexdump(data)
    detect_repeated_blocks(data)
    extract_tempo_guess(data)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("⚠️ Drag a .sav file onto this script, or run:\n  python ds10_parser_stub.py file.sav")
    else:
        parse_ds10_stub(sys.argv[1])
