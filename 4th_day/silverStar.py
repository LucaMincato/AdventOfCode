def main():
    rc = 1  # number of row to check
    rc_array = []
    sum_input = 4
    sum_thrs = sum_input + 1 # devo considerare che l'elemento che prendo non viene contato
    input_data = '..@@.@@@@.@@@.@.@.@@@@@@@.@.@@@.@@@@..@.@@.@@@@.@@.@@@@@@@.@.@.@.@.@@@@.@@@.@@@@.@@@@@@@@.@.@.@@@.@.'
    length_data = len(input_data)
    length_column = 10
    output_data = []

    for i in range(-rc,rc + 1):
        rc_array.append(i)

    dx_edge = length_column - 1
    for el_idx in range(length_data):
        sum_of_paper = 0
        print('this is', el_idx, input_data[el_idx])
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
                    print(start)
                    print(end)
                    check_el = input_data[start : end]
                    sum_of_paper = sum_of_paper + check_el.count('@')

                if sum_of_paper > sum_thrs:
                    output_data[-1] = '@'
                    break
        else:
            output_data.append('.')

        if el_idx == dx_edge:
            dx_edge = dx_edge + length_column
    print(output_data)
    output_sum = output_data.count('x')
    return output_sum


if __name__ == "__main__":
    output = main()
    print(output)
