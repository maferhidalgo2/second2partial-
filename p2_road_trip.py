https://replit.com/join/ccnufrevpz-maria-fernan901
#link

#Ask the user to input the distance in miles and the car's miles per gallon (MPG). Then, inquire about the current price of gasoline per gallon and how many days they plan to travel. Calculate the total cost of the trip, considering changing gasoline prices during the journey.
#Enter the distance in miles: 500
#Enter the car's miles per gallon (MPG): 25
#Enter the current price of gasoline per gallon: 3.50 Enter the number of days you plan to travel: 7
#Total cost of the trip: $700.00#

distance_miles=int(input("Enter the distance on miles"))
price_gasoline=int(input("Enter the current price of gasoline"))
days_travel=int(input("Enter the number of days you plan to travel"))
mpg=int(input("Enter the car's miles per gallon (MPG)"))
cost_gasoline=(distance_miles/mpg)*price_gasoline
total_cost=cost_gasoline*days_travel
print("Total cost of the trip: $",total_cost)
