import xlrd


class Excel_data():
    # OA_datal换为__init__自动被调用
    def OA_data1(self,path):
        self.data=xlrd.open_workbook(path)
        self.table=self.data.sheet_by_index(0)

#         # 获取总列数
        self.colNUM=self.table.ncols
        list0 = []
        for i in range(self.table.ncols):

            a=self.table.col_values(i)
            # print(a)
            list0.append(a)
        # print(list0)
        return list0
#       获取总行数
#         self.rowNUM=self.table.nrows
#     def OA_data2(self):
#         if self.colNUM <= 1:
#             print("总行数小于1")
#         else:
#             result = []
#         # 按行读取表格内容添加到result列表中，方便调用
#             for line in range(self.colNUM):
#                 shuju = self.table.col_values(line)
#                 result.append(shuju)
#             print(result)
#             return result


# path=r"C:\Users\000\Desktop\OA.xlsx"
# a=Excel_data()
# a.OA_data1(path)
# a.OA_data2()