from aocd import data, submit
from collections import deque

DISK_MAP = [int(char) for char in data]
TEST_MAP = [int(char) for char in "2333133121414131402"]


def pop_move_back_candidate_index(
    move_back_candidate_indices_by_size: dict[int, list[int]],
    size_to_fill: int,
    minimum_index: int,
):
    _, bucket_with_latest_fitting_candidate = max(
        move_back_candidate_indices_by_size.items(),
        key=lambda item: (item[1][-1] if item[1] and item[0] <= size_to_fill else -1),
    )
    try:
        index = bucket_with_latest_fitting_candidate.pop()
        if index < minimum_index:
            return None
        return index
    except IndexError:
        return None


def compute_checksum(disk: list[int]):
    offset = 0
    res = 0

    move_back_candidate_indices_by_size = {
        block_size: [] for block_size in range(1, 10)
    }

    for index, size_of_block_moved_back in enumerate(disk):
        if index % 2 == 0:
            move_back_candidate_indices_by_size[size_of_block_moved_back].append(index)

    files_scored = set()

    for index, current_block_size in enumerate(disk):
        block_contains_file = index % 2 == 0
        if block_contains_file:
            file_id = index // 2
            if file_id not in files_scored:
                res += sum(
                    file_id * address
                    for address in range(offset, offset + current_block_size)
                )
            files_scored.add(file_id)
            offset += current_block_size
        else:
            left_to_fill = current_block_size
            while left_to_fill:
                block_to_move_back_index = pop_move_back_candidate_index(
                    move_back_candidate_indices_by_size, left_to_fill, index
                )
                if block_to_move_back_index is None:
                    break
                size_of_block_moved_back = disk[block_to_move_back_index]
                file_id = block_to_move_back_index // 2
                if file_id not in files_scored:
                    res += sum(
                        file_id * address
                        for address in range(offset, offset + size_of_block_moved_back)
                    )
                files_scored.add(file_id)
                offset += size_of_block_moved_back
                left_to_fill -= size_of_block_moved_back
            offset += left_to_fill
    return res


assert compute_checksum(TEST_MAP) == 2858

res = compute_checksum(DISK_MAP)
print(res)

input("enter to submit")

submit(res)
