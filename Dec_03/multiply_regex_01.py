import re

def read_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    return content

def extract_patterns(content):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.finditer(pattern, content)
    
    total = 0
    for match in matches:
        x, y = map(int, match.groups())
        result = x * y
        total += result
        print(f"Multiplying {x} and {y}")
    return total

filepath = 'input'
content = read_file(filepath)
result = extract_patterns(content)
print(f"Total multiplication result: {result}")