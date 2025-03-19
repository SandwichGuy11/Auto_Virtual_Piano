
import functions
import glob
from pathlib import Path

# TODO 1: show list of sheets to pick from and have user pick 1
# TODO 2: parse the sheets so the program can tell singular notes from grouped notes
# TODO 3: listen for given key presses and play a note on keypress
# TODO 4: do step 3 until no more notes left


sheet_paths = glob.glob("sheets/*")
sheets_list = [Path(filepath).stem for filepath in sheet_paths]

# sheet_dir = Path("sheets").resolve()
# print(f"Sheets Directory: {sheet_dir}")
print("---------- SHEETS LIST ----------")
for index, title in enumerate(sheets_list):
    print(f"{index + 1}. {title}")

try:
    sheet_num = int(input("\nPick a sheet. Enter a number: "))
    sheet_num -= 1
    print(sheet_paths[sheet_num])
except ValueError:
    print("Please enter a number.")
