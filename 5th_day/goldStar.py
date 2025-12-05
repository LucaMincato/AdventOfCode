def getInputData():
    output_range = []
    flag = True

    with open('InputData.txt', 'r', encoding='utf-8') as input_data:
        for row in input_data.readlines():
            tmp = row.replace('\n','')
            if '' == tmp:
                flag = False
            elif flag:
                cells = tmp.split('-')
                start = int(cells[0])
                end = int(cells[1])
                input_dict = {'start': start, 'end':end}
                output_range.append(input_dict)
            else:
                break
        return (output_range)

def main(inputListRange):
    output_list = []
    flag = True
    # define the edge of the range
    for row_range in inputListRange:
        start = row_range['start']
        end = row_range['end']
        if flag:
            output_list.append(row_range)
            flag = False
        else:
            for idx in range(len(output_list)):
                if start == output_list[idx]['start'] and  end == output_list[idx]['end']:
                    break
                # |->
                if start <= output_list[idx]['end'] and end > output_list[idx]['end'] and start > output_list[idx]['start']:
                    output_list[idx]['end'] =  end
                    break
                # <-|
                elif start < output_list[idx]['start'] and end <= output_list[idx]['end'] and end >= output_list[idx]['start']:
                    output_list[idx]['start'] =  start
                    break
                elif (start > output_list[idx]['end'] and end > output_list[idx]['end']) or (start < output_list[idx]['start'] and end < output_list[idx]['start']):
                    if  idx == (len(output_list) - 1):
                        output_list.append(row_range)
                elif (start <= output_list[idx]['start'] and end >= output_list[idx]['end']):
                    output_list[idx]['start'] =  start
                    output_list[idx]['end'] =  end
                else:
                    break
    return output_list




if __name__ == '__main__':
    (inputListRange) = getInputData()
    output = inputListRange
    flag = True
    while flag:
        output_k1 = output
        output = main(output)
        if output == output_k1:
            flag = False

    sum = 0
    #print(output)
    for row in output:
        sum = sum + (row['end'] - row['start'] + 1)
    print(sum)
    #print(output)
    