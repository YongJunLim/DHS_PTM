def manipulate(string):
    array = string.split(",")
    new = []
    for i in range(len(array)):
        if array[i] in new:
            pass
        elif array[i].isdigit():
            new.append(array[i])
        else:
            new.append(array[i])
    S_array = []
    temp = [new[0]]
    for i in range(1, len(new)):
        if new[i].isdigit():
            temp.append(int(new[i]))
        else:
            S_array.append(temp)
            temp = [new[i]]
    S_array.append(temp)
    return S_array
