import sys


def grow():
    grow_per_day = 1.1
    day = 1
    result = int(sys.argv[1])
    last_result = int(sys.argv[2])
    while result < last_result:
        result *= grow_per_day
        day += 1
    else:
        print(day)


if __name__ == "__main__":
    grow()
