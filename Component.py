from dataclasses import dataclass
from caseconverter import snakecase


@dataclass
class Component:
    name: str
    image: str
    level: int

    throughput: int
    latency: int
    cost: int

    colour: str = '#000000'
    api_name: str = ''

    def __post_init__(self):
        self.api_name = snakecase(self.name)

    def __str__(self):
        return f'{self.name} - level {self.level}'
