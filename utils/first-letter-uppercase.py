import fileinput

for line in fileinput.input():
    print("  %s  "%' '.join([s.capitalize() for s in line.split()]))