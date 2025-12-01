def Secret_Entrance_02(file_path):
    position = 50 
    zero_hits = 0 

    with open(file_path) as f:
        for line in f:
            move = line.strip()
            if not move:
                continue

            direction = move[0] 
            distance = int(move[1:])
            
            zero_hits += distance // 100 
            
            remaining_dist = distance % 100

            if direction == 'L':
                if position != 0 and remaining_dist >= position:
                    zero_hits += 1
                position = (position - distance) % 100
                
            else: 
                if position + remaining_dist >= 100:
                    zero_hits += 1
                position = (position + distance) % 100

    return zero_hits


print(Secret_Entrance_02("DAY01\moves.txt"))
