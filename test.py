import xlrd
import xlsxwriter

path = "book.xlsx"

inputWorkbook = xlrd.open_workbook(path)
inputWorksheet = inputWorkbook.sheet_by_index(0)

print(inputWorksheet.nrows)


dict = {}

for x in range(1, inputWorksheet.nrows):
    dict[inputWorksheet.cell_value(x, 0)] = [inputWorksheet.cell_value(x, 1)]
    
for i in dict:
    print (i)
    print(dict[i])
    
    
outWorkbook = xlsxwriter.Workbook("out.xlsx")
outSheet = outWorkbook.add_worksheet()

i = 0;
for key, value in dict.items():
    outSheet.write(i, 0, key)
    val = str(value)[1:-1]
    outSheet.write(i, 1, int(val))
    i+=1
    

outWorkbook.close()

    

