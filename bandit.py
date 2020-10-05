import random


def explore(vending_machines):
    # explore randomly
    return random.choice(vending_machines)


def exploit(values):
    # greedy exploit
    return values.index(max(values))


def choose_vending_machine(epsilon, vending_machines, values):
    if random.random() > epsilon:
        return exploit(values)
    else:
        return explore(vending_machines)
