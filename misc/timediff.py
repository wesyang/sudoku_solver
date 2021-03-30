import datetime
from typing import List


def isLeapYear(year: int) -> bool:
    return (year % 4) == 0;


def getDaysInMonth(year: int, month: int) -> int:
    if month in set([1, 3, 5, 7, 8, 10, 12]):
        return 31
    elif month in set([4, 6, 9, 11]):
        return 30
    return 29 if isLeapYear(year) else 28


def getDaysInYear(year: int) -> int:
    return 366 if isLeapYear(year) else 365


def timeDifference(s: List[int], e: List[int]) -> int:
    if s[0] == e[0] and s[1] == e[1]:
        return e[2] - s[2]

    total: int = getDaysInMonth(s[0], s[1]) - s[2]

    for i in range((e[1] if s[0] == e[0] else 13) - (s[1] + 1)):
        total += getDaysInMonth(s[0], s[1] + i + 1)
    if e[0] > s[0]:
        for i in range(e[0] - s[0] - 1):
            total += getDaysInYear(s[0] + i + 1)
        for i in range(e[1] - 1):
            total += getDaysInMonth(e[0], i + 1)

    total += e[2]

    return total


if __name__ == "__main__":
    s: List[int] = [2010, 6, 3]
    e: List[int] = [2017, 12, 31]

    span: int = timeDifference(s, e)
    st = datetime.datetime(s[0], s[1], s[2])
    et = datetime.datetime(e[0], e[1], e[2])
    expected = int((et - st).days)
    print(f'span {span}, expected = {expected}')
