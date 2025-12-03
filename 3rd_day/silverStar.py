def getInputData():
    output = []
    with open('provaInput.txt', 'r', encoding='utf-8') as input_data:
        for row in input_data.readlines():
            tmp = row.replace('\n','')
            output.append(tmp)
        return (output)

def main(inputData):
    max_tot = 0
    for bank in inputData:
        length = len(bank)
        print(bank)
        max_decine = 0
        max_unità = 0
        idx = 1
        for row in bank:
            if idx == 1:
                max_unità = int(row)
            elif idx == 2:
                max_decine = max_unità
                max_unità = int(row)
            elif idx == length:
                if int(row) > max_unità:
                    max_unità = int(row)
            else:
                if int(row) > max_decine:
                    max_decine = int(row)
                    max_unità = 0
                elif int(row) > max_unità:
                    max_unità = int(row)
                else:
                    # do nothing
                    pass
            max_bank = max_decine * 10 + max_unità
            idx = idx + 1
        print(max_bank)
        max_tot = max_tot + max_bank
    return max_tot

if __name__ == '__main__':
    inputDataList = getInputData()
    output = main(inputDataList)
    print('The output is:')
    print(output)