def Contiune_Operation():
    while True:
        weight = int(input("Weight: "))
        unit = input("(P)bs or (K)g:  ")
        if unit.upper() == "K":
            weight * 0.45
            print(f"You are {weight} Pounds")
        elif unit.upper() == "P":
            weight / 0.45
            print(f"You are {weight} kilos")
        else:
            print("Input a proper value")
        Continue = input("DO YOU WANT TO DO ANOTHER CONVERSION, IF YES 'Y' AND IF NO 'N': ")
        if Continue.upper() != "Y":
            break
        
Contiune_Operation()
