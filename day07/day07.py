from util.file import readfile

HIGH_CARD = 1
ONE_PAIR = 2
TWO_PAIR = 3
THREE_KIND = 4
FULL_HOUSE = 5
FOUR_KIND = 6
FIVE_KIND = 7

card_order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
joker_card_order = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']


def solve_part1(lines: list[str]) -> int:
    total = 0

    hands = [Hand(line) for line in lines]
    hands.sort()

    for i, hand in enumerate(hands):
        total += hand.bid * (i + 1)

    return total


def solve_part2(lines: list[str]) -> int:
    total = 0

    hands = [JokerHand(line) for line in lines]
    hands.sort()

    for i, hand in enumerate(hands):
        total += hand.bid * (i + 1)

    return total


class Hand:
    def __init__(self, line: str):
        puzzle_input = line.split()
        self.cards = puzzle_input[0]
        self.bid = int(puzzle_input[1])
        card_count = {}
        for c in self.cards:
            card_count[c] = card_count.get(c, 0) + 1
        counts = list(card_count.values())

        if counts.count(5) == 1:
            self.hand_type = FIVE_KIND
        elif counts.count(4) == 1:
            self.hand_type = FOUR_KIND
        elif counts.count(3) == 1 and counts.count(2) == 1:
            self.hand_type = FULL_HOUSE
        elif counts.count(3) == 1:
            self.hand_type = THREE_KIND
        elif counts.count(2) == 2:
            self.hand_type = TWO_PAIR
        elif counts.count(2) == 1:
            self.hand_type = ONE_PAIR
        else:
            self.hand_type = HIGH_CARD

    def __lt__(self, other):
        if self.hand_type < other.hand_type:
            return True
        elif self.hand_type > other.hand_type:
            return False

        for i, c in enumerate(self.cards):
            oc = other.cards[i]
            if c == oc:
                continue
            if card_order.index(c) < card_order.index(oc):
                return True
            else:
                return False

        return False

    def __str__(self):
        return f"cards: {self.cards} bid: {self.bid} hand type: {self.hand_type}"

    def __repr__(self):
        return f"cards: {self.cards} bid: {self.bid} hand type: {self.hand_type}"


class JokerHand:
    def __init__(self, line: str):
        puzzle_input = line.split()
        self.cards = puzzle_input[0]
        self.bid = int(puzzle_input[1])
        card_count = {}
        for c in self.cards:
            card_count[c] = card_count.get(c, 0) + 1

        joker_count = card_count.get('J', 0)
        if joker_count > 0 and joker_count != 5:
            card_count.pop('J')

            max_count = 0
            max_card = ''
            for c in card_count:
                if card_count[c] > max_count:
                    max_card = c
                    max_count = card_count[c]
            card_count[max_card] = card_count[max_card] + joker_count

        counts = list(card_count.values())

        if counts.count(5) == 1:
            self.hand_type = FIVE_KIND
        elif counts.count(4) == 1:
            self.hand_type = FOUR_KIND
        elif counts.count(3) == 1 and counts.count(2) == 1:
            self.hand_type = FULL_HOUSE
        elif counts.count(3) == 1:
            self.hand_type = THREE_KIND
        elif counts.count(2) == 2:
            self.hand_type = TWO_PAIR
        elif counts.count(2) == 1:
            self.hand_type = ONE_PAIR
        else:
            self.hand_type = HIGH_CARD

    def __lt__(self, other):
        if self.hand_type < other.hand_type:
            return True
        elif self.hand_type > other.hand_type:
            return False

        for i, c in enumerate(self.cards):
            oc = other.cards[i]
            if c == oc:
                continue
            if joker_card_order.index(c) < joker_card_order.index(oc):
                return True
            else:
                return False

        return False

    def __str__(self):
        return f"cards: {self.cards} bid: {self.bid} hand type: {self.hand_type}"

    def __repr__(self):
        return f"cards: {self.cards} bid: {self.bid} hand type: {self.hand_type}"


if __name__ == '__main__':
    input_lines = readfile("day07/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
