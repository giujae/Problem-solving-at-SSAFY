def tower_builder(n_floors):
    result = []
    for i in range(1, n_floors * 2, 2):
        stars = i * '*'
        result.append(stars.center((n_floors * 2) - 1))
    return result