def part_one():
    current_pos = 50
    direction_to_value = {'L': -1, 'R': 1}
    zero_count = 0
    with open("D1_Secret_Entrance/sw_solution/input.txt") as f:
        data = f.readlines()
    for line in data:
        current_pos += direction_to_value[line[0]] * int(line[1:]) 
        current_pos %= 100
        if current_pos == 0:
            zero_count += 1
    print(f"Initial Password: {zero_count}")

def part_two():
    current_pos = 50
    direction_to_value = {'L': -1, 'R': 1}
    zero_count = 0
    with open("D1_Secret_Entrance/sw_solution/input.txt") as f:
        data = f.readlines()
    for line in data:
        old_pos = current_pos
        full_rotations = int(line[1:]) // 100
        current_pos += direction_to_value[line[0]] * (int(line[1:]) - (100*full_rotations))
        zero_count += ((current_pos > 99 and line[0] == 'R') or (current_pos < 0 and line[0] == 'L' and old_pos != 0) or (current_pos == 0 and current_pos != old_pos)) + full_rotations 
        current_pos %= 100
    print(f"New Password: {zero_count}")

def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()
