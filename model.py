def calc_charges(num):
    if int(num) % 100 == 0:
        final_num = float(num)*3
    else:
        final_num = float(num)*3.5
    return final_num
