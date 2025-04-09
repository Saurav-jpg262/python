products = [
{"name": "iphone", "price": 1400},
{"name": "samsung", "price": 900},
{"name": "nokia", "price": 700},
]

careers = [
    {"company_name": "pathao", "fees": 25},
    {"company_name": "indrive", "fees": 20},
    {"company_name": "foodmandu", "fees": 15},
]

for index, career in enumerate(careers):
    print(f"For {career["name"]} press {index}")
while True:
    user_career_index = input("Please enter the product number:\n")
    try:
        user_career_index = int(user_career_index)
    
        if user_career_index >=0 and user_career_index < len(careers):
            break
        else:
            print("This product does not exit")
    
    except ValueError:
        print("Please only enter number")

user_career = careers[user_career_index]