import os
import json

def clr_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n')


# on program start up, accessing cars.json db,
# returns cars list , creats cars.json if not exist
def load_cars(file_name):
    try:
        # Try to open the file for reading
        with open(file_name, 'r') as f:
            # Try to load JSON cars from the file
            cars = json.load(f)
            # print(f'File content: {cars}')
            return cars

    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f'The file {file_name} does not exist. Creating it...')
    
        # Create the file and write some initial cars (an empty list in this case)
        with open(file_name, 'w') as f:
            json.dump([], f)

        print(f'The file {file_name} has been created.')

        # open the file for reading
        with open(file_name, 'r') as f:
            # Try to load JSON cars from the file
            cars = json.load(f)
            print(f'File content: {cars}')
            return cars
    

# returns user selection
def dsp_menu(Selection):
    print('\ncars menu:\n')
    for item in Selection:
        print(f'{item.value} -> {item.name}')
    return Selection(input('\nselect from menu: '))


def print_cars(cars):
    clr_screen()
    if len(cars) == 0:
        print('car list is empty')
        return
    for id, car in enumerate(cars):
        print(id, car)


def search(cars):
    clr_screen()
    # Key and value to search for
    search_key = input('search key: ')
    search_value = input('search value: ')

    # Find dictionaries that contain the specified key-value pair
    cars = [d for d in cars if search_key in d and d[search_key] == search_value]

    clr_screen()
    for id, car in enumerate(cars):
        print(id, car)


# adds new entry to cars list
def add(cars, CARS_PATH):
    clr_screen()

    brand = input('brand: ')
    if brand == '6':  # Check for escape option
            clr_screen()
            return
    color = input('color: ')
    if color == '6':  # Check for escape option
            clr_screen()
            return
    model = input('model: ')
    if model == '6':  # Check for escape option
            clr_screen()
            return
    
    cars.append(
        {'brand': brand,
         'color': color,
         'model': model}
        )

    # cars.append(
    #     {'brand': input('brand: '),
    #      'color': input('color: '),
    #      'model': input('model: ')}
    #     )

    # Append the list to a JSON file
    with open(CARS_PATH, 'w') as f:
        json.dump(cars, f, indent=2)
        f.write('\n')  # Add a newline to separate appended content
    
    clr_screen()
        
    
def update(cars, CARS_PATH):
    clr_screen()
    for id, car in enumerate(cars):
        print(id, car)
    car = int(input('\nindex to update: '))
    if car == 6:  # Check for escape option
            clr_screen()
            return

    cars[car].update(
        {'brand': input('update brand: '),
         'color': input('update color: '),
         'model': input('update model: ')}
        )
    # Append the list to a JSON file
    with open(CARS_PATH, 'w') as f:
        json.dump(cars, f, indent=2)
        f.write('\n')  # Add a newline to separate appended content

    clr_screen()
    cars = load_cars(CARS_PATH)
    for id, car in enumerate(cars):
        print(id, car)


def delete(cars, CARS_PATH):
    clr_screen()
    for id, car in enumerate(cars):
        print(id, car)
    car = int(input('\nenter car id: '))
    if car == 6:  # Check for escape option
        clr_screen()
        return
    if 0 <= id < len(cars): del cars[car]
    # Append the list to a JSON file
    with open(CARS_PATH, 'w') as f:
        json.dump(cars, f, indent=2)
        f.write('\n')  # Add a newline to separate appended content

    clr_screen()
    cars = load_cars(CARS_PATH)
    for id, car in enumerate(cars):
        print(id, car)


def exit_prog():
    clr_screen()
    print('FIN')
    exit()