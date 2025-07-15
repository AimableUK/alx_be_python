weatherCondition = input("What's the weather like today? (sunny/rainy/cold): ")

if weatherCondition == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weatherCondition == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weatherCondition == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")