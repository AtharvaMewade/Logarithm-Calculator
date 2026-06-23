print("This Program Is Made To Calculate Logarithms: ")
choice = int(input("Enter 1 To Find Base: , 2 To Find Target: , 3 To Find Steps: "))# Asks User For Input
try: #Tries Interpreting User's Input Based On 1, 2, 3
    if choice == 1: #Checks If User's Input Is 1 Or Not
        steps = float(input("Enter The Step Of Logarithm: ")) # Asks User For Logarithm's Step
        target = float(input("Enter The Logarithm Of Target:")) #Asks User's Target
        if steps <=0 or target <= 0 : # If steps's Value Inserted By User Is Greater Or Lesser Than '0'
            print("Undefined Input ! Restart The Program And Insert Valid Inputs:")
        base = target**(1/steps) # By Adding Brackets, We Designed An Cnstraint That 0.3333333333333333 Is Close To  FPU [Floating-Point Unit] 
        print("The Base Of Logarithm Is:", base)
    elif choice == 2: # Checks If 'choice' input is 2
        steps = float(input("Enter The Step Of Logarithm:")) #Asks User For Steps's Input
        base = float(input("Enter The Base Of Logarithm:")) #Asks User For Base Of Log
        if base <= 0 or steps <=0: # If The Input Is Equal Or Lesser Than Zero The:-
            print("Invalid Input: Restart Program And Add Correct Inputs")
        target = base ** steps # Nothing Complex, It Is Just Basically exponents
        print("The Target Of Logarithm Is:", target)
    elif choice == 3:
        base = float(input("Enter The Base Of Logarithm:")) # Asks User For Logarith's Base
        target = float(input("Enter The Target Of Logarithm:")) # Asks User For Target
        count = 0 # Assignment Of Empty Bracket. Here, count = 0
        if base <= 0 or target <= 0 or base == 1:
            print("Invalid Input!, Restart Program And Enter Valid Inputs:-")
        else:
            while target > 1: # Runs Loop If Target Is Greater Than 1.
                target = target / base # Division Of Target By Base And Every Time That's Done A New Target Value Is Recieved Which Gets Smaller Everytime
                count += 1 # The No. Of Times The Above Procedure Is Done, One I Added To It
            print("The Steps Of Logarithm Is:", count)

except: # Acts As A Safety Net Preventing Program To Crash
    print("Error: Invalid Input, Restart The Program And Enter Valid Inputs:") # If User Presents Invalid Input, Then It Prints This Statement