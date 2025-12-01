def Secret_Entrance_01(file_path):
    position = 50
    zero_count = 0

    with open(file_path, "r") as f:
        for line in f:
            move = line.strip()
            if not move:
                continue
            
            direction = move[0]
            dist = int(move[1:])

            if direction == "L":
                position = (position - dist) % 100
            else:
                position = (position + dist) % 100

            if position == 0:
                zero_count += 1

    return zero_count

print(Secret_Entrance_01("DAY01\moves.txt"))
