# https://www.codewars.com/kata/5a6225e5d8e145b540000127/train/python
# def common(a, b, c):
#     sum = 0
#     a_dict = {}
#     for item in a:
#         if item in a_dict.keys():
#             a_dict[item] +=1
#         else:
#             a_dict[item] = 1
#     b_dict = {}
#     for item in b:
#         if item in b_dict.keys():
#             b_dict[item] +=1
#         else:
#             b_dict[item] = 1      
#     c_dict = {}
#     for item in c:
#         if item in c_dict.keys():
#             c_dict[item] +=1
#         else:
#             c_dict[item] = 1
#     for key, val in a_dict.items():
#         if key in b_dict.keys() and key in c_dict.keys():
#             count = a_dict.values()
#             sum = key*count
    
            
#     return a, b, c, sum

a = [1, 2, 2, 3]
b = [5, 3, 2, 2]
c = [7, 3, 5, 2]

def creat_dictionary(list: dict):
    def_dict = {}
    for item in a:
         if item in def_dict.keys():
             def_dict[item] +=1
         else:
             def_dict[item] = 1
    return def_dict

print(creat_dictionary(a))