def calc_charges(num):
    if int(num) % 100 == 0:
        final_num = float(num)*7.7
    else:
        final_num = float(num)*8.99
    return final_num
