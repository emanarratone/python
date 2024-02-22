cities = [(19542209, "New York"), (4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]
srt_cities = sorted(cities, key=(lambda n: n[1][-1]), reverse=True)
print(srt_cities)
