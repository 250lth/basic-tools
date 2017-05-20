import sys, re, time, iso8601

word_finder = re.compile("([\w\s]+),\s(\w+)")

for line in sys.stdin:
    fields = line.rstrip("\n").split("\t", 2)
    try:
        sighted_at, reported_at, rest = fields
        sighted_dt = iso8601.parse_date(sighted_at)
        reported_dt = iso8601.parse_date(reported_at)
        diff = reported_dt - sighted_dt
    except:
        sys.stderr.write("Bad line: {}".format(line))
        continue

    print("\t".join((str(diff.days), "1")))