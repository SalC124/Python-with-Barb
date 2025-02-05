# "SalCali" in decimal form
asciiName = "83,97,108,67,97,108,105"


# program 1
print("\nprogram 1\n")
for i in range(0, len(asciiName)):
    print(asciiName[i])


# program 2
print("\nprogram 2\n")
for i in range(0, len(asciiName)):
    if asciiName[i] == ",":
        print("comma")
    else:
        print(asciiName[i])


# program 3 & 4
print("\nprogram 3\n")
snippet = ""
total = 0
for i in range(0, len(asciiName)):
    if asciiName[i] == ",":
        print(snippet)
        total += int(snippet)
        snippet = ""
    else:
        snippet += asciiName[i]


# program 4
print("\nprogram 4\n")
print(total)


# program 5
print("\nprogram 5\n")


def delimitStr(data: str, delimiter: str):
    snippet = ""
    total = 0
    for i in range(0, len(data)):
        if data[i] == delimiter:
            print(snippet)
            total += int(snippet)
            snippet = ""
        else:
            snippet += data[i]

    return total


print("total:", delimitStr(asciiName, ","))
