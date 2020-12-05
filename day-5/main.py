def get_sample_input() -> str:
    return """FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL"""


def get_real_input() -> str:
    with open('input.txt', 'r') as f:
        return f.read()


def get_boarding_passes(batch: str) -> list[str]:
    return batch.splitlines()


def decode_boarding_pass(boarding_pass: str) -> (int, int):
    class Node:
        def __init__(self, data):
            self.left = None
            self.right = None
            self.data = data

        def traverse(self, pattern: str):
            if self.data:
                node = self
                for character in pattern:
                    if character == 'F' or character == 'L':
                        node = node.left or node
                    elif character == 'B' or character == 'R':
                        node = node.right or Node(node.data + 1)
                return node.data

    def generate_tree(values):
        if len(values) == 0:
            return None

        middle = len(values) // 2
        tree_node = Node(values[middle])
        tree_node.left = generate_tree(values[:middle])
        tree_node.right = generate_tree(values[middle + 1:])
        return tree_node

    row_values = list(range(0, 127))
    rows = generate_tree(row_values)
    column_values = list(range(0, 7))
    columns = generate_tree(column_values)

    pass_rows = boarding_pass[:7]
    row = rows.traverse(pass_rows)
    pass_columns = boarding_pass[7:]
    column = columns.traverse(pass_columns)

    return row, column


def get_decoded_boarding_passes(encoded_boarding_passes):
    return list(
        map(lambda boarding_pass: decode_boarding_pass(boarding_pass), encoded_boarding_passes)
    )


def get_seat_ids(boarding_passes):
    return list(map(lambda boarding_pass: get_seat_id(boarding_pass[0], boarding_pass[1]), boarding_passes))


def get_max_seat_id(boarding_passes):
    return max(get_seat_ids(boarding_passes))


def get_seat_id(row, column) -> int:
    return row * 8 + column


if __name__ == '__main__':
    sample_input = get_sample_input()
    sample_boarding_passes = get_boarding_passes(sample_input)
    decoded_boarding_passes = get_decoded_boarding_passes(sample_boarding_passes)
    sample_result = get_max_seat_id(decoded_boarding_passes)
    print(f'Sample Result: {sample_result}')

    real_input = get_real_input()
    real_boarding_passes = get_boarding_passes(real_input)
    decoded_boarding_passes = get_decoded_boarding_passes(real_boarding_passes)
    part_one_result = get_max_seat_id(decoded_boarding_passes)
    print(f'Part One Result: {part_one_result}')

    all_seat_ids = sorted(get_seat_ids(decoded_boarding_passes))
    for idx in range(1, len(all_seat_ids) - 1):
        if all_seat_ids[idx + 1] - all_seat_ids[idx] > 1:
            print(f'Part Two Result: {all_seat_ids[idx] + 1}')
