def getInputData():
    output = ''
    with open('input.txt', 'r', encoding='utf-8') as input_data:
        for row in input_data.readlines():
            tmp = row.replace('\n','')
            output = output + tmp
        length = len(tmp)

        return (output, length)

def main(inputDataList , lengthDataList):
    rc = 1  # number of row to check
    rc_array = []
    sum_input = 4
    sum_thrs = sum_input + 1 # devo considerare che l'elemento che prendo non viene contato
    input_data = inputDataList
    length_data = len(input_data)
    length_column = lengthDataList
    output_data = []

    for i in range(-rc,rc + 1):
        rc_array.append(i)

    dx_edge = length_column - 1
    for el_idx in range(length_data):
        sum_of_paper = 0
        # guardo se c'è un rotolo di carta
        if '@' == input_data[el_idx]:
            output_data.append('x')
            # non sono nei bordi
            for row in rc_array:
                init_start_idx = el_idx - rc + row * length_column
                init_end_idx = init_start_idx + len(rc_array) - 1

                if init_start_idx >= length_data or init_end_idx < 0:
                    pass
                else:
                    if el_idx % length_column == 0:
                        start = init_start_idx + rc
                        end = init_end_idx
                    elif el_idx == dx_edge:
                        start = init_start_idx
                        end = init_end_idx - rc
                    else:
                        if init_start_idx < 0:
                            start = 0
                        else:
                            start = init_start_idx
                        end = init_end_idx
                    check_el = input_data[start : end + 1]
                    sum_of_paper = sum_of_paper + check_el.count('@')

                if sum_of_paper >= sum_thrs:
                    output_data[-1] = '@'
                    break
        else:
            output_data.append('.')

        if el_idx == dx_edge:
            dx_edge = dx_edge + length_column
    output_sum = output_data.count('x')


    return output_sum


if __name__ == "__main__":
    (inputDataList , lengthDataList) = getInputData()
    output = main(inputDataList , lengthDataList)
    print(output)
