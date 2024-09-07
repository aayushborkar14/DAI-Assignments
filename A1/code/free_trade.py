import matplotlib.pyplot as plt

placelist = []
probablitylist = []
maxplace, maxprobablity = 0, 0

plt.figure(dpi=600)
for x in range(1, 100):
    probablity = 1
    for i in range(x - 1):
        probablity *= (200 - i) / 200
    probablity *= (x - 1) / 200
    placelist.append(x)
    probablitylist.append(probablity)
    if probablity > maxprobablity:
        maxprobablity = probablity
        maxplace = x
    print(f"{x} th place: {probablity}")

plt.scatter(placelist, probablitylist)
plt.axvline(maxplace)
plt.xticks([maxplace])
plt.axhline(maxprobablity)
plt.yticks([maxprobablity])
plt.xlabel("Place ")
plt.ylabel("Probablity of getting the free trade")
print(f"Max value is {maxprobablity} for place = {maxplace}")

plt.savefig("./Q5 Graph Plot.png", bbox_inches="tight")

