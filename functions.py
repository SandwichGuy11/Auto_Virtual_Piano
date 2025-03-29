
import keyboard

PLAY_NOTE_1 = ","
PLAY_NOTE_2 = "."


def parse_sheet(sheet_dir: str):
    """Returns a list of individual notes/note groups for iteration."""
    # TODO: remove brackets []
    try:
        with open(file=sheet_dir, mode="r") as file:
            contents = file.read()
            translate_tbl = str.maketrans({"|": " ",
                                           "\n": " ",
                                           })
            contents = [grp.translate(translate_tbl) for grp in contents]
            contents = ''.join(contents)
            contents = contents.split()

            notes = []
            for note in contents:
                # Separate notes if not encased in brackets
                if len(note) > 1 and not note.startswith("["):
                    notes.extend(note)
                elif len(note) > 1 and note.startswith("["):
                    notes.append(note.strip("[]"))
                else:
                    notes.append(note)

            return notes

    except PermissionError as e:
        print(f"{e}: Please input a txt file")
    except FileNotFoundError as e:
        print(f"{e}: The specified file was not found.")


def is_note_group(note: str):
    return len(note) > 1


def is_shifted(char: str):
    """Checks if a character requires the Shift key to be pressed to be typed with a keyboard.

    It checks if the given character is an uppercase letter or a special
    character that is accessed by holding down the Shift key.

    :param char: A single character (length of 1).
    :return: bool: True if the character requires the Shift key, False otherwise.
    """
    if char.isupper():
        return True
    if char in "!@#$%^&*()_+{}|:\"<>?":
        return True
    return False


def play_note(note: str):
    conversion_cases = {'!': '1',
                        '@': '2',
                        '£': '3',
                        '$': '4',
                        '%': '5',
                        '^': '6',
                        '&': '7',
                        '*': '8',
                        '(': '9',
                        ')': '0'}
    note = note
    if is_shifted(note):
        if note in conversion_cases:
            note = f"shift+{conversion_cases[note]}"  # convert to symbol to number
        note = f"shift+{note.lower()}"

    keyboard.press(note)
    keyboard.release(note)


def on_key_press(sheet: list):
    sheet = sheet
    note = sheet[0]
    if is_note_group(note):
        for nt in note:
            play_note(nt)
    else:
        play_note(note)
    sheet.pop(0)


def print_note(sheet):
    """Debug"""
    sheet = sheet
    note = sheet[0]
    print(note)
    sheet.pop(0)


if __name__ == "__main__":
    print(parse_sheet("sheets/DS3 - Sister Friede And Father Ariandel.txt"))
