
def parseInput():
    f = open("inputData.txt", "r")
    return f.readlines()


def main(listInput):
    somma = 50
    ctr = 0
    for row in listInput:
        if 'r' in row.lower():
            cell = row.split('R')
            tmp = int(cell[1].replace('\n',''))
            if tmp > 99:
                tmp = tmp % 100

            somma_totale = somma + tmp
        else:
            cell = row.split('L')
            tmp = int(cell[1].replace('\n',''))
            if tmp > 99:
                tmp = tmp % 100
                
            somma_totale = somma - tmp

        if somma_totale < 0:
            somma = somma_totale + 100
        elif somma_totale > 99:
            somma = somma_totale - 100
        else:
            somma = somma_totale

        if somma == 0:
            ctr = ctr + 1
    print(ctr)

if __name__ == "__main__":
    list_input = parseInput()
   # list_input = ['L68','L30','R48','L5','R60','L55','L1','L99','R14','L82', 'L132']
    main(list_input)