import FliesClass as FC

name = input("Enter flies' name: ")
fly_name = FC.Flies(name)

housefly = fly_name.flight_length()
mosquito = fly_name.flight_length()
print(f"{fly_name.get_name()} can fly: ", fly_name.get_miles(), " miles")
print(f"{housefly.get_name()} can fly: ", mosquito.get_miles(), " miles")











