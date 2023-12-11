from enum import Enum
import mod

class Selection(Enum):
    PRINT = '1'
    SEARCH = '2'
    ADD = '3'
    UPDATE = '4'
    DELET = '5'
    ESCAPE = '6'
    EXIT = '7'


CARS_PATH = 'cars.json'

def main():
    mod.clr_screen()

    while True:
        cars = mod.load_cars(CARS_PATH)
        selection = mod.dsp_menu(Selection)

        if selection == Selection.PRINT: mod.print_cars(cars)
        elif selection == Selection.SEARCH: mod.search(cars)
        elif selection == Selection.ADD: mod.add(cars, CARS_PATH)
        elif selection == Selection.UPDATE: mod.update(cars, CARS_PATH)
        elif selection == Selection.DELET: mod.delete(cars, CARS_PATH)
        elif selection == Selection.ESCAPE: return
        elif selection == Selection.EXIT: mod.exit_prog()


if __name__ == "__main__":
    main()