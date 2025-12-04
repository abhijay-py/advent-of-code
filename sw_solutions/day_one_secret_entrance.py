import os

here = os.path.dirname(os.path.abspath(__file__))
filename = "d1_input.txt"
direction_to_value = {'L': -1, 'R': 1}

def get_data():
    with open(os.path.join(here, filename)) as f:
        data = f.readlines()
    return data

def part_one():
    current_pos = 50
    zero_count = 0
    data = get_data()
    for line in data:
        current_pos += direction_to_value[line[0]] * int(line[1:]) 
        current_pos %= 100
        if current_pos == 0:
            zero_count += 1
            
    print(f"Initial Password: {zero_count}")

def part_two():
    current_pos = 50
    zero_count = 0
    data = get_data()
    for line in data:
        old_pos = current_pos
        full_rotations = int(line[1:]) // 100
        current_pos += direction_to_value[line[0]] * (int(line[1:]) - (100*full_rotations))
        zero_count += ((current_pos > 99 and line[0] == 'R') or (current_pos < 0 and line[0] == 'L' and old_pos != 0) or (current_pos == 0 and current_pos != old_pos)) + full_rotations 
        current_pos %= 100

    print(f"New Password: {zero_count}")

def day_one_solution():
    part_one()
    part_two()

def main():
    day_one_solution()

if __name__ == "__main__":
    main()
