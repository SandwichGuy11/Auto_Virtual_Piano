import glob
from pathlib import Path
import functions
import keyboard


class AutoPiano:

    def __init__(self, sheet_path: str):
        # Sheet File Paths
        self.SHEET_PATHS = sorted(glob.glob(f"{sheet_path}/*"))
        self.sheets_list = [Path(path).stem for path in self.SHEET_PATHS]
        self.title, self.sheet = self.pick_sheet()

    def pick_sheet(self):
        """Display sheets and allows the user to pick one.

        Returns:
             list: A list of notes/ note groups
         """

        # Display Sheets in Directory
        print("---------- SHEETS LIST ----------")
        for index, title in enumerate(self.sheets_list):
            print(f"{index + 1}. {title}")

        try:
            # Ask for index and get directory
            chosen_num = int(input("\nEnter a number: ")) - 1
            sheet_dir = self.SHEET_PATHS[chosen_num]
            local_title = self.sheets_list[chosen_num]
            local_sheet = functions.parse_sheet(sheet_dir)

            print(f"Chosen sheet: {local_title}")
            print(f"Notes: {len(local_sheet)}")

            return local_title, local_sheet

        except ValueError:
            print("Error: enter a valid number!")
        except IndexError:
            print("Error: enter a valid range!")

    def listen_for_keys(self):
        if self.sheet:
            keyboard.on_press_key(',', lambda event: functions.on_key_press(self.sheet))
            keyboard.on_press_key('.', lambda event: functions.on_key_press(self.sheet))
            keyboard.wait("esc")
        print("No notes left. exiting.")


if __name__ == "__main__":
    ap = AutoPiano("sheets")
    ap.listen_for_keys()
