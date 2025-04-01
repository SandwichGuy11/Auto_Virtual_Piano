import glob
from pathlib import Path
import functions
import keyboard


class AutoPiano:

    def __init__(self, sheet_path: str):
        # Sheet File Paths
        self.SHEET_PATHS = sorted(glob.glob(f"{sheet_path}/*"))
        self.sheets_list = [Path(path).stem for path in self.SHEET_PATHS]
        self.title, self.sheet = self._pick_sheet()
        self.sheet = functions.manual_parse(self.sheet)

    def _pick_sheet(self):
        """Display sheets and allows the user to pick one.

        Returns:
             str: Title of the sheet.
             str: Directory of the sheet.
         """

        # Display Sheets in Directory
        print("---------- SHEETS LIST ----------")
        for index, name in enumerate(self.sheets_list):
            print(f"{index + 1}. {name}")

        try:
            # Ask for index and get directory
            chosen_num = int(input("\nEnter a number: ")) - 1
            sheet_dir = self.SHEET_PATHS[chosen_num]
            l_title = self.sheets_list[chosen_num]

            print(f"Chosen sheet: {l_title}")

            return l_title, sheet_dir

        except ValueError:
            print("Error: enter a valid number!")
        except IndexError:
            print("Error: enter a valid range!")

    def manual_play(self):
        """Listens for key presses and plays a note on key press."""
        note_list = self.sheet

        print("Press '[' or ']' to play a note\nPress 'ESC' to quit")
        if note_list:
            keyboard.on_press_key('[', lambda event: functions.on_key_press(note_list))
            keyboard.on_press_key(']', lambda event: functions.on_key_press(note_list))

            # Continue listening unless key is pressed
            keyboard.wait("esc")
        print("Exiting..")

    def auto_play(self):
        pass


if __name__ == "__main__":
    ap = AutoPiano("sheets")
    ap.manual_play()
