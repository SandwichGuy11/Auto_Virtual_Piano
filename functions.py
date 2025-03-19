
def parse_sheet(sheet_dir: str):
    """Returns a list of individual notes/note groups for iteration."""
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


if __name__ == "__main__":
    import time

    print(parse_sheet("sheets/Stromae - Alors On Danse.txt"))
    for i in parse_sheet("sheets/Stromae - Alors On Danse.txt"):
        print(i)
        # time.sleep(0.7)
