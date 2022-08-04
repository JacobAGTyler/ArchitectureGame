from dataclasses import dataclass


@dataclass
class ChanceCard:
    title: str
    impact: str
    text: str
    coded: dict

