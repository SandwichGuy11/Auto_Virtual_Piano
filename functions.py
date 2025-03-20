
def parse_sheet(sheet_dir: str):
    """Returns a list of individual notes/note groups for iteration.

    Returns:
        list: A list of individual notes or note groups.
    """
    try:
        with open(file=sheet_dir, mode="r") as file:
            contents = file.read()
            translate_tbl = str.maketrans({"|": " ",
                                           "\n": " "}
                                          )
            contents = [grp.translate(translate_tbl) for grp in contents]
            contents = ''.join(contents)
            contents = contents.split()

            notes = []
            for note in contents:
                if len(note) > 1 and not note.startswith("["):
                    notes.extend(note)
                else:
                    notes.append(note)

            return notes

    except PermissionError as e:
        print(f"{e}: Please input a txt file")
    except FileNotFoundError as e:
        print(f"{e}: The specified file was not found.")


def is_note_group(note: str):
     # TODO: check if the str is encased in [].


def is_shifted(char: str):
    """Checks if a character requires the Shift key to be pressed to be typed with a keyboard.

    It checks if the given character is an uppercase letter or a special
    character that is accessed by holding down the Shift key.

    :param char: A single character (length of 1).
    :return: bool: True if the character requires the Shift key, False otherwise.
    """
    ascii_value = ord(char)  # get integer that represents char i.e (a = 97)
    if 65 <= ascii_value <= 90:  # 65-90 represents uppercase letters
        return True
    if char in "!@#$%^&*()_+{}|:\"<>?":
        return True
    return False


def play_note(note: str):
    # TODO: play the note if single char, else if note is encased in [], iterate through and play all notes.
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

    if is_shifted(note):
        if note in conversion_cases:
            note = conversion_cases[note]  # convert to symbol to number



if __name__ == "__main__":
    import time

    print(parse_sheet("sheets/DS3 - Sister Friede And Father Ariandel.txt"))
    for i in parse_sheet("sheets/DS3 - Sister Friede And Father Ariandel.txt"):
        print(i)
        # time.sleep(0.7)
