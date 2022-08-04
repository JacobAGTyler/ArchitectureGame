from dataclasses import dataclass
from caseconverter import snakecase


@dataclass
class Component:
    name: str
    image: str
    level: int

    throughput: int
    latency: int

    base: int
    cost: int

    min_latency: int = 10
    colour: str = '#000000'
    api_name: str = ''

    def __post_init__(self):
        self.api_name = snakecase(self.name)

        self.throughput = self.level * self.throughput
        self.latency = max(round(self.latency / self.level), self.min_latency)

        self.price = self.base + (self.cost * self.level)

        if type(self.colour) == str and '#' not in self.colour:
            self.colour = f'#{self.colour}'

    def __str__(self):
        return f'{self.name} - level {self.level} [L: {self.latency}ms T: {self.throughput}m/s P: ${self.price}]'
