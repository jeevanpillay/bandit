import bandit


if __name__ == '__main__':
    vending_machines = [0, 1, 2, 3]
    values = [0, 0, 0, 0]
    e = 0.5

    for _ in range(100):
        print(bandit.choose_vending_machine(e, vending_machines, values))


