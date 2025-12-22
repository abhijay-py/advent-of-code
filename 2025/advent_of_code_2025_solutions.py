from day_one_secret_entrance import day_one_solution
from day_two_gift_shop import day_two_solution
from day_three_lobby import day_three_solution
from day_four_printing_department import day_four_solution
from day_five_cafeteria import day_five_solution
from day_six_trash_compactor import day_six_solution
from day_seven_laboratories import day_seven_solution
from day_eight_playground import day_eight_solution

def output_all_solutions():
    print("\nAdvent of Code 2025 Solutions:", end="\n\n")

    print("Day 1 Solutions:")
    day_one_solution()
    print("\nDay 2 Solutions:")
    day_two_solution()
    print("\nDay 3 Solutions:")
    day_three_solution()
    print("\nDay 4 Solutions:")
    day_four_solution()
    print("\nDay 5 Solutions:")
    day_five_solution()
    print("\nDay 6 Solutions:")
    day_six_solution()
    print("\nDay 7 Solutions:")
    day_seven_solution()
    print("\nDay 8 Solutions:")
    day_eight_solution()
    print()

def main():
    output_all_solutions()

if __name__ == "__main__":
    main()