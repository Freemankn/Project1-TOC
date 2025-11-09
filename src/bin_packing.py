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
        combo = []
        cur_combo = []

        def backtracker(remaining_capacity: int, available_clauses: List[int]):
            if remaining_capacity == 0:
                combo.append(cur_combo.copy())
                return
            elif remaining_capacity < 0 or len(available_clauses) == 0:
                return

            cur_clause = available_clauses[0]
            cur_combo.append(cur_clause)
            backtracker(remaining_capacity - cur_clause, available_clauses[1:])
            cur_combo.pop()

            backtracker(remaining_capacity, available_clauses[1:])

        backtracker(bin_capacity, clauses)
        if len(combo) == 0:
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

        return subsets_without_first + subsets_with_first

    def binpacking_bruteforce(
        self, bin_capacity: int, clauses: List[int]
    ) -> List[List[int]]:
        subsets = self.generate_subsets(clauses)
        combo = []
        for bin in subsets:
            if sum(bin) == bin_capacity:
                combo.append(bin)
        if len(combo) == 0:
            return [[0]]
        return combo

    def binpacking_simple(
        self, bin_capacity: int, clauses: List[int]
    ) -> List[List[int]]:
        pass

    def binpacking_bestcase(
        self, bin_capacity: int, clauses: List[int]
    ) -> List[List[int]]:
        return [1,2,4]
