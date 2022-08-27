from typing import Optional

class Folder:
    def __init__(self, dots, folds, max_x, max_y) -> None:
        self.dots = dots
        self.folds = folds
        self.max_x = max_x
        self.max_y = max_y
        
    def coord_transform(dot_index: int, length: int, fold_index: int) -> Optional[int]:
        if dot_index == fold_index:
            return None
        
        pre_fold_length = fold_index
        post_fold_length = length - 1 - fold_index
        offset = post_fold_length - pre_fold_length

        if dot_index < fold_index:
            return dot_index + max(0, offset)
        else:
            return fold_index - (dot_index - fold_index)

    def do_fold(self, fold_index, fold_is_x=True):
        new_dots = set()
        if fold_is_x:
            length = self.max_x + 1
            self.max_x = 0
            for x, y in self.dots:
                x = Folder.coord_transform(x, length, fold_index)
                if x is None:
                    raise Exception(f"Tried to fold on dot at {fold_index}, {y}")
                if x > self.max_x:
                    self.max_x = x
                new_dots.add((x, y))    
        else:
            length = self.max_y + 1
            self.max_y = 0
            for x, y in self.dots:
                y = Folder.coord_transform(y, length, fold_index)
                if y is None:
                    raise Exception(f"Tried to fold on dot at {x}, {fold_index}")
                if y > self.max_y:
                    self.max_y = y
                new_dots.add((x, y))
        self.dots = new_dots

    def solve_1(self):
        index, fold_direction = self.folds.pop(0)
        self.do_fold(index, fold_is_x=fold_direction=='x')
        print(len(self.dots))

    def solve_rest(self):
        while self.folds:
            index, fold_direction = self.folds.pop(0)
            self.do_fold(index, fold_is_x=fold_direction=='x')
        print(self)

    def __str__(self) -> str:
        res = []
        for y in range(self.max_y + 1):
            res.append("".join(['#' if (x, y) in self.dots else '.' for x in range(self.max_x + 1)]))
        return "\n".join(res)

dots = set()
folds = []
max_x = 0
max_y = 0
with open("day 13/input.txt", 'r') as infile:
    for line in infile:
        if line[0].isnumeric():
            x, y = map(int, line.strip().split(','))
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
            dots.add((x, y))
        elif line.startswith("fold"):
            fold_direction, index = line.strip().split()[2].split('=', 1)
            folds.append((int(index), fold_direction))

folder = Folder(dots, folds, max_x, max_y)
folder.solve_1()
folder.solve_rest()