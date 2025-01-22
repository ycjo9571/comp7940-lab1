# EX 1

x = 52633
for i in range(1, x+1):
    if x % i == 0:
        print(i)

# EX 2


def print_factor(x):
    factors = []
    for i in range(1, x+1):
        if x % i == 0:
            factors.append(i)

    print(f'Factors of {x}: {factors}')


# EX 3
def find_factors_ofaList(list):
    for num in list:
        print_factor(num)


find_factors_ofaList([52633, 8137, 1024, 999])
