import glob
from pathlib import Path
import functions
import keyboard


class AutoPiano:

    def __init__(self, sheet_path: str):
        self.SHEET_PATHS = sorted(glob.glob(f"{sheet_path}/*"))
        self.sheets_list = [Path(path).stem for path in self.SHEET_PATHS]
        self.title, self.sheet = self._pick_sheet()

    def _pick_sheet(self):
        """Displays a list of sheets and allow the user to pick one.

        :return: Sheet Title (str), Sheet Directory (str)
        """

        if not self.sheets_list:
            print("No sheets found in directory. Add a valid text file or check your spelling.")
            exit()

        # Display Sheets in Directory
        print("---------- SHEETS LIST ----------")
        for index, name in enumerate(self.sheets_list):
            print(f"{index + 1}. {name}")

        try:
            # Ask for index and get directory
            user_input = input("\nEnter a number or enter 'quit' to exit: ")

            if user_input.lower() == "quit":
                print("Exiting program..")
                exit()
            else:
                chosen_num = int(user_input) - 1

                sheet_dir = self.SHEET_PATHS[chosen_num]
                l_title = self.sheets_list[chosen_num]

                print(f"Chosen sheet: {l_title}")

                return l_title, sheet_dir

        except ValueError:
            print("Enter a valid number!")
            exit()
        except IndexError:
            print("Number not in list!")
            exit()

    def manual_play(self):
        """Listens for key presses and plays a note on key press."""
        note_list = functions.parse_sheet(self.sheet, manual=True)

        print("Press '[' or ']' to play a note\nPress 'ESC' to quit")
        if note_list:
            keyboard.on_press_key('[', lambda event: functions.on_key_press(note_list))
            keyboard.on_press_key(']', lambda event: functions.on_key_press(note_list))

            # Continue listening unless key is pressed
            keyboard.wait("esc")
        print("Sheet finished.")

    def auto_play(self):
        """Automatically plays a sheet on key press."""
        notes_list = functions.parse_sheet(self.sheet, manual=False)

        try:
            bpm = int(input("Enter song bpm: "))
        except ValueError:
            print("Enter a valid number!")
            exit()

        print("\nPress F9 to start playing\nPress F6 to stop playing")

        # Start
        keyboard.wait("F9")
        functions.auto_play(notes_list, bpm)
        print("Sheet finished.")
        exit()


if __name__ == "__main__":
    ap = AutoPiano("sheets")

    while True:
        inp = input("\nEnter 'auto' for auto-play. Enter 'manual' for manual play: ")
        inp.lower()

        if inp == "auto":
            ap.auto_play()
        elif inp == "manual":
            ap.manual_play()
        elif inp == "quit":
            print("Quit Program.")
            break
