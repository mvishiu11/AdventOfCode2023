from multiprocessing import process

class Card:
    def __init__(self, id, winning_numbers, your_numbers):
        self.id = id
        self.winning_numbers = winning_numbers
        self.your_numbers = your_numbers
    

def read_input(input_file):
    with open(input_file) as f:
        cards = f.read().splitlines()
    
    out = []
    for card in cards:
        winning_numbers, your_numbers = card.split(" | ")
        id = int(winning_numbers.split(":")[0].split()[1])
        winning_numbers = set(map(int, winning_numbers.split(":")[1].split()))
        your_numbers = list(map(int, your_numbers.split()))
        out.append(Card(id, winning_numbers, your_numbers))
    return out

def process_card(card):
    winning_numbers, your_numbers = card.winning_numbers, card.your_numbers
    points = 0
    for number in your_numbers:
        if number in winning_numbers:
            points += 1
               
    return points

def count_cards(cards, counts):
    for card in cards:
        matches = process_card(card)
        for j in range(matches):
            counts[card.id + j + 1] += counts[card.id]
    sum = 0
    for card, count in counts.items():
        sum += count
    return sum
            

if __name__ == "__main__":
   
   test = read_input("test.txt") 
   assert count_cards(test, {card.id : 1 for card in test}) == 30
   
   cards = read_input("input.txt")
   counts = {card.id : 1 for card in cards}
   print(f"Total cards: {count_cards(cards, counts)}") 