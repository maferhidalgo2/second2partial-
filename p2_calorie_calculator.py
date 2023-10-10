#LINK
https://replit.com/join/knqzdarobo-maria-fernan901
def calculate_final_price(price, category, quantity):
    category_discount = 0
    
    if category == 'A':
        category_discount = 0.10
    elif category == 'B':
        category_discount = 0.05
    elif category == 'C':
        category_discount = 0.02
    
    additional_discount = 0
    if quantity > 10:
        additional_discount = 0.05

    total_discount = category_discount + additional_discount
    discounted_price = price * (1 - total_discount)
 return discounted_price
  
while True:
    try:

  price=float(input("Enter the price of the item"))
  category=input("Enter the category of the item ,Please enter A,B,C.").strip().upper.()
  quantity=int(input("Enter the quantity of the item"))
  
  final_price=calculate_final_price(price, category, quantity)
  print(f"The final price of the item is: ${final_price:.2f}")

if __name__ == "__main__":
    main()
