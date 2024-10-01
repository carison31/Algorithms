def change(money):
    cache = [float('inf')]*(money+1) 
    cache[0] = 0
    path = [[]]*(money+1)
    path[0] = [0]
    for m in range(1, money + 1):
        for c in [1, 3, 4]:
            if c <= m:
                if cache[m-c] + 1 < cache[m]:
                    path[m] = path[m-c] + [c]
                    cache[m] = cache[m-c] + 1
                
    return cache[money], path[money][1:]
            


def main():
    money = int(input())
    amount, chain = change(money)
    print(f'Минимальное количество монет, которыми можно разменять монету номиналом: {money} = {amount}\n({" + ".join(str(num) for num in chain)} = {money})')



if __name__ == "__main__":
    main()