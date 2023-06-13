
from time import time 
from random import randint
from nQueen import NQueen

# creates a random state of n size. created so that there is 1 n per column 
def random_state(n):
    arr = [[0 for c in range(n)] for r in range(n)]
    for c in range(n):
        arr[randint(0,n - 1)][c] = 1

    return arr

# prints out the 2d array in a more readable form 
def print_state(state):
    for r in range(len(state)):
        for c in range(len(state)):
            print(state[r][c], end=" ")
        print()
    print()


# runs the given test a number of times based on the count value
def bulk_test(version, test_cases):
   
    # initalize variable to keep track of analysis
    average_time = 0.0
    solved_states = 0
    average_cost = 0.0

    # loops test based on input value
    for case in range(test_cases):

        #creates a random state
        initial_state = random_state(8)

        # calls one of the two algorithms and measures time taken 
        if version == 1: 
            start_time = time()
            final_results = NQueen().steepest_ascent(initial_state)
            end_time = time()
            
        elif version == 2:
            start_time = time()
            final_results = NQueen().min_conflict(initial_state, 100)
            end_time = time()
        
        # counts solution if one is return 
        if final_results[0] != None:
            solved_states += 1


        # calculates the average values
        average_time = (average_time + (end_time - start_time))/2
        average_cost = (average_cost + (final_results[1]))/2

    # Prints out the stats of the test 
    print("Number of Boards: ", test_cases)
    print("Solved Percentage", str(solved_states / test_cases * 100) + "%")
    print("Average Time: ", average_time)
    print("Average Cost: ", average_cost)

# Asks the user what algorithm to use
def start_menu():
    while True:
        print("Select:")
        print("[1] Steepest Ascent")
        print("[2] Min-Conflict")
        print("[3] Exit")
        start_input = input()

        if start_input == "1":
            print()
            return 1

        elif start_input == "2":
            print()
            return 2

        # exits program
        elif start_input == "3":
            print("Goodbye")
            quit()

# Asks user for how many tests are run 
def test_menu(test_type):
    while True:
        print("Select:")
        print("[1] Single Test")
        print("[2] Bulk Test")
        print("[3] Exit")
        start_input = input()

        # Single N Queen problem test and print out the solution
        if start_input == "1":
           
            print()
            initial_state = random_state(8)
            print("Initial State: ")
            print_state(initial_state)
            start_time = time()
            if test_type == 1:
                final_results = NQueen().steepest_ascent(initial_state)
            elif test_type == 2:
                final_results = NQueen().min_conflict(initial_state, 100)
            end_time = time()

            if final_results[0] != None:
                print("Final State: ")
                print_state(final_results[0])
            else:
                print("No Solution Found")
            
            print("Time: ", (end_time - start_time))
            print("Cost: ", final_results[1])
            break
        
        # Runs x number of test and prints out the averages 
        if start_input == "2":
            print()
            # input validation
            while True: 
                try:
                    num_states = int(input("Enter number of states: "))
                except ValueError:
                    print("You must enter a valid number.")
                else: 
                    if num_states > 0:
                        break
                    else:
                        print("The number must be greater than 0")
            print()

            # Run the given test
            bulk_test(test_type, num_states)
        
            break
        # exits program
        elif start_input == "3":
            print("Goodbye")
            quit()

def main():
    verison = start_menu()
    test_menu(verison)

if __name__=="__main__":
    main()






