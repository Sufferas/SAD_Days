def day_3(name):
    with open(name) as f:
        contents = f.readlines()

    content_len_num_0 = []
    content_len_num_1 = []
    content_len_num_gama = []
    content_len_num_epsilon = []

    content_len_num_range = 12
    for i in range(content_len_num_range):
        content_len_num_1.append(0)
        content_len_num_0.append(0)
        content_len_num_gama.append(0)
        content_len_num_epsilon.append(0)

    for content in contents:
        len(content)
        for x in range(len(content)-1):
            if int(str(content)[x]) == 0:
                content_len_num_0[x] = content_len_num_0[x] + 1
            else:
                content_len_num_1[x] = content_len_num_1[x] + 1

    for x in range(content_len_num_range):
        if content_len_num_1[x] < content_len_num_0[x]:
            content_len_num_gama[x] = 0
            content_len_num_epsilon[x] = 1
        else:
            content_len_num_gama[x] = 1
            content_len_num_epsilon[x] = 0

    str_gama =''
    str_epsilon = ''
    for x in range(content_len_num_range):
        str_gama = str_gama + str(content_len_num_gama[x])
        str_epsilon = str_epsilon + str(content_len_num_epsilon[x])

    print("Submarine power consumption:", int(str(binaryToDecimal(int(str_gama)))) * int(str(binaryToDecimal(int(str_epsilon)))))


def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal