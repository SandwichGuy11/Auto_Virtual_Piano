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


def parse_sheet(sheet_dir: str, manual: bool):
    """Returns a list of individual notes/note groups for automatic iteration.
        :param sheet_dir: Directory of the txt file to parse.
        :param manual: Use a different parsing method for manual playing.
        """
    try:
        with open(file=sheet_dir, mode="r") as file:
            contents = file.read()  # file contents as str

        if manual:
            translate_tbl = str.maketrans({"|": "",
                                           "\n": "",
                                           " ": "",
                                           })
            contents = [grp.translate(translate_tbl) for grp in contents]
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
        print(f"{e}: Please input a txt file")
    # Catch invalid file
    except FileNotFoundError as e:
        print(f"{e}: The specified file was not found.")


def is_note_group(note: str):
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
    note = note
    if is_shifted(note):
        if note in CONVERSION_CASES:
            note = f"shift+{CONVERSION_CASES[note]}"  # convert to symbol to number
        note = f"shift+{note.lower()}"

    keyboard.press(note)
    keyboard.release(note)


def on_key_press(sheet: list):
    sheet = sheet
    note = sheet[0]
    print(note)
    if is_note_group(note):
        for nt in note:
            play_note(nt)
    else:
        play_note(note)
    sheet.pop(0)


def auto_play(sheet, bpm):
    interval = (60 / bpm) * 0.23
    space_interval = (60 / bpm) * 0.03
    rest_interval = (60 / bpm) * 0.25

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
