romano = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 1000, 'm': 10000}

def convertromdec(num):
    if len(num) == 1:
        return romano[num]
    else:
        if romano[num[0]] >= romano[num[1]]:
            return romano[num[0]] + convertromdec(num[1:])
        else:
            return - romano[num[0]] + convertromdec(num[1:])