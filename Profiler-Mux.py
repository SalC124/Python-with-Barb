import math


def muxTime(cellCount):
    for i in range(2):
        cell = 1
        cellSlots = cellCount + 1
        decimalPlaces = math.ceil(math.log10(int("11" + "0" * (cellCount - 1), 2)))
        for i in range(1, cellSlots):
            mosfets = cell + cell * 2
            print(
                "{0:b}".format(mosfets).zfill(cellSlots),
                "   %{0}d".format(decimalPlaces) % (mosfets),
                "   %2d" % (abs((i % 2) * 2) - 1),
                "   Cell",
                i,
            )
            cell *= 2


print("\nprogram 1")
muxTime(7)
print("\nprogram 2")
muxTime(15)
