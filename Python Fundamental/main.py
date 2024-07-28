car = [
    {"make": "Ford","model": "v1","mileage": 23000,"fuel_consumed": 460},
    {"make": "Mazda","model": "v2","mileage": 23000,"fuel_consumed": 460},
    {"make": "Mini","model": "v3","mileage": 23000,"fuel_consumed": 460},
    {"make": "Roals Roils","model": "v4","mileage": 23000,"fuel_consumed": 460}
]


def calculateMpg(car_to_calculate):
    mpg = car_to_calculate["mileage"] / car_to_calculate["fuel_consumed"]
    name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f"{name} does {mpg} miles per Gallon")

calculateMpg(car[1])
