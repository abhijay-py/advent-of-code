from day_one_secret_entrance import day_one_solution
from day_two_gift_shop import day_two_solution
from day_three_lobby import day_three_solution

def output_all_solutions():
    print("\nAdvent of Code 2025 Solutions:", end="\n\n")

    print("Day 1 Solutions:")
    day_one_solution()
    print("\nDay 2 Solutions:")
    day_two_solution()
    print("\nDay 3 Solutions:")
    day_three_solution()
    print()

def main():
    output_all_solutions()

if __name__ == "__main__":
    main()