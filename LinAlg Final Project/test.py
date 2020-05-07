mod_input = int(input("For mod 26, type '26'. For mod 29, type '29': "))


for determinant in range(0,26):
    for i in range(0, 26):
        if (abs((determinant * i) % mod_input) == 1):
            # new_scalar = i
            print("The determinant is: {} and the scalar is {}".format(determinant,i))
            # reverse_matrix = (new_scalar * new_matrix) % 26
        else:
            # print("There is no mod.")
            continue

