from algorithms import randomString, middleUnderscore


def generateName(algorithm, length, casing):
    return {"random": randomString, "middleUnderscore": middleUnderscore}[algorithm](
        length, casing
    )
