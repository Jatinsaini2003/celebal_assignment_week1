from itertools import groupby

if __name__ == "__main__":
    s = input().strip()
    parts = []
    for char, group in groupby(s):
        count = sum(1 for _ in group)
        parts.append(f"({count}, {char})")
    print(" ".join(parts))
