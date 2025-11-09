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
        return [1,2,4]
    
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
        return combo

    def binpacking_simple(
        self, bin_capacity: int, clauses: List[int]
    ) -> List[List[int]]:
        return [1,2,4]

    def binpacking_bestcase(
        self, bin_capacity: int, clauses: List[int]
    ) -> List[List[int]]:
        return [1,2,4]
