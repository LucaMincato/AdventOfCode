def getInputData():
    with open('provaInput.txt', 'r', encoding='utf-8') as input_data:
        tmp = input_data.readlines()
        output = tmp[0].replace(' \n','').split(',')
        return (output)

def main(inputData):
    ctr = 0
    for row in inputData:
        cells = row.split('-')
        start = int(cells[0])
        end = int(cells[1]) + 1
        for idx in range(start, end):
            cell = str(idx)
            length = len(cell)
            start_element = 2
            for element in range(start_element, length + 1):
                if 0 == (length % element):
                    element_length = (length // element)
                    blocchi = [cell[i:i + element_length]
                                 for i in range(0, len(cell), element_length)]
                    if len(set(blocchi)) == 1:
                        ctr = ctr + int(cell)
                        break

    return ctr

if __name__ == '__main__':
    inputDataList = getInputData()
    mainOutput = main(inputDataList)
    print (mainOutput)