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
            if 0 == (length % 2):
                half_length = length // 2
                if cell[:half_length] == cell[half_length:]:
                    ctr = ctr + int(cell)
    return ctr

if __name__ == '__main__':
    inputDataList = getInputData()
    mainOutput = main(inputDataList)
    print (mainOutput)