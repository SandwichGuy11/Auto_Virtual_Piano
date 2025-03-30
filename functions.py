
import keyboard

PLAY_NOTE_1 = ","
PLAY_NOTE_2 = "."


def autoplay_parse(sheet_dir: str):
    """Returns a list of individual notes/note groups for automatic iteration.
        :param sheet_dir: Directory of the txt file to parse.
        """
    try:
        with open(file=sheet_dir, mode="r") as file:
            translate_tbl = str.maketrans({"|": "",
                                           "\n": "",
                                           " ": "",
                                           })

            contents = file.read()  # file contents as str
            contents = [grp.translate(translate_tbl) for grp in contents]
            contents = ''.join(contents)  # str

            notes_list = []
            current_chord = ""
            in_chord = False

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


def manual_parse(sheet_dir: str):
    """Returns a list of individual notes/note groups for manual iteration.
    :param sheet_dir: Directory of the txt file to parse.
    """
    try:
        with open(file=sheet_dir, mode="r") as file:
            translate_tbl = str.maketrans({"|": "",
                                           "\n": "",
                                           " ": "",
                                           })

            contents = file.read()  # file contents as str
            contents = [grp.translate(translate_tbl) for grp in contents]
            contents = ''.join(contents)  # str

            notes_list = []
            current_chord = ""
            in_chord = False

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
    print(note)
    if is_note_group(note):
        for nt in note:
            play_note(nt)
    else:
        play_note(note)
    sheet.pop(0)


if __name__ == "__main__":
    print(manual_parse("sheets/AOT - YouSeeBIGGIRLTT.txt"))
