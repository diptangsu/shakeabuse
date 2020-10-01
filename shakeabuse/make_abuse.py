import random
from insults_parts import *
from insults_full import *


def generate_random_abuse():
    abuse = ' '.join(random.choice(x) for x in (FIRST_ADJECTIVES, SECOND_ADJECTIVES, NOUNS))
    constructed_abuse = 'Thou ' + abuse
    
    abuse_full = random.choice(FULL_INSULTS)
    
    return random.choice((constructed_abuse, abuse_full))

