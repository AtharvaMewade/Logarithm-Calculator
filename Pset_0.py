print("This Program Is Made To Calculate Logarithms: ")
choice = int(input("Enter 1 To Find Base: , 2 To Find Target: , 3 To Find Steps: "))# Asks User For Input
try: #Tries Interpreting User's Input Based On 1, 2, 3
    if choice == 1: #CHecks If User's Input Is 1 Or Not
        steps = float(input("Enter The Step Of Logarithm: ")) # Asks User For Logarithm's Step
        target = float(input("Enter The Logarithm Of Base:")) #Asks User's Target
        #--- Architectural Anchors: Setting Up Bisection Search Work SPace
        highest_possible_base = target #Assupmtion That Higehest Base No. Could Be The Target No. Itself
        lowest_possible_base = 1 # Assupmtion That Lowest Possible Base Could Be '1' Itself
        while (highest_possible_base - lowest_possible_base) > 0.0001: #Checks If Subtraction Of Highest Possibbe Base i.e. 'Target' With 1 Is Greater Than '0.001' Or Not
            #-- Math Engine: Slices The Search Space Into Half (O(log n)efficiency)
            base = (highest_possible_base + lowest_possible_base) / 2 # Bisection Step: Guesses The Perfect Middle Term
            test_result = base ** steps #Base Is Raised To No. Of Steps
            # Decision Matrix -- Adjusts The Boundraries Of The Results
            if test_result > target: #If Result Is Higher Target
                highest_possible_base = base #Eliminates All The Higher Possibilities
            elif test_result < target:# If Above Condition Is False Then Then It Checks If The Results Are Smaller Than Target
                lowest_possible_base = base #It Eliminates All Lower Possibilities
        print("The Base Of Logarithm Is:", base)# Prints The Base Which Satisfies The Condition Of 'if' or 'elif'
            
    elif choice == 2: # Checks If 'choice' input is 2
        steps = float(input("Enter The Step Of Logarithm:")) #Asks User For Steps's Input
        base = float(input("Enter The Base Of Logarithm:")) #Asks User For Base Of Log
        target = 1.0 #Assupmtion That Target Is One
        if steps%2 !=0: #Checks if User's Input Is Odd
            target = target * base  # 1 Is Multipied With Target Because It Locks Out That '1' Remainder
        while steps > 0: # Runs Loop Till The No. Of Steps Is Equal To Zero
            base = base*base # Multiplies Itself Then It Is Assigned New 'Base' Value. The Loop Repeats Itself Till The Total Steps Are Zero
            steps = steps//2 # Floor Divides Itself Then Assigns Itself New 'Step' Value. the Loop Repeats The No. Times the Above Loop Repeatss
        print("The Target Of Logarithm Is:",target)
    
    elif choice == 3:
        base = float(input("Enter The Base Of Logarithm:")) # Asks User For Logarith's Base
        target = float(input("Enter The Target Of Logarithm:")) # Asks User For Target
        count = 0 # Assignment Of Empty Bracket. Here, count = 0
        while target > 1: # Runs Loop If Target Is Greater Is Greater Than 1.
            target = target/base # Division Of Target By Base And Every Time That's Done A New Target Value Is Recieved Which Gets Smaller Everytime
            count += 1 # The No. Of Times The Above Procedure Is Done, One I Added To It
        print("The Steps Of Logarithm Is:",count)

except: # Acts As A Safety Net Preventing Program To Crash
    print("Error: Invalid Input, Restart The Program And Enter Valid Inputs:") # If User Presents Invalid Input, Then It Prints This Statement