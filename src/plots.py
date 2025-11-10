import csv
import matplotlib.pyplot as plt

sizes_solved = []
times_solved = []

sizes_unsolved = []
times_unsolved = []

# Paths
csv_result_path = 'results'
txt_input_path = 'input'

csv_files = [
    'best_case_binpacking_sat_solver_results.csv',
    'brute_force_binpacking_sat_solver_results.csv',
    'btracking_binpacking_sat_solver_results.csv'
]
txt_file = 'binpacking.txt'

# Build coinsKnapsack indexed by instance_id
coinsKnapsack = []

with open(f"../{txt_input_path}/{txt_file}", "r") as f:
    for line in f:
        coinsKnapsack.append(len(line.split()) - 1)

for file in csv_files:
    with open(f"../{csv_result_path}/{file}", newline="") as f:
        reader = csv.DictReader(f)
        seen = set()

        for row in reader:
            instance_id = int(row["instance_id"])
            if instance_id in seen:
                continue
            seen.add(instance_id)

            time_taken = float(row["time_taken"])
            bins_array_str = row["bins_array"]
            has_solution = bins_array_str.strip() != "[0]"

            # Use coinsKnapsack count as problem size (x value)
            if instance_id < len(coinsKnapsack):
                instance_size = coinsKnapsack[instance_id]
            else:
                instance_size = 0  # fallback if input mismatch

            if has_solution:
                sizes_solved.append(instance_size)
                times_solved.append(time_taken)
            else:
                sizes_unsolved.append(instance_size)
                times_unsolved.append(time_taken)

    # Now plot
    plt.figure()
    plt.scatter(sizes_solved, times_solved, color="green", label="Solution exists")
    plt.scatter(sizes_unsolved, times_unsolved, color="red", label="No solution")

    plt.xlabel("Problem size (number of coins in instance)")
    plt.ylabel("Time taken (seconds)")
    plt.title(f"{file}: Time vs Problem Size")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(f"plots_binpacking_{file.replace('.csv', '')}.png")
    plt.show()