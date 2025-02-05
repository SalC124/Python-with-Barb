def fun(**kwargs):
    my_dict = {"skib": 0, "i": 0, "di": 0}

    for index, value in kwargs.items():
        print(index)
        my_dict[index] = value

    if kwargs.get("i") is not None:
        my_dict["di"] = my_dict["i"] + my_dict["di"]
    return my_dict


print(fun(skib=10, di=5))

print(fun(i=1, di=2))
