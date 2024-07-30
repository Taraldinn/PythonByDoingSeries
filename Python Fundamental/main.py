cars = [
    {"make": "Ford", "model": "v1", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Mazda", "model": "v2", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Mini", "model": "v3", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Roals Roils", "model": "v4", "mileage": 23000, "fuel_consumed": 460}
]


def calculate_mpg(car):
    mpg = car["mileage"] / car["fuel_consumed"]
    return mpg


def car_name(car):
    name = f"{car['make']} {car['model']}"
    return name


def print_car_info(car):
    name = car_name(car)
    mpg = calculate_mpg(car)
    print(f"{name} does {mpg} miles per Gallon")
    return None

for car in cars:
    mpg = print_car_info(car)

