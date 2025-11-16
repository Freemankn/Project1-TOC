# Libraries
import csv
import matplotlib.pyplot as plt

# Plotting Variables
sizes_solved = []
times_solved = []
sizes_unsolved = []
times_unsolved = []

# Paths
csv_result_path = 'results'
txt_input_path = 'input'

# Files
csv_files = [
    'best_case_check_Twin_Track_Trio.csv',
    'brute_force_check_Twin_Track_Trio.csv',
    'btracking_check_Twin_Track_Trio.csv'
]
txt_file = 'check_Twin_Track_Trio.txt'

coinsKnapsack = []  # Variable to hold

# Finds the len of each set of coins
with open(f"../{txt_input_path}/{txt_file}", "r") as f:
    for line in f:
        coinsKnapsack.append(len(line.split()) - 1)

# Reading in all the data and matching up with knapsack length
for file in csv_files: # Loop checks data for each type of solution
    with open(f"../{csv_result_path}/output_{file}", newline="") as f:
        reader = csv.DictReader(f)
        seen = set()

        for row in reader: # Reads in csv line by line
            instance_id = int(row["instance_id"])
            # Stops duplication of same times for multiple solutions
            if instance_id in seen:
                continue
            seen.add(instance_id)

            time_taken = float(row["time_taken"])
            bins_array_str = row["bins_array"]

            has_solution = bins_array_str.strip() != "[0]"  # Only zero coin means no solution
            instance_size = coinsKnapsack[instance_id]  # Use coinsKnapsack count as problem size (x value)

            # Creates x and y pairs for both solved and unsolved coin sets
            if has_solution:
                sizes_solved.append(instance_size)
                times_solved.append(time_taken)
            else:
                sizes_unsolved.append(instance_size)
                times_unsolved.append(time_taken)

    # Plotting of the data
    plt.figure()
    plt.scatter(sizes_solved, times_solved, color="green", label="Solution exists")
    plt.scatter(sizes_unsolved, times_unsolved, color="red", label="No solution")

    plt.xlabel("Problem size (number of coins in instance)")
    plt.ylabel("Time taken (seconds)")
    plt.title(f"{file}: Time vs Problem Size")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(f"plots_binpacking_{file.replace('.csv', '')}.png") # Saves to png
    plt.show()