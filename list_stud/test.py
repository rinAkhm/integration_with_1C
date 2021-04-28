# class test:
#     def __init__(self, l):
#         self.l= l

#     def __add__(self,other):
#         new_list = []
#         if isinstance(other, list):
#             for i in range(len(other)): 
#                 print(other[0])
#                 z = self.l[i].copy()
#                 w = other[0].copy()
#                 print(z.update(w))
#                 # self.l[i] = self.l[i].setdefault(other[0])
#                 # print(self.l[i])




# x = test([{1:'name',2:'surname',3:'other'},{1:'name2',2:'surname2',3:'other2'}])
# x.__add__([{4:'data',5:'prcocess'}])