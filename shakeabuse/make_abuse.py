from .abuses import *
import random


def generate_random_abuse():
    one = random.choice(ONE)
    two = random.choice(TWO)
    three = random.choice(THREE)

    abuse = f'Thou {one} {two} {three}!'
    return abuse
