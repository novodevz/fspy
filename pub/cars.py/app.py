from enum import Enum
import mod

class Selection(Enum):
    PRINT = '1'
    SEARCH = '2'
    ADD = '3'
    UPDATE = '4'
    DELET = '5'
    EXIT = '6'


CARS_PATH = 'cars.json'

def main():
    mod.clr_screen()

    while True:
        cars = mod.load_cars(CARS_PATH)
        selection = mod.dsp_menu(Selection)

        if selection == Selection.PRINT: mod.print_cars(cars)
        if selection == Selection.SEARCH: mod.search()
        if selection == Selection.ADD: mod.add(cars, CARS_PATH)
        if selection == Selection.UPDATE: mod.update()
        if selection == Selection.DELET: mod.delete(cars, CARS_PATH)
        if selection == Selection.EXIT: mod.exit_prog()


if __name__ == "__main__":
    main()