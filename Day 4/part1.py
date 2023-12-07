def read_input(input_file):
    with open(input_file) as f:
        return f.read().splitlines()
    

def calculate_points(cards):
    total_points = 0

    for card in cards:
        winning_numbers, your_numbers = card.split(" | ")
        winning_numbers = set(map(int, winning_numbers.split(":")[1].split()))
        your_numbers = list(map(int, your_numbers.split()))

        points = 0
        for number in your_numbers:
            if number in winning_numbers:
                if points == 0:
                    points += 1
                else:
                    points *= 2
                winning_numbers.remove(number)
        total_points += points

    return total_points


if __name__ == "__main__":
    assert calculate_points(read_input("test.txt")) == 13
    total_points = calculate_points(read_input("input.txt"))
    print("Total points:", total_points)
