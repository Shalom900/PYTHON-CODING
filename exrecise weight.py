def Contiune_Operation():
    while True:
        weight = int(input("Weight: "))
        p = weight / 0.45
        K = weight * 0.45
        unit = input("(P)bs or (K)g:  ")
        if unit.upper() == "K":
            print(f"You are {K} Kilogram")
        elif unit == "p":
            print(f"You are {p} pounds")
        else:
            print("Input a proper value")
        Continue = input("DO YOU WANT TO DO ANOTHER CONVERSION, IF YES 'Y' AND IF NO 'N': ")
        if Continue.upper() != "Y":
            break
        
Contiune_Operation()
