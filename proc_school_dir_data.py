#! /usr/bin/python2
county2highschoolct = {}
with open("School_Directory_2016.csv", 'r') as sdirfile:
    for line in sdirfile:
        cmps = line.split(';')
        # Skip first line
        if cmps[0] == "Academic Year":
            continue
        county_name = cmps[2]
        if county_name not in county2highschoolct:
            county2highschoolct[county_name] = 0
        if "H" in cmps[5]:
            county2highschoolct[county_name] += 1
counties = sorted(county2highschoolct.keys())
for c in counties:
    print c, county2highschoolct[c]
