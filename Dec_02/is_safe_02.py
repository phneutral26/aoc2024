def is_safe_sequence(numbers):
    if len(numbers) <= 1:
        return True
    increasing = numbers[1] > numbers[0]
    for i in range(1, len(numbers)):
        current_diff = numbers[i] - numbers[i-1]
        if (increasing and current_diff <= 0) or (not increasing and current_diff >= 0):
            return False
        if abs(current_diff) < 1 or abs(current_diff) > 3:
            return False
    return True

def is_safe_row(numbers):
    if is_safe_sequence(numbers):
        return True
    for i in range(len(numbers)):
        modified_numbers = numbers[:i] + numbers[i+1:]
        if is_safe_sequence(modified_numbers):
            return True

    return False
def process_input(filename):
    safe_rows = 0
    total_rows = 0

    with open(filename, 'r') as file:
        for line in file:
            total_rows += 1
            numbers = [int(num) for num in line.strip().split()]
            if is_safe_row(numbers):
                safe_rows += 1

    return safe_rows, total_rows

# Test the data
safe_count, total_count = process_input('input')
print(f"Safe rows: {safe_count}")
print(f"Total rows: {total_count}")
print(f"Percentage safe: {(safe_count / total_count) * 100:.2f}%")