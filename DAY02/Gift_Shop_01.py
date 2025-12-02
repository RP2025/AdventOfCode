import re

def check_pattern(num):
    return bool(re.fullmatch(r"(.+)\1", str(num)))

def Gift_Shop_01(file_path):
    
    invalid_sum = 0

    with open(file_path) as f:
        data = f.read()

    ranges = [
        tuple(map(int, p.split("-")))
        for p in data.replace("\n", "").split(",")
        if p
    ]

    for a,b in ranges:
        for num in range(a,b+1):
            if check_pattern(num):
                invalid_sum += num

    return invalid_sum

print(Gift_Shop_01("DAY02/input.txt"))