import sys, re

current_days = None
current_count = 0
days = None

for line in sys.stdin:
    days, count = line.rstrip("\n").split("\t", 1)
    try:
        count = int(count)
    except:
        sys.stderr.write("Can't convert '{}' to \n".format(count))
        continue

    if current_days == days:
        current_count += count
    else:
        if current_days:
            print("{}\t{}".format(current_days, current_count))
            current_count = count
            current_days = days

    if current_days == days:
        print("{}\t{}".format(current_days, current_count))