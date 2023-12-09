def read_input(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        times = [int(x) for x in lines[0].split(":")[1].strip().split()]
        distances = [int(x) for x in lines[1].split(":")[1].strip().split()]
        return times, distances

def possible_wins(time, distance):
    count = 0
    for i in range(0, time + 1):
        dist = i * (time - i)
        if dist > distance:
            count += 1
    print(f"Count: {count}")
    return count
        
if __name__ == "__main__":
    times, distances = read_input("input.txt")
    ans = 1
    for i in range(len(times)):
        ans *= possible_wins(times[i], distances[i])
    print(f"Part1: {ans}")