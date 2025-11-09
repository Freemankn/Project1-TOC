import csv
import matplotlib.pyplot as plt

sizes_solved = []
times_solved = []

sizes_unsolved = []
times_unsolved = []

with open("../results/brute_force_binpacking_sat_solver_results.csv", newline="") as f:
    reader = csv.DictReader(f)
    # To avoid multi-row duplicates per instance, track first time seen
    seen = set()

    for row in reader:
        inst_id = (row["instance_id"], row["method"])
        if inst_id in seen:
            continue
        seen.add(inst_id)

        bin_capacity = int(row["bin_capacity"])
        bins_array_str = row["bins_array"]
        time_taken = float(row["time_taken"])

        # interpret bins_array string; "[]" means no solution
        has_solution = bins_array_str.strip() != "[]"

        # define instance size; you can also look it up from input file
        # simplest: use bin_capacity, or number_of_items from a separate map
        # for now, let's say size = bin_capacity (or precomputed length)
        instance_size = bin_capacity  # or replace with real size

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

plt.xlabel("Problem size (e.g., number of items)")
plt.ylabel("Time taken (seconds)")
plt.title("Brute Force Bin-Packing: Time vs Problem Size")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("plots_binpacking_bruteforce_teamname.png")
plt.show()
