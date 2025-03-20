
import functions
import glob
import keyboard
from pathlib import Path

# 1: show list of sheets to pick from and have user pick 1
# 2: parse the sheets so the program can tell singular notes from grouped notes
# 3: listen for given key presses and play a note on keypress
# 4: do step 3 until no more notes left
# 5: add a key to quit the program when pressed at any point during loop


PLAY_NOTE_1 = ","
PLAY_NOTE_2 = "."

SHEET_PATHS = glob.glob("sheets/*")
sheets_list = [Path(path).stem for path in SHEET_PATHS]
sheet = None

# sheet_dir = Path("sheets").resolve()
# print(f"Sheets Directory: {sheet_dir}")

is_choosing = True
while is_choosing:
    try:
        # Display available sheets
        print("---------- SHEETS LIST ----------")
        for index, title in enumerate(sheets_list):
            print(f"{index + 1}. {title}")

        user_input = input("\nEnter a number or type 'exit' to quit: ")
        if user_input.upper() == "EXIT":
            print("Quitting program..")
            is_choosing = False
        else:
            sheet_num = int(user_input) - 1
            sheet_dir = SHEET_PATHS[sheet_num]
            sheet_name = sheets_list[sheet_num]
            sheet = functions.parse_sheet(sheet_dir)
            print(f"Selected: {sheet_name}")
            is_choosing = False

    except ValueError:
        print("Enter a valid number.")


if sheet:
    while len(sheet) > 0:
        # this is just a placeholder for the event
        inp = input("Enter g: ")
        if inp == "g":
            print(sheet[0])
            sheet.pop(0)

    print("No more notes left.")
