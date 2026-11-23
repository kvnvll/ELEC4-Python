
# P2 - Student Utilities Module

import statistics


def average(grades):
    return statistics.mean(grades)


def pass_fail(grades):
    if average(grades) >= 75:
        return "PASSED"
    else:
        return "FAILED"


def highest(grades):
    return max(grades)


def lowest(grades):
    return min(grades)
