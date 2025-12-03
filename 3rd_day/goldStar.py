def getInputData():
    output = []
    with open('provaInput.txt', 'r', encoding='utf-8') as input_data:
        for row in input_data.readlines():
            tmp = row.replace('\n','')
            output.append(tmp)
        return (output)

def main(inputData):
    max_tot = 0
    check_element = 12
    element_end = check_element - 1
    for bank in inputData:
        max_bank = 0
        element = []
        length = len(bank)
        print(bank)
        # fill the first values
        for i in range(check_element):
            element.append(0)
        idx = 0
        start = element_end - ((length - check_element) - 1)
        start = 1
        for row in bank:
            if idx > (length - check_element):
                for index in range(start,check_element):
                    if int(row) > element[index]:
                            element[index] = int(row)
                            if index == element_end:
                                pass
                            else:
                                for j in range(index + 1, check_element):
                                    element[j] = 0
                                break
                start = start + 1
            else:
                for index in range(check_element):
                    if int(row) > element[index]:
                            element[index] = int(row)
                            if index == element_end:
                                pass
                            else:
                                for j in range(index + 1, check_element):
                                    element[j] = 0
                                break
            idx = idx + 1
        for jj in range(check_element):
            max_bank = max_bank + element[jj] * (10 ** (element_end - jj))
        print(max_bank)
        max_tot = max_tot + max_bank
    return max_tot

if __name__ == '__main__':
    inputDataList = getInputData()
    output = main(inputDataList)
    print('The output is:')
    print(output)