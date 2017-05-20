import numpy as np
import matplotlib as plt

day_labels = []
counts = []

file = open("ufo_hist.csv")
for line in file:
    fields = line.rstrip("\n").split("\t", 1)
    days, count = fields
    day_labels.append(int(days))
    counts.append(int(count))

plt.title("UFO Reporting Delays")
plt.bar(day_labels, counts)
plt.savefig("UFO_Reporting_Delays.png")