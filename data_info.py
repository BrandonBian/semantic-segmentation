if __name__ == "__main__":
    # Initialize a counter
    room_count = 0
    total = 0

    # Open the file and read line by line
    with open('data/ADEChallengeData2016/sceneCategories.txt', 'r') as file:
        for line in file:
            total += 1
            # Check if 'room' is in the line
            if 'room' in line.split()[1]:
                room_count += 1

    print(f"Number of lines with 'room': {room_count}")
    print(f"Total number of lines: {total}")