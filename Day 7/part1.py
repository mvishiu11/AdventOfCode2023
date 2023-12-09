from functools import cmp_to_key


def evaluate_hand(hand):
    # Function to evaluate the strength of a hand
    labels = "AKQJT98765432"
    counts = [hand.count(label) for label in labels]
    
    if 5 in counts:
        return 7, labels[counts.index(5)]  # Five of a kind
    elif 4 in counts:
        return 6, labels[counts.index(4)]  # Four of a kind
    elif 3 in counts and 2 in counts:
        return 5, labels[counts.index(3)], labels[counts.index(2)]  # Full house
    elif 3 in counts:
        return 4, labels[counts.index(3)]  # Three of a kind
    elif counts.count(2) == 2:
        pairs = [labels[i] for i in range(len(counts)) if counts[i] == 2]
        return 3, max(pairs), min(pairs)  # Two pair
    elif counts.count(2) == 1:
        pair_label = labels[counts.index(2)]
        return 2, pair_label  # One pair
    else:
        return 1, labels[counts.index(1)]  # High card

def compare_hands(hand1, hand2):
    # Function to compare two hands based on their evaluation
    eval1 = evaluate_hand(hand1[0])
    eval2 = evaluate_hand(hand2[0])
    
    print(eval1, eval2)
    
    if eval1[0] > eval2[0]:
        return 1
    elif eval1[0] < eval2[0]:
        return -1
    else:
        # If hands are of the same type, compare card labels
        for i in range(len(eval1[1])):
            if eval1[1][i] > eval2[1][i]:
                return 1
            elif eval1[1][i] < eval2[1][i]:
                return -1
        return 0

def calculate_winnings(hands_bids):
    # Function to calculate total winnings based on hands and bids
    hands_bids.sort(key=cmp_to_key(compare_hands), reverse=False)  # Sort hands based on strength
    print(hands_bids)
    total_winnings = sum(bid * (i + 1) for i, (_, bid) in enumerate(hands_bids))
    return total_winnings

# Example input
hands_bids = [
    ("32T3K", 765),
    ("T55J5", 684),
    ("KK677", 28),
    ("KTJJT", 220),
    ("QQQJA", 483),
]

# Calculate and print the total winnings
total_winnings = calculate_winnings(hands_bids)
print("Total Winnings:", total_winnings)
