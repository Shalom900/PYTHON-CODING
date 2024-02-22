#Turning an AC On and Off
def Continue_On():
    while True:
        First_Number = "YES"
        On = True
        Off = True
        On_AC = input("Press Yes to turn the Air Condition: ").upper()
        if On_AC == First_Number:
            if On:
               print("The Air Condition is on")
            
        elif On_AC != First_Number:
            print("Error value")
        Continue = input("Do YOu wish to on the AC Again if Yes Y/ No N:   ").upper()
        if Continue != "Y":
            break
        else:
            print("Choose the Correct Value")
        On_AC = input("Press Yes to turn the Air Condition: ").upper()
        print("The Air Condition is alrady on")
        if On_AC == Off:
            print("The AC is off")
        Continue = input("Do YOu wish to Contine if Yes Y/ No N:   ").upper()
        if Continue != "Y":
            break
Continue_On()
        
        
    

