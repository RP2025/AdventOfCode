def Lobby_01(bank):
    k = 12  # or 2 -- This is the number of digits in each bank's joltage output
    result = ""

    start = 0
    n = len(bank)

    for remaining in range(k, 0, -1):
        end_limit = n - remaining + 1

        window = bank[start:end_limit]
        best_digit = max(window)
        pos = window.index(best_digit)

        result += best_digit

        start += pos + 1

    return int(result)

def total_joltage(file_path):
    with open(file_path) as f:
        data = f.read()

    return sum(Lobby_01(line) for line in data.split())


print(total_joltage("DAY03\lobby.txt"))

