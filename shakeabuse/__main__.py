from .make_abuse import generate_random_abuse


def abuse() -> str:
    random_abuse = generate_random_abuse()
    return random_abuse


if __name__ == '__main__':
    print(abuse())

