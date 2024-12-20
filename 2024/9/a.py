from aocd import data, submit

DISK_MAP = [int(char) for char in data]
TEST_MAP = [int(char) for char in "2333133121414131402"]

def compute_checksum(disk: list[int]):
    offset = 0
    front_index = 0
    back_index = len(disk) - 1 if len(disk) % 2 == 1 else len(disk) - 2

    res = 0

    back_part_moved = 0
    while front_index < back_index:
        current_block_size = disk[front_index]
        if front_index % 2 == 0:
            res += sum(front_index // 2 * address for address in range(offset, offset + current_block_size))
            offset += current_block_size
        else:
            empty_space_filled = 0
            while empty_space_filled < current_block_size and front_index < back_index:
                filled_from_this_block = min(disk[back_index] - back_part_moved, current_block_size - empty_space_filled)
                empty_space_filled += filled_from_this_block
                back_part_moved += filled_from_this_block
                res += sum(back_index // 2 * address for address in range(offset, offset + filled_from_this_block))
                offset += filled_from_this_block

                if back_part_moved >= disk[back_index]:
                    back_part_moved = 0
                    back_index -= 2
        front_index += 1
    remaining_from_last_block = disk[back_index] - back_part_moved
    res += sum(back_index // 2 * address for address in range(offset, offset + remaining_from_last_block))

    return res

assert compute_checksum(TEST_MAP) == 1928

res = compute_checksum(DISK_MAP)
print(res)

input("enter to submit")

submit(res)