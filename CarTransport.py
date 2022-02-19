cars = input("Input number of cars \n")
cars = int(cars)

space_in_car = input("Input Space in Car \n")
space_in_car = float(space_in_car)

drivers = input("Input number of drivers \n")
drivers = int(drivers)

passengers = input("Input number of passengers \n")
passengers = int(passengers)

cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car")


cars = int(input("Input number of cars \n"))

space_in_car = float(input("Input Space in Car \n"))

drivers = int(input("Input number of drivers \n"))

passengers = int(input("Input number of passengers \n"))

cars_not_driven = cars - drivers
cars_driven = drivers
carrying_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven

# updated

print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carrying_capacity, "at once")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car")

if average_passengers_per_car > 5:
    print('There has to be another trip for the remaining passengers')
