

from dataclasses import dataclass, field
import data


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

    def increment_din_code(self, code, increment):
        """Increment a code in the DIN codes list."""
        codes_list = ''.join(data.DIN_TAB.keys())
        return codes_list[codes_list.index(code) + increment]

    def get_din_set(self):
        """Return the DIN setting of the rider."""

        code_height = 'A'
        code_weight = 'A'
        for code, sizes in data.WEIGHT_DICT.items():
            if sizes[0] < self.weight < sizes[1]:
                code_weight = code
                break

        for code, sizes in data.HEIGHT_DICT.items():
            if sizes[0] < self.height < sizes[1]:
                code_height = code
                break

        code_din = max(code_height, code_weight)

        if self.age < 10 or self.age > 49.1:
            code_din = self.increment_din_code(code_din, -1)

        code_din = self.increment_din_code(code_din, self.level-2)

        for sole_lenght_sup in data.SOLE_LENGHT_TAB:
            if self.sole_length < sole_lenght_sup:
                sole_lenght_index = data.SOLE_LENGHT_TAB.index(sole_lenght_sup)
                break

        return data.DIN_TAB.get(code_din)[sole_lenght_index]


if __name__ == '__main__':
    rider = Rider()
    rider.din_set = rider.get_din_set()
    print(rider.din_set)
