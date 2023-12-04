import os

def read_input_file(file_path):
    with open(file_path) as file:
        return file.read().strip()

def parse_input(data):
    lines = data.split('\n')
    return [[c for c in line] for line in lines], len(lines), len(lines[0])

def process_gears(G, R, C):
    p1 = 0
    nums = {}

    for r in range(R):
        gears = set()
        n = 0
        has_part = False

        for c in range(C + 1):
            if c < C and G[r][c].isdigit():
                n = n * 10 + int(G[r][c])
                for rr in [-1, 0, 1]:
                    for cc in [-1, 0, 1]:
                        if 0 <= r + rr < R and 0 <= c + cc < C:
                            ch = G[r + rr][c + cc]
                            if not ch.isdigit() and ch != '.':
                                has_part = True
                            if ch == '*':
                                gears.add((r + rr, c + cc))
            elif n > 0:
                for gear in gears:
                    if gear not in nums:
                        nums[gear] = []
                    nums[gear].append(n)
                if has_part:
                    p1 += n
                n = 0
                has_part = False
                gears = set()

    return p1, nums

def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    parent_dir = os.path.dirname(script_dir)
    relative_path = os.path.join('input', 'day3.txt')
    file_path = os.path.join(parent_dir, relative_path)

    data = read_input_file(file_path)
    G, R, C = parse_input(data)

    p1, nums = process_gears(G, R, C)
    print("Part 1:", p1)

    p2 = sum(v[0] * v[1] for v in nums.values() if len(v) == 2)
    print("Part 2:", p2)

if __name__ == "__main__":
    main()
