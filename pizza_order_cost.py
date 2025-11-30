# pizza_order_cost.py
# Program to calculate total pizza order cost

def main():
    # Display welcome message
    print("=== Pizza Order Cost Calculator ===\n")
    
    # Step 1: Get user inputs
    # Pizza size input with validation
    while True:
        pizza_size = input("Enter pizza size (small or large): ").lower().strip()
        if pizza_size in ['small', 'large']:
            break
        else:
            print("Invalid size! Please enter 'small' or 'large'.")
    
    # Number of toppings input with validation
    while True:
        try:
            num_toppings = int(input("Enter number of toppings: "))
            if num_toppings >= 0:
                break
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input! Please enter a whole number.")
    
    # Delivery distance input with validation
    while True:
        try:
            delivery_distance = float(input("Enter delivery distance in miles: "))
            if delivery_distance >= 0:
                break
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    # Step 2: Calculate base cost using if-elif (scalable)
    if pizza_size == "small":
        base_cost = 8.00
    elif pizza_size == "large":
        base_cost = 12.00
    else:
        base_cost = 0  # Fallback, should not happen due to validation
    
    # Step 3: Calculate cost of toppings
    # Each topping costs $1
    topping_cost = num_toppings * 1.00
    
    # Step 4: Calculate delivery fee
    # $2 for first 5 miles, $1 for each additional mile
    if delivery_distance == 0:
        delivery_fee = 0.00  # Pickup order
    elif delivery_distance <= 5:
        delivery_fee = 2.00
    else:
        delivery_fee = 2.00 + (delivery_distance - 5) * 1.00
    
    # Step 5: Calculate total cost
    subtotal = base_cost + topping_cost
    total_cost = subtotal + delivery_fee
    
    # Step 6: Display the result using f-string
    print("\n" + "="*40)
    print("ORDER SUMMARY")
    print("="*40)
    print(f"Pizza Size: {pizza_size.title()} - ${base_cost:.2f}")
    print(f"Toppings ({num_toppings}) - ${topping_cost:.2f}")
    print(f"Delivery Fee ({delivery_distance:.1f} miles) - ${delivery_fee:.2f}")
    print("-"*40)
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Total Cost: ${total_cost:.2f}")
    print("="*40)

# Run the program
if __name__ == "__main__":
    main()
