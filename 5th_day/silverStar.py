def getInputData():
    output_range = []
    output_value = []
    flag = True
    with open('InputData.txt', 'r', encoding='utf-8') as input_data:
        for row in input_data.readlines():
            tmp = row.replace('\n','')
            if '' == tmp:
                flag = False
            elif flag:
                output_range.append(tmp)
            else:
                output_value.append(tmp)

        return (output_range, output_value)

def main(inputListRange , inputListValue):
    output = 0
    # define the edge of the range
    for row_value in inputListValue:
        for row_range in inputListRange:
            cells = row_range.split('-')
            start = int(cells[0])
            end = int(cells[1])

            if int(row_value) >= start and int(row_value) <= end :
                output = output + 1
                break

    return output




if __name__ == '__main__':
    (inputListRange , inputListValue) = getInputData()
    output = main(inputListRange , inputListValue)
    print(output)