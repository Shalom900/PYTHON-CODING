command =""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already Statrted!")
        else:
            started = True
            print("Car started...")
    elif command == "stopped":
        if not started:
            print("Car is already stopped")
        else:
            started = False   
            print("Car stopped.")
    elif command == "help":
        print("""
Start - to Start the car
Stop - to stop the car
quit - to exit
    """)
    elif command == "quit":
        break
    else:
        print("I dont Understand this")
       
   
        


 

    


   


    


   
