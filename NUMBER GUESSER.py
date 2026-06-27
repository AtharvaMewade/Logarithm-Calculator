import math # Imports Math Library To Use Logs

print("This Program Guesses User's No. Using Bisection Search Or O(log n)")
max_range = int(input("Enter The Maximum Range To Play With:- ")) # Asks User To Play With What No. Of Maximum Range:
min_range = 0 # Sets The Smallest No. To '0'
print("Keep Your No. Ready In Mind") # States User To KeepThe No. Ready In Their Mind

# Calculating Log Base 2 Of 'max_range' To Get The Maximum Number Of Splits Needed
Guesses_Required = int(math.log(max_range, 2)) # Sets It In Intefer Type If In Fraction:- 
print(f"The Algorithm Requires {Guesses_Required + 1} Guesses: ") # States User How Many Guesses Are Required For Algorithm
Guesses = 0

# Loop Runs Till There Is Only One No. Left Due To Rigorous Filteration
while min_range <= max_range: # The Loop Runs Till
    Pool_Size = (max_range - min_range) # States User How Many Possible Values Are Left After Each FIlteration
    print("The Remaining Left No. Are:", Pool_Size)# Prints It After Every Filteration
    print("Guesses No:", Guesses)
    
    # Uses Bisection Search To Find Midpoint
    midpoint = (max_range+min_range)//2
    
    try:
        guess = int(input(f"Enter 1 If Your Guess Is Greater Or Equal {(max_range+min_range)//2}, Enter 2 If Your Guess Is Lesser"))              
        
        # If Number Is Higher, Shift The Bottom Boundary Up Past The Midpoint
        if guess == 1: 
            min_range = midpoint + 1
            Guesses +=1
            
        # If Number Is Lower, Shift The Top Boundary Down Below The Midpoint
        if guess == 2:
            max_range = midpoint - 1
            Guesses += 1
        
    except:
        # Intercepts Random Letter Inputs So The Terminal Doesn't Crash
        print("Invalid Input, Restart Program And Enter Valid Inputs:")

# Boundaries Fully Collapsed Due To Massive Filteration, 'max_range' Holds The Final Locked Value
print("Your No. Is", max_range)

