import EC_Joe_Classes as c


name = input("Customer Name:")
address = input("Address:")
phone = input("Phone Number:")
customer = c.Customer(name,address,phone)


make = input("Car Make:")
model = input("Model:")
year = input("Year:")
car = c.Car(make,model,year)


part_cost = float(input("Parts Cost:"))
labor_cost = float(input("Labor Cost:"))
costs = c.ServiceQuote(part_cost,labor_cost)


print("Customer:",customer.get_name(), "    ","Address:",customer.get_address(),
     "    ","Phone:",customer.get_phone())
print("Car Make:",car.get_make(),"    ","Car Model:",car.get_model(),"    ","Car Year:",car.get_year())
print("Service Quote")
print("Parts: $",costs.get_parts_charges())
print("Labor: $",costs.get_labor_charges())
print("Sales Tax: $",costs.get_sales_tax())
print("Total Charges: $",costs.get_total_charges())

