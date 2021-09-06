my_name = 'JAMAL IBRAHIM UMAR'
my_age = 2021 - 1998
my_height = 183  # CM
my_weight = 66 # KG
my_eyes = 'BROWN'
my_teeth = 'WHITE'
my_hair = 'BLACK'
my_qualification = 'Python Dev'


while True:
  try:
    Q1 = input("Ask about me \n")

    if Q1 == "What's your name?":
        print(f"My name is {my_name}.")

    elif Q1 == "How old are you?":
        print(f"I am {my_age} years old")

    elif Q1 == "How about your height?":
        print(f"I am {my_height} CM tall")

    elif Q1 == "And your weight?":
        print(f"I am {my_weight} KG heavy")
        print("I know I'm not that heavy")

    elif Q1 == "Any other thing?":
        print(f"I have {my_eyes} eyes and my hair is {my_hair}")
        print(f"My teeth are usually {my_teeth} .")
        print('And i Absolutely Love python')

    else:
        print("Ask this questions pythonicallly")

  except:
    print("Don't be a dumbass")

