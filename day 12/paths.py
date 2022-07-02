from __future__ import annotations
from typing import Set

class Cave():
    def __init__(self) -> None:
        self.nodes = dict()

    def __getitem__(self, cave_node: str):
        if cave_node not in self.nodes:
            raise KeyError(cave_node)
        return self.nodes[cave_node]

    def __setitem__(self, name: str, value: CaveNode):
        self.nodes[name] = value

    def __contains__(self, cave_node: str):
        return cave_node in self.nodes

    def add_connection(self, node1: str, node2: str):
        if node1 not in self:
            self.add_node(node1)
        if node2 not in self:
            self.add_node(node2)
        self[node1].connect(self[node2])
    
    def add_node(self, name: str):
        self[name] = CaveNode(name, node1.isupper())

    def __iter__(self):
        return self.nodes.__iter__()

    def items(self):
        return self.nodes.items()

class CaveNode():
    def __init__(self, name: str, revisitable: bool, connected_nodes: Set[bool]=None) -> None:
        self.name = name
        self.revisitable = revisitable
        self.connected_nodes = connected_nodes if connected_nodes else set()
        self.visit_count = 0

    def __hash__(self):
        return self.name.__hash__()
    
    def __eq__(self, other: CaveNode):
        return self.name == other.name

    def is_connected_to(self, other:CaveNode):
        return other.name in self.connected_nodes

    def connect(self, other: CaveNode):
        self.connected_nodes.add(other)
        other.connected_nodes.add(self)

    def is_revisitable(self):
        return self.revisitable

    def can_be_visited(self):
        return self.revisitable or self.visit_count < 1
    
    def __str__(self) -> str:
        return self.name


cave = Cave()
with open("day 12/input.txt", 'r') as infile:
    for line in infile.readlines():
        node1, node2 = line.strip().split('-')
        if not node1 in cave:
            cave.add_node(node1)
        if not node2 in cave:
            cave.add_node(node2)
        
        cave[node1].connect(cave[node2])

