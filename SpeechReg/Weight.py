weight = float(input("Please input weight \n"))
unit = input("(K)g or (L)bs \n")

if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs" + str(converted))

if unit.upper() == "L":
    converted = weight * 0.45
    print("Weight in Kgs:" + str(converted))
else:
    print("Enter either K or L")
