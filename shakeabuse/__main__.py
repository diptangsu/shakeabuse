from .make_abuse import generate_random_abuse


def abuse() -> str:
    random_abuse = generate_random_abuse()
    print(random_abuse)
    return 0


if __name__ == '__main__':
    print(abuse())

