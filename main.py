"""The GPS Swears It Was a Shortcut — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The excuse: the road looked shorter on the map, and the goat seemed confident.
TEXT = "Recalculating. In my defence, that road looked shorter on the map, and the goat crossing it seemed very confident."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
