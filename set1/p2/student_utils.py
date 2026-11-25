
# Name: VILA, KEVIN V.
# Section: IV-BSIT C
# Activity: P2 - Custom Module
# Date: November 2026


def average(grades):
    return sum(grades) / len(grades)


def highest(grades):
    return max(grades)


def lowest(grades):
    return min(grades)


def pass_fail(grades):
    if average(grades) >= 75:
        return "PASSED"
    else:
        return "FAILED"
