from random import shuffle

class NQueen():

    def __init__(self):
        pass

    # steepest ascent hill climbing algorithm
    def steepest_ascent(self, state):
        cost = 0
        curr_state = state
        while True:
            better_found = False
            curr_pairs = self.count_attacking_pairs(curr_state)
            
            # exit condition 
            if curr_pairs == 0:
                return [curr_state, cost]

            possibile_children = self.create_child_states_sa(curr_state)
            best_neighbor = None
            lowest_pairs = curr_pairs

            # find the state with the lowest pairs in conflict
            for c in possibile_children:
                curr_pairs = self.count_attacking_pairs(c)
                if curr_pairs < lowest_pairs:
                    best_neighbor = c
                    lowest_pairs = curr_pairs
                    better_found = True
            curr_state = best_neighbor
            cost += 1

            # fail if no lower state is found
            if better_found == False:  
                return [None, cost]

    # min conflict 
    def min_conflict(self, state, max_steps):
        cost = 0
        curr_state = state
        for steps in range(max_steps):
            curr_pairs = self.count_attacking_pairs(curr_state)

            # exit condition
            if curr_pairs == 0:
                return [curr_state, cost]

            # chooses a random queen in conflict 
            c_queens = self.get_conflicting_queens(curr_state)
            shuffle(c_queens)
            curr_queen = c_queens[0]


            # gets a list of the lowest conflict states
            best_neighbors = []
            lowest_value = curr_pairs
            possible_children = list(self.create_child_states_mc(curr_state, curr_queen[1]))
            for c in possible_children:
                curr_pairs = self.count_attacking_pairs(c)

                # if a new lowest state is found, start a new list 
                if curr_pairs < lowest_value:
                    best_neighbors = [c]
                    lowest_value = curr_pairs

                # if state is equal to current lowest state, append to list
                if curr_pairs == lowest_value:
                    best_neighbors.append(c)
            
            # choose a random lowest neighbor from the list
            if len(best_neighbors) > 0:
                shuffle(best_neighbors)
                curr_state = best_neighbors[0]
            cost += 1

        return [None, cost]

    # given a list of queens will remove queens that are not 
    def get_conflicting_queens(self, state):

        # get a list of queen locations
        queens_list = self.get_queens(state)
        conflicting_queens = []

        for q in range(len(queens_list)):
            for q2 in range(q + 1, len(queens_list)):
                
                # if queen is in conflict add them to the list if not already present 
                if self.check_conflicts(queens_list[q], queens_list[q2]):
                    if queens_list[q] not in conflicting_queens:
                        conflicting_queens.append(queens_list[q]) 
                    if queens_list[q2] not in conflicting_queens:
                        conflicting_queens.append(queens_list[q2]) 
        return conflicting_queens

    # creates possible children contrained to a column
    def create_child_states_mc(self, state, index):  
        for r in range(len(state)):
            if state[r][index] == 1:
                for r2 in range(len(state)):
                    if r2 != r:
                        new_state = [r[:] for r in state]
                        new_state[r][index] = 0
                        new_state[r2][index] = 1
                        yield new_state

    # creates all possible children given a state
    def create_child_states_sa(self,state):
        n = len(state)
        for r in range(n):
            for c in range(n):
                if state[r][c] == 1:
                    for r2 in range(n):
                        if r2 != r:
                            new_state = [r[:] for r in state]
                            new_state[r][c] = 0
                            new_state[r2][c] = 1
                            yield new_state

    # gets a list of the location of all queens
    def get_queens(self, state):
        list_of_queens = []
        for r in range(len(state)):
            for c in range(len(state)):
                if state[r][c] == 1:
                    list_of_queens.append((r,c))
        return list_of_queens

    # checks if two queens are conflicting 
    def check_conflicts(self, first_queen, second_queen):
        # checks for a queen on the same column
        if first_queen[0] == second_queen[0]:
            return True
        # checks for a queen on the same row
        elif first_queen[1] == second_queen[1]:
            return True
        # checks for a queen on the same diagonal
        elif abs(first_queen[0] - second_queen[0]) == abs(first_queen[1] - second_queen[1]):
            return True
        # return false if no neighbors have been found
        else:
            return False

    # gets the total amount of pairs that are indirectly or directly in conflict
    def count_attacking_pairs(self, state):
        queens_list = self.get_queens(state)
        
        total_pairs = 0
        for q in range(len(queens_list)):
            for q2 in range(q + 1, len(queens_list)):
                if self.check_conflicts(queens_list[q], queens_list[q2]):
                    total_pairs += 1
        return total_pairs