import yaml

from dataclasses import dataclass


@dataclass
class Component:
    name: str
    image: str

    throughput: int
    latency: float
    cost: float

    colour: str = '#000000'

    def __str__(self):
        return f'{self.name}'


def main():
    with open('components.yml', 'r') as f:
        components: [dict] = yaml.safe_load(f)

    component: dict
    for component in components:
        c = Component(**component)
        print(c)


if __name__ == '__main__':
    main()
