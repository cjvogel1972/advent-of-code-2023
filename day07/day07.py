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
        self.card_order = card_order
        counts = self.count_cards()

        self.hand_type = self.determine_hand_type_from_counts(counts)

    def count_cards(self) -> list[int]:
        card_count = self.map_cards_to_counts()

        return list(card_count.values())

    def map_cards_to_counts(self) -> dict[str, int]:
        card_count = {}
        for c in self.cards:
            card_count[c] = card_count.get(c, 0) + 1

        return card_count

    @staticmethod
    def determine_hand_type_from_counts(counts: list[int]) -> int:
        if counts.count(5) == 1:
            hand_type = FIVE_KIND
        elif counts.count(4) == 1:
            hand_type = FOUR_KIND
        elif counts.count(3) == 1 and counts.count(2) == 1:
            hand_type = FULL_HOUSE
        elif counts.count(3) == 1:
            hand_type = THREE_KIND
        elif counts.count(2) == 2:
            hand_type = TWO_PAIR
        elif counts.count(2) == 1:
            hand_type = ONE_PAIR
        else:
            hand_type = HIGH_CARD

        return hand_type

    def __lt__(self, other):
        if self.hand_type < other.hand_type:
            return True
        elif self.hand_type > other.hand_type:
            return False

        for i, c in enumerate(self.cards):
            oc = other.cards[i]
            if c == oc:
                continue
            if self.card_order.index(c) < self.card_order.index(oc):
                return True
            else:
                return False

        return False

    def __str__(self):
        return f"cards: {self.cards} bid: {self.bid} hand type: {self.hand_type}"

    def __repr__(self):
        return f"cards: {self.cards} bid: {self.bid} hand type: {self.hand_type}"


class JokerHand(Hand):
    def __init__(self, line: str):
        Hand.__init__(self, line)
        self.card_order = joker_card_order

    def count_cards(self) -> list[int]:
        card_count = self.map_cards_to_counts()

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

        return list(card_count.values())


if __name__ == '__main__':
    input_lines = readfile("day07/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
