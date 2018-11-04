import timeit


def number_of_paths(stair_count, steps, recur=None):
    if recur is None:
        recur = number_of_paths
    paths = 0
    for step in steps:
        if step > stair_count:
            pass  # Can't reach the top because we'll overshoot
        elif step == stair_count:
            paths += 1
        elif step < stair_count:
            paths += recur(stair_count - step, steps)
        else:
            assert False, "something very strange happened"
    return paths


def make_memoized():
    cache = {}

    def memoized(stair_count, steps):
        key = stair_count
        if key in cache:
            return cache[key]
        # print("cache miss", stair_count)
        result = number_of_paths(stair_count, steps, memoized)
        cache[key] = result
        # print(stair_count, cache)
        return result

    return memoized


def main():
    stair_count = 300
    steps = [1, 2, 3, 4, 5]

    memoized = make_memoized()

    def format_int(i):
        return "{:.2E}".format(i)

    result = memoized(stair_count, steps)
    print(format_int(result))
    # print(number_of_paths(stair_count, steps))


main()

