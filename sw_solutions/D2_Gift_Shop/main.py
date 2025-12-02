def main():
    with open("sw_solution/D2_Gift_Shop/input.txt") as f:
        data = f.readline().strip().split(',')
    
    pairs = [(int(j) for j in entry.split('-')) for entry in data]
    temp = [len(entry.split('-')[0]) for entry in data]
    pair_len = [i / 2 if i / 2.0 == i // 2 else -1 for i in temp]
    

if __name__ == "__main__":
    main()
