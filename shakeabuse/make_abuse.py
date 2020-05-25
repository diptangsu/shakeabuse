from .abuses import *
import random


def generate_random_abuse():
    one = random.choice(ONE)
    two = random.choice(TWO)
    three = random.choice(THREE)
    abuse_parts = f'Thou {one} {two} {three}!'
    
    abuse_full = random.choice(FULL_INSULTS)
    
    return random.choice((abuse_parts, abuse_full))

