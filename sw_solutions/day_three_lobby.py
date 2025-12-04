import os

here = os.path.dirname(os.path.abspath(__file__))
filename = "d3_input.txt"

def get_data():
    with open(os.path.join(here, filename)) as f:
        data = f.readlines()
    
    data_clean = [entry.strip() for entry in data]

    return data_clean

def part_one():
    data = get_data()
    total_joltage = 0
    for line in data:
        max_one = -1
        max_two = -1
        for i in range(len(line)):
            if int(line[i]) > max_one and i != len(line) - 1:
                max_one = int(line[i])
                max_two = -1
            elif int(line[i]) > max_two:
                max_two = int(line[i])
        total_joltage += max_one * 10 + max_two
    print(f"Total Two Digit Joltage: {total_joltage}")

def part_two():
    data = get_data()
    total_joltage = 0
    for line in data:
        max_values = [-1 for i in range(12)]
        for i in range(len(line)):
            updated_max = False
            for j in range(12):
                if updated_max:
                    max_values[j] = -1
                elif int(line[i]) > max_values[j] and i <= len(line) - 12 + j:
                    max_values[j] = int(line[i])
                    updated_max = True
        for i in range(12):
            total_joltage += max_values[i] * (10 ** (11 - i))    
    print(f"Total Twelve Digit Joltage: {total_joltage}")

def day_three_solution():
    part_one()
    part_two()

def main():
    day_three_solution()
    
if __name__ == "__main__":
    main()
