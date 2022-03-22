
def  areatriagulo(a=0,b=0,c=0):
    p = (a+b+c)/2
    area = (p*(p-a)*(p-b)*(p-c))**1/2
    return area

def end(areax,areay):
    if (areax > areay):
        print(f"O triãgulo com maior área é [Tx] = [{areax}]")
    elif (areay > areax):
        print(f"O triânguelo com maior área é [Ty] = [{areay}]")
    else:
        print(f"Os triângulo têm áreas iguais [{areax}] -- [{areay}]")

def istriangulo(a=0,b=0,c=0):
    c1 = ((abs(b-c) < a) & (a < b+c))
    c2 = ((abs(a-c) < b) & (b < a+c))
    c3 = ((abs(a-b) < c) & (c < a+b))
    if (c1 & c2 & c3):
        return areatriagulo(a,b,c)
    else:
        print("Input ivalid: is not a Triangle")
        return False

def main():
    area = list()
    i = 1
    while True:
        a = int(input(f"Digite o lado a do triangulo {i}: "))
        b = int(input(f"Digite o lado b do triangulo {i}: "))
        c = int(input(f"Digite o lado c do triangulo {i}: "))
        check = istriangulo(a,b,c)
        if check :
            area.append(istriangulo(a,b,c))
        else:
            continue
        if i == 2:
            break
        i += 1

    end(area[0], area[1])

main()