
import functions
import glob
from pathlib import Path

# 1: show list of sheets to pick from and have user pick 1
# 2: parse the sheets so the program can tell singular notes from grouped notes
# 3: listen for given key presses and play a note on keypress
# 4: do step 3 until no more notes left


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
    sheet_dir = sheet_paths[sheet_num]
    sheet = functions.parse_sheet(sheet_dir)
    print(sheet)

except ValueError:
    print("Please enter a number.")
