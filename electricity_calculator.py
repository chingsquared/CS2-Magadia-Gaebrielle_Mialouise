# Electricity Bill Calculator

RATE = 12.90

#Validate customer's name
while True:
    name = input("Enter customer name: ")
    if name.strip() != "":
     break
    else:
        print("Invalid name. Name cannot be empty.")
#Validate previous reading
while True:
    previous = float(input("Enter previous meter reading: "))

    if previous >=0:
     break
    else:
     print ("Invalid reading. PLease try a number that is at least 0.")

#Validate current reading
while True:
    current = float(input("Enter current meter reading: "))
    if current >= previous:
     break
    else:
        print ("Invalid reading. PLease try a number that is at least your previous reading.")

consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))
