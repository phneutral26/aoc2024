import re

def read_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    return content

def extract_patterns(content):
    pattern = r'(do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\))'
    matches = re.finditer(pattern, content)
    
    total = 0
    enabled = True
    
    for match in matches:
        instruction = match.group(1)
        
        if instruction == 'do()':
            enabled = True
        elif instruction == "don't()":
            enabled = False
        elif enabled and instruction.startswith('mul'):
            x, y = map(int, match.group(2, 3))
            result = x * y
            total += result
            print(f"Multiplying {x} and {y}")
    
    return total

filepath = 'input'
content = read_file(filepath)
result = extract_patterns(content)
print(f"Total multiplication result: {result}")