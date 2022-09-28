list = [(4, 5), (4, ), (8, 6, 7), (1, 2), (3, 4, 6, 7)]
print("The original list : " + str(list))
K = 2
res = [ele for ele in list if len(ele) != K]
print("Filtered list : " + str(res))