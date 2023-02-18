def tower_builder(n_floors):
    return [ ("*" * (1 + 2*i)).center(2*n_floors - 1) for i in range(n_floors) ]
