from collections import Counter

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

def calculate_similarity_score(left_list, right_list):
    right_counter = Counter(right_list)
    similarity_score = 0
    for num in left_list:
        similarity_score += num * right_counter[num]
    
    return similarity_score

file_path = 'input'
left_list, right_list = read_input_file(file_path)
similarity_score = calculate_similarity_score(left_list, right_list)
print("Similarity Score:", similarity_score)