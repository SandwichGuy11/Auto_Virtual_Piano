import keyboard
import time

CONVERSION_CASES = {'!': '1',
                    '@': '2',
                    '£': '3',
                    '$': '4',
                    '%': '5',
                    '^': '6',
                    '&': '7',
                    '*': '8',
                    '(': '9',
                    ')': '0'}

TRANSLATE_TABLE = str.maketrans({"|": "",
                                 "\n": "",
                                 " ": "",
                                 })


def parse_sheet(sheet_dir: str, manual: bool):
    """Returns a list of individual notes/note groups for iteration.
        :param sheet_dir: Directory of the txt file to parse.
        :param manual: Use a different parsing method for manual playing.
        """
    try:
        with open(file=sheet_dir, mode="r") as file:
            contents = file.read()  # file contents as str

        if manual:
            contents = [grp.translate(TRANSLATE_TABLE) for grp in contents]
            contents = ''.join(contents)

        notes_list = []

        current_chord = ""
        in_chord = False

        # Remove brackets in chords
        for char in contents:
            if char == "[":
                in_chord = True
            elif char == "]":
                in_chord = False
                notes_list.append(current_chord)  # add chord to sheet
                current_chord = ""  # clear chord variable
            elif in_chord:
                current_chord += char
            else:
                notes_list.append(char)

        return notes_list

    # Catch wrong file types
    except PermissionError as e:
        print("Please input a txt file")
    # Catch invalid file
    except FileNotFoundError as e:
        print("The specified file was not found.")


def is_note_group(note: str):
    """Check if a note is more than 1 char"""
    return len(note) > 1


def is_shifted(char: str):
    """Checks if a character requires the Shift key to be pressed to be typed with a keyboard.
    :param char: A single character (length of 1).
    :return: bool: True if the character requires the Shift key, False otherwise.
    """
    if char.isupper():
        return True
    if char in "!@#$%^&*()_+{}|:\"<>?":
        return True
    return False


def play_note(note: str):
    """Plays the given note as a keystroke.
    :param note: The note to be played.
    """

    note = note
    if is_shifted(note):
        if note in CONVERSION_CASES:
            note = f"shift+{CONVERSION_CASES[note]}"  # convert to symbol to number
        note = f"shift+{note.lower()}"

    keyboard.press(note)
    keyboard.release(note)


def on_key_press(sheet: list):
    """Takes a list of notes and invokes play_note to play a note.
    :param sheet: A list of notes.
    """
    sheet = sheet
    note = sheet[0]
    print(note)
    if is_note_group(note):
        for nt in note:
            play_note(nt)
    else:
        play_note(note)
    sheet.pop(0)


def auto_play(sheet: list, bpm: int):
    """Takes a sheet and bpm value and iterates through the sheet relative to the BPM.

    :param sheet: A list of notes.
    :param bpm: The BPM of the song.
    """
    interval = (60 / bpm) * 0.23
    space_interval = (60 / bpm) * 0.03
    rest_interval = (60 / bpm) * 0.23

    for note in sheet:
        print(note)

        if keyboard.is_pressed("F6"):
            break

        if note == " ":
            time.sleep(space_interval)
        elif note == "|":
            time.sleep(rest_interval)
        elif is_note_group(note):
            for nt in note:
                play_note(nt)
        else:
            play_note(note)
        time.sleep(interval)


if __name__ == "__main__":
    print(parse_sheet("sheets/AOT - YouSeeBIGGIRLTT.txt", manual=False))
