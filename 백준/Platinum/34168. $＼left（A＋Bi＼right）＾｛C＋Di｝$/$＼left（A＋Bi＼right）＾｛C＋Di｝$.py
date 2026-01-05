import sys

MOD = 998244353

def compute_case(A: int, B: int, M: int) -> int:
    if A == 0 and B == 0:
        return M % MOD

    if B == 0:
        if A == 1:
            term = (2 * M + 1) % MOD
            return (term * term) % MOD
        else:
            return (2 * M + 1) % MOD

    if A == 0:
        if B == 1:
            count_C = (2 * (M // 2) + 1) % MOD
            count_D = (2 * M + 1) % MOD
            return (count_C * count_D) % MOD
        else:
            return (2 * (M // 2) + 1) % MOD

    if A == B:
        return (2 * (M // 4) + 1) % MOD

    return 1

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    nums = list(map(int, data))

    if (len(nums) % 3) == 1:
        T = nums[0]
        ptr = 1
    elif (len(nums) % 3) == 0:
        T = len(nums) // 3
        ptr = 0
    else:
        T = 0
        ptr = 0

    out_lines = []
    for _ in range(T):
        A, B, M = nums[ptr], nums[ptr + 1], nums[ptr + 2]
        ptr += 3
        out_lines.append(str(compute_case(A, B, M)))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()