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
            # Decision Matrix -- Adjusts The Boundraries Of The Resukts
            if test_result > target: #If Result Is Higher Target
                highest_possible_base = base# Assumption That Highest Possible Base Is The Base
            elif test_result < target:# If Above COndition Is False Then Then It Checks If The Results Are Smaller Than Target
                lowest_possible_base = base #Then lowest POssible Base Is The Base Itself
        print("The Base Of Logarithm Is:", base)# Prints The Base Which Satisfies The Condition Of 'if' or 'elif'
            
    elif choice == 2:
        steps = float(input("Enter The Step Of Logarithm:"))
        base = float(input("Enter The Base Of Logarithm:"))
        target = 1
        while steps > 0:
            target = target * base
            steps -= 1
        print("The Target Of Logarithm Is:",target)
    
    else:
        choice == 3
        base = float(input("Enter The Base Of Logarithm:"))
        target = float(input("Enter The Target Of Logarithm:"))
        count = 0
        while target > 1:
            target = target/base
            count += 1
        print("The Steps Of Logarithm Is:",count)

except:
    print("Error: Invalid Input, Restart The Program And Enter Valid Inputs:")