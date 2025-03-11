for i in range(2):
    cell = 1
    for j in range(1, 8):
       print("{0:b}".format(cell + cell * 2).zfill(8)," %3d" % (cell + cell * 2),"   %2d" % (abs((j % 2) * 2) - 1),"   Cell",j,)
       cell *= 2
