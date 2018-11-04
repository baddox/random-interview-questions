"""
From https://www.youtube.com/watch?v=5o-kdjv7FD0&t=151s
"""

import timeit


def number_of_paths(stair_count, steps, recur=None):
    if recur is None:
        recur = number_of_paths
    paths = 0
    for step_count in steps:
        if step_count > stair_count:
            # We can't reach the top because we'll overshoot
            pass
        elif step_count == stair_count:
            # We reach the top in 1 step!
            paths += 1
        elif step_count < stair_count:
            # We climb up the stairs, then add the number of paths from our new
            # location.
            paths += recur(stair_count - step_count, steps)
        else:
            assert False, "something very strange happened"
    return paths


def make_memoized():
    cache = {}

    def memoized(stair_count, steps):
        key = stair_count
        if key in cache:
            return cache[key]
        result = number_of_paths(stair_count, steps, memoized)
        cache[key] = result
        return result

    return memoized


def linear(stair_count, steps):
    memoized = make_memoized()
    result = None
    for i in range(stair_count + 1):
        result = memoized(i, steps)
    return result


def main():
    stair_count = 200
    steps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    memoized = make_memoized()

    def format_int(i):
        return "{:.2E}".format(i)

    # The simple memoized version will stack overflow at around 500 stairs.
    result = memoized(stair_count, steps)
    print(format_int(result))

    # The linear version uses the memoized version and just pre-caches from
    # 0 to `stair_count`, so the stack never grows.
    result = linear(stair_count, steps)
    print(format_int(result))


main()

