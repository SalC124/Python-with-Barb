for i in range(2):
    cell = 1
    cellSlots = 8
    for i in range(1, cellSlots):
        mosfets = cell + cell * 2
        print("{0:b}".format(mosfets).zfill(cellSlots)," %3d" % (mosfets),"   %2d" % (abs((i % 2) * 2) - 1),"   Cell",i)
        cell *= 2
