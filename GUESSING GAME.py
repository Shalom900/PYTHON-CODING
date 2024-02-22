def Continue_Game():
    while True:
    
        SECRET_NUMBER = 9
        GUESS_1 = 0
        GUESS_LIMIT = 3
        while GUESS_1 < GUESS_LIMIT:
            GUESS_2 = int(input("Guess:  "))
            GUESS_1 += 1
            if GUESS_2 == SECRET_NUMBER:
                print("You Won")
                break
        else:
            print("SOrry you failed")

        Continue = input("DO YOU WANT TO GUESS ANOTHER ONE, IF YES 'Y' AND IF NO 'N': ")
        if Continue.upper() != "Y":
            break
        
Continue_Game()

    


   
