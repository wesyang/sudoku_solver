p1_meetings = [
    (1230, 1300),
    (845, 900),
    (1300, 1500),
]

p2_meetings = [
    (0, 844),
    (930, 1200),
    (1515, 1546),
    (1600, 2400),
]

p3_meetings = [
    (845, 915),
    (1515, 1545),
    (1235, 1245),
]

p4_meetings = [
    (1, 5),
    (844, 900),
    (1515, 1600)
]

schedules1 = [p1_meetings, p2_meetings, p3_meetings]
schedules2 = [p1_meetings, p3_meetings]
schedules3 = [p2_meetings, p4_meetings]

print(schedules1)


def inBetween(range, point):
    return range[0] <= point <= range[1]


def canMergeHelper(last, item):
    return inBetween(last, item[0]) or inBetween(last, item[1])


def canMerge(last, item):
    if not last: return False;
    return canMergeHelper(last, item) or canMergeHelper(item, last)


def mergeTwo(last, item):
    start = last[0] if last[0] < item[0] else item[0]
    end = last[1] if last[1] > item[1] else item[1]
    return start, end;


def mergeList(items):
    merged = []
    for item in items:
        lastItem = None if not merged else merged[-1]
        if not canMerge(lastItem, item):
            merged.append(item)
        else:
            print(f'***** merge item {lastItem}, with {item}')
            newItem = mergeTwo(lastItem, item);
            print(f'***** new item {newItem}')
            merged = merged[:-1]
            merged.append(newItem);

    return merged;


def buildAvaliable(items):
    start = 0;
    endDay = 2400;
    avalible = []
    for item in items:
        if start < item[0]:
            avalible.append((start, item[0]))
        start = item[1]

    if start < endDay:
        avalible.append((start, endDay))

    return avalible;


def process(schedules):
    flat = [m for meetings in schedules for m in meetings];
    print(flat);
    sort = sorted(flat, key=lambda item: item[0]);
    print(sort);
    merged = mergeList(sort);
    print(merged);
    openSlots = buildAvaliable(merged);
    print('-------------------------------------------------------------');
    print(f'\t++++ final ++++ : {openSlots}');
    print('-------------------------------------------------------------');


process(schedules1)
process(schedules2)
process(schedules3)