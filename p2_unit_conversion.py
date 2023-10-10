https://replit.com/join/fcvlfyllmt-maria-fernan901
#LINK
def miles_to_kilometers(miles):
    return miles * 1.60934

def liters_to_gallons(liters):
    return liters * 0.264172

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def operation():
 print("Welcome to the unit calculator")
   
while True:
        try:
            quantity = float(input("Enter the quantity to convert: "))
            unit_origin = input("Enter the unit to convert")
            unit_destination = input("Enter the unit of destination")
            
            if unit_origin == unit_destination:
                print("The units are the same. No conversion needed.")
            elif unit_origin == "miles" and unit_destination== "kilometers":
                result = miles_to_kilometers(quantity)
                print(f",{quantity} miles is equal to {result} kilometers.")
            elif unit_origin == "liters" and unit_destination == "gallons":
                result = liters_to_gallons(quantity)
                print(f"{quantity} liters is equal to {result} gallons.")
            elif unit_origin == "fahrenheit" and unit_destination == "celsius":
                result = fahrenheit_to_celsius(quantity)
                print(f"{quantity} Fahrenheit is equal to {result} celsius.")
            
            else:
            print("Write something valid)
