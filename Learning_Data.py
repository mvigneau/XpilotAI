 
import sys
import xlwt
from xlrd import open_workbook
from xlutils.copy import copy                           

def Save_Data(filename, sheet_number, titles, data, number_rows):

       ## Open existing workbook ##
       book = open_workbook(filename)

       ## Get the first sheet inside the workbook ##
       r_sheet = book.sheet_by_index(sheet_number)


       ## Copy the workbook read over into a workbook we can write into ##
       wb = copy(book)

       ## Get the sheet to write to within the writable copy ##
       w_sheet = wb.get_sheet(sheet_number)

       ## find the first row that has no data (empty) ##
       number_rows = r_sheet.nrows
       print(number_rows)

       ## write titles of each column at top ##
       if number_rows == 0:
              for number in range(titles):
                     w_sheet.write(0, number, titles[number])

       ## Write to writable sheet ##
       for col in range(data):
              w_sheet.write(number_rows, col, data[col])

       ## save the writable workbook 
       wb.save(filename)
