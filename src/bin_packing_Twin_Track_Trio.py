"""
SAT Solver - DIMACS-like Multi-instance Format
----------------------------------------------------------
Project 1: Tough Problems & The Wonderful World of NP

INPUT FORMAT (multi-instance file):
-----------------------------------
Each instance starts with a comment and a problem definition:

bin_capacity <capacity>
...

Example:
10 2 5 4 7 1 3 8 6

OUTPUT:
-------
A CSV file named 'resultsfile.csv' with columns:
instance_id,bin_capacity,bins_array,method,time_taken


EXAMPLE OUTPUT
------------
instance_id,bin_capacity,bins_array,method,time_taken
0,10,"[8, 2]",BruteForce,9.862499427981675e-05
0,10,"[7, 3]",BruteForce,9.862499427981675e-05

"""

from typing import List



from src.helpers.bin_packing_helper import BinPackingAbstractClass


class BinPacking(BinPackingAbstractClass):
    """
    NOTE: The output of the CSV file should be same as EXAMPLE OUTPUT above otherwise you will loose marks
    For this you dont need to save anything just make sure to return exact related output.

    For ease look at the Abstract Solver class and basically we are having the run method which does the saving
    of the CSV file just focus on the logic
    """

    def binpacking_backtracing(
            self, bin_capacity: int, clauses: List[int]
    ) -> List[List[int]]:
        # Keeps track of current backtracking positions and passing conditions
        combo = []
        cur_combo = []

        def backtracker(remaining_capacity: int, available_clauses: List[int]):
            # Base Cases
            if remaining_capacity == 0: # Passing
                combo.append(cur_combo.copy())
                return
            elif remaining_capacity < 0 or len(available_clauses) == 0: # Failing
                return

            # Branch checks current clause
            cur_clause = available_clauses[0]
            cur_combo.append(cur_clause)
            backtracker(remaining_capacity - cur_clause, available_clauses[1:])
            cur_combo.pop()

            # Branch goes on without checking first clause
            backtracker(remaining_capacity, available_clauses[1:])

        backtracker(bin_capacity, clauses) # First call to backtrack
        if len(combo) == 0: # No passing Cases
            return [[0]]
        return combo
    
    # Function to generate subsets for the jar
    @staticmethod
    def generate_subsets(items):
        if not items:
            return [[]]              # base case

        first = items[0]
        rest = items[1:]

        subsets_without_first = BinPacking.generate_subsets(rest)

        subsets_with_first = []
        for subset in subsets_without_first:
            subsets_with_first.append([first] + subset)

        return subsets_without_first + subsets_with_first # returned set of subsets.

    def binpacking_bruteforce(
        self, bin_capacity: int, clauses: List[int]
    ) -> List[List[int]]:
        subsets = self.generate_subsets(clauses) # get all subsets
        combo = []
        for bin in subsets:
            if sum(bin) == bin_capacity: # checks if sum of bin is equal to the targer
                combo.append(bin)
        if len(combo) == 0: # if no bin works, return a [[0]] to signify that it's no solution.
            return [[0]]
        return combo

    def binpacking_simple(
        self, bin_capacity: int, clauses: List[int]
    ) -> List[List[int]]:
        pass

    def binpacking_bestcase(
        self, bin_capacity: int, clauses: List[int]
    ) -> List[List[int]]:
        bestCases = [float('inf'), []] #[the closest distance to target, subsets with the closest distance to target]
        subsets = self.generate_subsets(clauses) #get all the subsets
        for bin in subsets: #terate through subsets
            distanceFromTarget = abs(sum(bin)-bin_capacity) #get how close the subset is to the target
            if distanceFromTarget == bestCases[0]: #if the distance is equal to our best distance so far...
                bestCases[1].append(bin) #add it to the list of subsets with the closest distance to target
            elif distanceFromTarget < bestCases[0]: #if the distance is less than out best distance so far
                bestCases[0] = distanceFromTarget #update our best distance from the the target
                bestCases[1] = [bin] #start a new list of subsets with the new closest distance to the target, starting with the current subset
        return bestCases[1] #return the list of best subsets

