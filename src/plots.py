import csv
import matplotlib.pyplot as plt

# 1) Build size map from input file
sizes_by_instance = {}
with open("../input/binpacking.txt") as f:
    for idx, line in enumerate(f):
        parts = line.split()
        if not parts:
            continue
        instance_size = len(parts) - 1  # capacity + items → items count = len-1
        sizes_by_instance[str(idx)] = instance_size

# 2) Prepare lists for plotting
sizes_solved = []
times_solved = []

sizes_unsolved = []
times_unsolved = []

# 3) Read results CSV
with open("../results/brute_force_binpacking_sat_solver_results.csv", newline="") as f:
    reader = csv.DictReader(f)
    seen = set()

    for row in reader:
        inst_id = (row["instance_id"], row["method"])
        if inst_id in seen:
            continue
        seen.add(inst_id)

        instance_id_str = row["instance_id"]
        time_taken = float(row["time_taken"])
        bins_array_str = row["bins_array"].strip()

        has_solution = bins_array_str != "[0]"

        # 🔹 Here is the important part: get size from the map
        instance_size = sizes_by_instance[instance_id_str]

        if has_solution:
            sizes_solved.append(instance_size)
            times_solved.append(time_taken)
        else:
            sizes_unsolved.append(instance_size)
            times_unsolved.append(time_taken)

# 4) Plot
plt.figure()
plt.scatter(sizes_solved, times_solved, color="green", label="Solution exists")
plt.scatter(sizes_unsolved, times_unsolved, color="red", label="No solution")

plt.xlabel("Problem size (number of items)")
plt.ylabel("Time taken (seconds)")
plt.title("Brute Force Bin-Packing: Time vs Problem Size")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("plots_binpacking_bruteforce_teamname.png")
plt.show()
