from aocd import get_data, submit
from collections import defaultdict

data = get_data(day=7, year=2022).splitlines(keepends=False)

directory_lookup = dict()

folders_we_are_inside = []
dir_size_map = defaultdict(int)

for output in data:
    match output.split(" "):
        case ["$", "ls"]:
            continue
        case ["dir", dir_name]:
            continue
        case ["$", "cd", ".."]:
            folders_we_are_inside.pop()
        case ["$", "cd", target_dir_name]:
            folders_we_are_inside.append(target_dir_name)
        case [file_size, file_name]:
            for i in range(len(folders_we_are_inside)):
                dir_size_map['/'.join(folders_we_are_inside[:i + 1])] += int(file_size)

answer = 0

for dir_name, dir_size in dir_size_map.items():
    if dir_size <= 100_000:
        print(f"{dir_name}: size {dir_size}")
        answer += dir_size

print(answer)
input("press anything to submit")
submit(answer=answer, part="a", year=2022, day=7)

used_space = dir_size_map["/"]
total_space = 70_000_000
required_space = 30_000_000
remaining_space = total_space - used_space
needed_space = required_space - remaining_space

answer2 = None
for dir_name, dir_size in dir_size_map.items():
    if dir_size >= needed_space:
        if answer2 is None or answer2 > dir_size:
            print(f"new candidate {dir_name}: {dir_size}")
            answer2 = dir_size

input("press anything to submit part b")
submit(answer=answer2, part="b", year=2022, day=7)
