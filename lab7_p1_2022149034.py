import re

def find_function_declarations_and_calls(file_path):
    func_decl_pattern = r"def\s+(\w+)\(.*\):"
    func_call_pattern = r"\b(\w+)\(.*\)"

    declarations = {}
    calls = {}

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        decl_match = re.search(func_decl_pattern, line)
        if decl_match:
            func_name = decl_match.group(1)
            declarations[func_name] = i + 1

        call_matches = re.finditer(func_call_pattern, line)
        for match in call_matches:
            func_name = match.group(1)
            if func_name not in calls:
                calls[func_name] = []
            calls[func_name].append(i + 1)

    output = ""
    for func, decl_line in declarations.items():
        call_lines = calls.get(func, [])
        output += f"{func}: def in {decl_line}, calls in {call_lines}\n"

    return output.strip()

file_path = 'input_7_1.txt'

print(find_function_declarations_and_calls(file_path))
