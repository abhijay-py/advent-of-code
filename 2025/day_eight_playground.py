import os, heapq

here = os.path.dirname(os.path.abspath(__file__))
filename = "input_files/d8_input.txt"

def get_data():
    with open(os.path.join(here, filename)) as f:
        data = f.readlines()
    data_out = [tuple(int(i) for i in line.strip().split(',')) for line in data]
    return data_out

def fully_connected(circuit_point_assoc, point_count):
    try:
        circuit_len = len(list(circuit_point_assoc.values())[0])
    except:
        return False
    return circuit_len == point_count

def part_one():
    points = get_data()
    max_heap = [] #heap of distances between points (use max heap to pop any high distances first)
    point_circuit_assoc = {} #point: circuit number
    circuit_point_assoc = {} #circuit number: list of points in circuit
    circuit_sizes = {}  #index is circuit number, value is size of circuit
    sum_max_heap = [] #heap of circuit size sums
    next_circuit_num = 0
   
    for i in range(len(points)):
        point_circuit_assoc[points[i]] = -1
        for j in range(i + 1, len(points)):
            dist = abs(points[i][0] - points[j][0]) ** 2 + abs(points[i][1] - points[j][1]) ** 2 + abs(points[i][2] - points[j][2]) ** 2
            dist = dist ** 0.5
            
            heapq.heappush(max_heap, (-dist, (points[i], points[j])))
            if len(max_heap) > 1000:
                heapq.heappop(max_heap)
    
    for i in range(1000):
        try:
            neg_dist, (point1, point2) = heapq.heappop(max_heap)
        except:
            break

        circuit1 = point_circuit_assoc[point1]
        circuit2 = point_circuit_assoc[point2]
        
        if circuit1 == -1 and circuit2 == -1:
            point_circuit_assoc[point1] = next_circuit_num
            point_circuit_assoc[point2] = next_circuit_num
            circuit_sizes[next_circuit_num] = 2
            circuit_point_assoc[next_circuit_num] = [point1, point2]
            next_circuit_num += 1
        elif circuit1 != -1 and circuit2 == -1:
            point_circuit_assoc[point2] = circuit1
            circuit_sizes[circuit1] += 1
            circuit_point_assoc[circuit1].append(point2)
        elif circuit1 == -1 and circuit2 != -1:
            point_circuit_assoc[point1] = circuit2
            circuit_sizes[circuit2] += 1
            circuit_point_assoc[circuit2].append(point1)
        elif circuit1 != circuit2:
            if circuit1 > circuit2:
                temp = circuit1
                circuit1 = circuit2
                circuit2 = temp
            
            new_c1_points = circuit_point_assoc[circuit2]
            circuit_point_assoc[circuit1].extend(new_c1_points)
            circuit_sizes[circuit1] += circuit_sizes[circuit2]

            del circuit_sizes[circuit2]
            del circuit_point_assoc[circuit2]

            for point in new_c1_points:
                point_circuit_assoc[point] = circuit1

    for i in circuit_sizes.values():
        heapq.heappush(sum_max_heap, -i)

    sizes_multiplied = 1
    for i in range(3):
        try:
            sizes_multiplied *= -heapq.heappop(sum_max_heap)
        except:
            break
    print(f"Big Three Circuit Sizes Multiplied: {sizes_multiplied}")
            
def part_two():
    points = get_data()
    min_heap = [] #heap of distances between points
    point_circuit_assoc = {} #point: circuit number
    circuit_point_assoc = {} #circuit number: list of points in circuit
    circuit_sizes = {}  #index is circuit number, value is size of circuit
    sum_max_heap = [] #heap of circuit size sums
    next_circuit_num = 0
   
    for i in range(len(points)):
        point_circuit_assoc[points[i]] = -1
        for j in range(i + 1, len(points)):
            dist = abs(points[i][0] - points[j][0]) ** 2 + abs(points[i][1] - points[j][1]) ** 2 + abs(points[i][2] - points[j][2]) ** 2
            dist = dist ** 0.5
            heapq.heappush(min_heap, (dist, (points[i], points[j])))
    
    last_points_x = [-1, -1]
    data_len = len(points)

    while not fully_connected(circuit_point_assoc, data_len):
        neg_dist, (point1, point2) = heapq.heappop(min_heap)

        circuit1 = point_circuit_assoc[point1]
        circuit2 = point_circuit_assoc[point2]
        
        if circuit1 == -1 and circuit2 == -1:
            point_circuit_assoc[point1] = next_circuit_num
            point_circuit_assoc[point2] = next_circuit_num
            circuit_sizes[next_circuit_num] = 2
            circuit_point_assoc[next_circuit_num] = [point1, point2]
            next_circuit_num += 1
        elif circuit1 != -1 and circuit2 == -1:
            point_circuit_assoc[point2] = circuit1
            circuit_sizes[circuit1] += 1
            circuit_point_assoc[circuit1].append(point2)
        elif circuit1 == -1 and circuit2 != -1:
            point_circuit_assoc[point1] = circuit2
            circuit_sizes[circuit2] += 1
            circuit_point_assoc[circuit2].append(point1)
        elif circuit1 != circuit2:
            if circuit1 > circuit2:
                temp = circuit1
                circuit1 = circuit2
                circuit2 = temp
            
            new_c1_points = circuit_point_assoc[circuit2]
            circuit_point_assoc[circuit1].extend(new_c1_points)
            circuit_sizes[circuit1] += circuit_sizes[circuit2]

            del circuit_sizes[circuit2]
            del circuit_point_assoc[circuit2]

            for point in new_c1_points:
                point_circuit_assoc[point] = circuit1
        last_points_x = [point1[0], point2[0]]
    
    print(f"Last Two Connected Points Xs Multiplied: {last_points_x[0] * last_points_x[1]}")

def day_eight_solution():
    part_one()
    part_two()
   
def main():
    day_eight_solution()
    
if __name__ == "__main__":
    main()
