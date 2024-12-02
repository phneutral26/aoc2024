def read_input_file(file_path):
    with open(file_path, 'r') as file:
        first_numbers = []
        second_numbers = []
        for line in file:
            parts = line.strip().split()
            if len(parts) >= 2:
                first_numbers.append(int(parts[0]))
                second_numbers.append(int(parts[1]))
    return first_numbers, second_numbers

def find_smallest_numbers(first_list, second_list):
    pairs = {}
    first_list_sorted = sorted(first_list)
    second_list_sorted = sorted(second_list)
    
    for idx, (first, second) in enumerate(zip(first_list_sorted, second_list_sorted), 1):
        pairs[idx] = (first, second)
    
    return pairs

def distance_pairs(pairs):
    total_distance = 0
    for _, (first, second) in pairs.items():
        distance = abs(first - second)
        total_distance += distance
    return total_distance

# Test the functions
file_path = 'input'
first_list, second_list = read_input_file(file_path)
pairs = find_smallest_numbers(first_list, second_list)
print("Pairs:", pairs)
total_distance = distance_pairs(pairs)
print("Total distance:", total_distance)