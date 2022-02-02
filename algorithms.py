import random
import string

sets = {
    "alphanumeric": string.ascii_letters + string.digits,
    "letters": string.ascii_lowercase,
}

# various name generators


def randomString(length, charSet="alphanumeric"):
    return "".join(random.choice(sets[charSet]) for i in range(length))


# one of middle chars are an underscore. ex. 1_33 93_3 12_6 Ab_3


def middleUnderscore(length, charSet):
    lenOne = random.randint(1, length - 2)
    return (
        randomString(1 if lenOne < 1 else lenOne, charSet)
        + "_"
        + randomString(length - lenOne - 1, charSet)
    )
