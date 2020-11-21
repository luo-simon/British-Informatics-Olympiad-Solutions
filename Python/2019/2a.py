input = input("> ").split(" ")

def main():
    trail(int(input[0]), str(input[1]), int(input[2]))

def update_direction(direction, instruction):
    if instruction == "F":
        return direction
    elif instruction == "R":
        return (direction + 1) % 4
    elif instruction == "L":
        return (direction + 3) % 4


def move(position, direction, trail):
    attempts = 0
    while attempts < 4:
        if direction == 0:
            new_position = (position[0], position[1] + 1)
        elif direction == 1:
            new_position = (position[0] + 1, position[1])
        elif direction == 2:
            new_position = (position[0], position[1] - 1)
        else:
            new_position = (position[0] - 1, position[1])

        if new_position in trail:
            direction = (direction + 1) % 4
            attempts += 1
        else:
            return new_position, direction
    return 1

def update_trail(position, trail, t):
    trail.append(position)
    if len(trail) > t:
        trail.pop(0)

    return trail

def trail(t, i, m):
    '''
    t : int between 1 and 1000 indicating no. moves for trail to disappear
    i : string between 1 and 10 uppercase letters {L,R,F} indicating instructions
    m : int indicating how many moves the explorer makes.
    '''
    position = (0,0); trail = list([position])
    direction = 0 # 0, 1, 2, 3 for North, East, South, West respectively.

    move_count = 0
    while True:
        for instruction in i:
            direction = update_direction(direction, instruction)
            if not move(position, direction, trail) == 1:
                position, direction = move(position, direction, trail)
            else:
                print(position); return 0
            trail = update_trail(position, trail, t)
            move_count += 1
            # Uncomment following line if you would like to see position after each move
            # print(f"[{move_count}]\t{position}")
            if move_count >= m:
                print(position); return 0

main()
