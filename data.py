"""data.py

"""

from dataclasses import dataclass, field

DIN_TAB = {
    'A': [0.75, 0.75, 0.00, 0.00, 0.00, 0.00],
    'B': [1.00, 1.00, 0.75, 0.00, 0.00, 0.00],
    'C': [1.25, 1.25, 1.00, 0.00, 0.00, 0.00],
    'D': [1.75, 1.50, 1.50, 0.00, 0.00, 0.00],
    'E': [2.00, 2.00, 1.75, 0.00, 0.00, 0.00],
    'F': [2.50, 2.50, 2.25, 2.00, 1.75, 1.75],
    'G': [0.00, 3.00, 2.50, 2.50, 2.25, 2.00],
    'H': [0.00, 3.50, 3.00, 3.00, 2.50, 2.50],
    'I': [0.00, 4.25, 4.00, 3.50, 3.25, 3.25],
    'J': [0.00, 5.00, 4.75, 4.50, 4.00, 4.00],
    'K': [0.00, 6.00, 5.50, 5.25, 5.00, 4.75],
    'L': [0.00, 7.00, 6.75, 6.25, 6.00, 5.75],
    'M': [0.00, 8.50, 8.00, 7.50, 7.00, 6.75],
    'N': [0.00, 10.0, 9.50, 9.00, 8.50, 8.25],
    '0': [0.00, 12.0, 11.0, 10.0, 10.0, 10.0],
    'P': [0.00, 12.0, 11.0, 10.0, 10.0, 10.0],
    'Q': [0.00, 12.0, 11.0, 10.0, 10.0, 10.0],
}

SOLE_LENGHT_TAB = [251, 270, 290, 310, 330, 500]

WEIGHT_DICT = {
    'A': (10.0, 13.0),
    'B': (13.1, 17.0),
    'C': (17.1, 21.0),
    'D': (21.1, 25.0),
    'E': (25.1, 30.0),
    'F': (30.1, 35.0),
    'G': (35.1, 41.0),
    'H': (41.1, 48.0),
    'I': (48.1, 57.0),
    'J': (57.1, 66.0),
    'K': (66.1, 78.0),
    'L': (78.1, 94.0),
    'M': (94.1, 2500)
}

HEIGHT_DICT = {
    'H': (00.00, 148.0),
    'I': (148.1, 157.0),
    'J': (157.1, 166.0),
    'K': (166.1, 178.0),
    'L': (178.1, 194.0),
    'M': (194.1, 250.0)
}

LEVELS = (
    (0, 'First timer'),
    (1, 'Beginner'),
    (2, 'Intermediate'),
    (3, 'Advanced'),
    (4, 'Expert'),
)


def increment_din_code(self, code, increment):
    """Increment a code in the DIN codes list."""
    codes_list = ''.join(DIN_TAB.keys())
    return codes_list[codes_list.index(code) + increment]


@dataclass
class Rider():
    """Represent a rider.

    keyword arguments are obvious.
    """
    name: str = "Rider"
    age: int = 30
    height: int = 175
    weight: int = 75
    level: int = 2
    sole_length: int = 300
    din_set: float = field(init=False)

    def __post_init__(self):
        self.din_set = self.get_din_set()

    def get_din_set(self):
        """Return the DIN setting of the rider."""

        code_height = 'A'
        code_weight = 'A'
        for code, sizes in WEIGHT_DICT.items():
            if sizes[0] < self.weight < sizes[1]:
                code_weight = code
                break

        for code, sizes in HEIGHT_DICT.items():
            if sizes[0] < self.height < sizes[1]:
                code_height = code
                break

        code_din = max(code_height, code_weight)

        if self.age < 10 or self.age > 49.1:
            code_din = increment_din_code(code_din, -1)

        code_din = ncrement_din_code(code_din, self.level-2)

        for sole_lenght_sup in SOLE_LENGHT_TAB:
            if self.sole_length < sole_lenght_sup:
                sole_lenght_index = SOLE_LENGHT_TAB.index(sole_lenght_sup)
                break

        return DIN_TAB.get(code_din)[sole_lenght_index]


if __name__ == '__main__':
    rider = Rider()
    rider.din_set = rider.get_din_set()
    print(rider.din_set)
