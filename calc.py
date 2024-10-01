def calc_recursive(n):
    if n == 1:
        return 0
    
    minim = float("inf")
    result = 1 + min(calc_recursive(n-1), calc_recursive(n // 2) if n % 2 == 0 else float("inf"), calc_recursive(n // 3) if n % 3 == 0 else float("inf"))

    return result


def calc_dp(n):
    table = [float("inf")] * (n + 1)  #1 -> n
    table[1] = 0
    path = [[0]] * (n + 1)
    path[1] = [[]]
    
    for k in range(2, n + 1):
        table[k] = 1 + table[k-1]
        if k % 2 == 0:
            table[k] = 1 + min(table[k], table[k//2])
        if k % 3 == 0:
            table[k] = 1 + min(table[k], table[k//3])

    last = n
    chain_stack = []
    while n > 1:
        chain_stack.append(n)
        if table[n] == 1 + table[n-1]:
            n -= 1
        elif n % 2 == 0 and table[n] == 1 + table[n//2]:
            n //= 2
        elif n % 3 == 0 and table[n] == 1 + table[n//3]:
            n //= 3
    chain_stack.append(1)

    return table[last], chain_stack

def main():
    n = int(input())
    amount, chain = calc_dp(n)
    print(f'Минимальное количество операций для того, чтобы из 1 получить n посредством операций *2, *3, +1: {amount}\n({", ".join(str(chain[num]) for num in range(len(chain) - 1, -1, -1))})')

if __name__ == "__main__":
    main()