import os

here = os.path.dirname(os.path.abspath(__file__))

def get_pairs():
    with open(os.path.join(here, "input.txt")) as f:
        data = f.readline().strip().split(',')
    
    pairs = [(j for j in entry.split('-')) for entry in data]

    return pairs

def part_one():
    pairs = get_pairs()
    invalid_id_sum = 0
    #iteration_count = 0

    for i, j in pairs:
        lower_bound = int(i)
        upper_bound = int(j)
        lower_digit_count = int(len(i) // 2)
        upper_digit_count = int(len(j) // 2)
        
        if len(i) == len(j) and len(i) % 2 != 0:
            continue
        elif len(i) != len(j):
            if len(i) % 2 != 0:
                lower_bound = 10 ** (len(i))
                lower_digit_count = int((len(i) + 1) // 2)
            if len(j) % 2 != 0:
                upper_bound = 10 ** (len(j) - 1) - 1
                upper_digit_count = int((len(j) - 1) // 2)
        
        for seq_len in range(lower_digit_count, upper_digit_count + 1):
            factor = (10 ** seq_len + 1)
            current_lower = lower_bound
            current_upper = upper_bound
            if 10 ** (seq_len * 2 - 1) > lower_bound:
                current_lower = 10 ** (seq_len * 2 - 1) 
            if 10 ** (seq_len * 2) - 1 < upper_bound:
                current_upper = 10 ** (seq_len * 2) - 1
            lower_multiple = current_lower // factor
            upper_multiple = current_upper // factor 

            for m in range(lower_multiple, upper_multiple + 1):
                value = m * factor
                if value >= current_lower and value <= current_upper:
                    invalid_id_sum += value
                #iteration_count += 1
    

    print(f"Sum of Basic Invalid Gift IDs: {invalid_id_sum}")
    #print(f"Total Iterations: {iteration_count}")

def part_two():
    pairs = get_pairs()
    invalid_id_sum = 0
    #iteration_count = 0
    for i, j in pairs:
        lower_bound = int(i)
        upper_bound = int(j)
        lower_len = len(i)
        upper_len = len(j)
        values = []
        for seq_len in range(1, int(len(j) // 2) + 1):
            total_digit_counts = []
            for k in range(lower_len, upper_len + 1):
                if k % seq_len == 0 and k != 1:
                    total_digit_counts.append(k)
            #print(f"i: {i}, j: {j}, seq_len: {seq_len}, total_digit_counts: {total_digit_counts}")
            if len(total_digit_counts) == 0:
                #print()
                #print()
                continue
            
            for digit_count in total_digit_counts:
                num_ones = digit_count / seq_len
                factor = 1
                for k in range(int(num_ones) - 1):
                    factor *= 10 ** seq_len
                    factor += 1
                current_lower = lower_bound
                current_upper = upper_bound
                if 10 ** (digit_count - 1) > lower_bound:
                    current_lower = 10 ** (digit_count - 1) 
                if (10 ** digit_count - 1) < upper_bound:
                    current_upper = 10 ** digit_count - 1
                #print(f"current_lower: {current_lower}, current_upper: {current_upper}, lower_bound: {lower_bound}, upper_bound: {upper_bound}, factor: {factor}")
                lower_multiple = current_lower // factor
                upper_multiple = current_upper // factor 
                #print(f"lower_multiple: {lower_multiple}, upper_multiple: {upper_multiple}")
                for m in range(lower_multiple, upper_multiple + 1):
                    value = m * factor
                    if value >= current_lower and value <= current_upper and value not in values:
                        invalid_id_sum += value
                        values.append(value)
                        #print()
                        #print(f"i: {i}, j: {j}")
                        #print(f"VALUE: {value}")
                        #print()
                    #iteration_count += 1
        #print()
        #print()
    print(f"Sum of Advanced Invalid Gift IDs: {invalid_id_sum}")
    #print(f"Total Iterations: {iteration_count}")

def main():
    part_one()
    part_two()
    
if __name__ == "__main__":
    main()
