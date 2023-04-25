import openpyxl

wb_obj = openpyxl.Workbook()

sheet = wb_obj.active
sheet['A1'] = 2
sheet['A2'] = 3
wb_obj.save('data.xlsx')