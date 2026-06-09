import os, heapq
from collections import deque
import time

#TODO DAY 9 PART TWO

here = os.path.dirname(os.path.abspath(__file__))
filename = "input_files/d9_input.txt"

def get_data():
    with open(os.path.join(here, filename)) as f:
        data = f.readlines()
    data_out = [tuple(int(i) for i in line.strip().split(',')) for line in data]
    return data_out

def part_one():
    points = get_data()
    
    max_area = 0
    for i in range(len(points)):
        point1 = points[i]
        for j in range(i + 1, len(points)):
            point2 = points[j]
            area = (abs(point1[0] - point2[0]) + 1) * (abs(point1[1] - point2[1]) + 1)
            if area > max_area:
                max_area = area
    print(f"Maximum Red Tile Cornered Area: {max_area}")

#WIP inefficient solution (coming back after other days)
def part_two():
    red_tiles = set(get_data())
    prev_tile = None
    green_tiles = set()
    internal_green_tiles = set()
    row_scan = {}
    area_heap = []

    for tile in red_tiles:
        if prev_tile is not None:
            if tile[0] == prev_tile[0]:
                for y in range(min(tile[1], prev_tile[1]), max(tile[1], prev_tile[1]) + 1):
                    green_tiles.add((tile[0], y))
            else:   
                for x in range(min(tile[0], prev_tile[0]), max(tile[0], prev_tile[0]) + 1):
                    green_tiles.add((x, tile[1]))
        else:
            first_tile = tile
        prev_tile = tile
    
    if first_tile[0] == prev_tile[0]:
        for y in range(min(first_tile[1], prev_tile[1]), max(first_tile[1], prev_tile[1]) + 1):
            green_tiles.add((first_tile[0], y))
    else:
        for x in range(min(first_tile[0], prev_tile[0]), max(first_tile[0], prev_tile[0]) + 1):
            green_tiles.add((x, first_tile[1]))

    border_tiles = red_tiles.union(green_tiles)
    border_tiles_sorted = list(border_tiles)
    border_tiles_sorted.sort(key=lambda t: t[0])

    for tile in border_tiles_sorted:
        x, y = tile
        if y not in row_scan.keys():
            row_scan[y] = [x]
        elif (x-1, y) not in border_tiles_sorted or (x+1, y) not in border_tiles_sorted:
            row_scan[y].append(x)

    sorted_y = list(row_scan.keys())
    sorted_y.sort()

    for y in row_scan.keys():
        row_scan[y].sort()

        for i in range(0, len(row_scan[y]), 2):
            for x in range(row_scan[y][i] + 1, row_scan[y][i + 1]):
                internal_green_tiles.add((x, y))

                
    all_colored_tiles = red_tiles.union(green_tiles).union(internal_green_tiles)    

    for i in range(len(red_tiles)):
        point1 = red_tiles[i]
        for j in range(i + 1, len(red_tiles)):
            point2 = red_tiles[j]
            area = (abs(point1[0] - point2[0]) + 1) * (abs(point1[1] - point2[1]) + 1)
            heapq.heappush(area_heap, (-area, (point1, point2)))

    while area_heap:
        area, (point1, point2) = heapq.heappop(area_heap)
        area = -area
        cornered_area_valid = True

        for x in range(min(point1[0], point2[0]), max(point1[0], point2[0]) + 1):
            for y in range(min(point1[1], point2[1]), max(point1[1], point2[1]) + 1):
                if (x, y) not in all_colored_tiles:
                    cornered_area_valid = False
                    break
            if not cornered_area_valid:
                break

        if cornered_area_valid:
            print(f"Largest Fully Colored Cornered Area: {area}")
            break

def day_nine_solution():
    part_one()
    #part_two()
   
def main():
    day_nine_solution()
    
if __name__ == "__main__":
    main()
