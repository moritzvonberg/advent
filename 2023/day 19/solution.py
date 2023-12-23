from aocd import get_data, submit
from dataclasses import dataclass
from typing import NamedTuple, Callable, Sequence
import re

data = get_data(day=19, year=2023)

workflows, parts = data.split("\n\n")

workflows = workflows.splitlines()

result = 0

params = 'xmas'

class Part(NamedTuple):
    x: int
    m: int
    a: int
    s: int

    def rating_number(self):
        return self.x + self.m + self.a + self.s

class Rule(NamedTuple):
    param: str | None
    symbol: str | None
    threshold: int | None
    dest: str

    @classmethod
    def create_rules(cls, repr: str):
        rules = repr.split(',')

    @classmethod
    def from_string(cls, repr: str):
        match = re.match(
            r"(?:(?P<param>[xmas])(?P<symbol>[<>])(?P<threshold>\d+):)?(?P<dest>\w+)",
            repr
            )
        



@dataclass
class Workflow:
    name: str
    rules: list[Rule]

    @classmethod
    def from_str(cls, repr: str):
        match = re.match(r"([a-z]+)\{(.+)\}")
        return Workflow(match[1], Rule.create_rules(match[2])) 


if result:
    submit(result)
