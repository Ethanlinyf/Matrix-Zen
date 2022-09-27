def create_a_random_list(n):
    import random

    arr = []

    for i in range(n):
        arr.append(random.randint(1, 100))

    return arr
