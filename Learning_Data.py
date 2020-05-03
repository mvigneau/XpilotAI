 
import sys
import xlwt
from xlrd import open_workbook
from xlutils.copy import copy                           

def Save_Data(filename, sheet_number, titles, data, first_time):

       print(filename)
       ## Open existing workbook ##
       book = open_workbook(filename)
       #print("found file")
       ## Get the first sheet inside the workbook ##
       r_sheet = book.sheet_by_index(sheet_number)


       ## Copy the workbook read over into a workbook we can write into ##
       wb = copy(book)
       #print("got new workbook")
       ## Get the sheet to write to within the writable copy ##
       w_sheet = wb.get_sheet(sheet_number)

       ## find the first row that has no data (empty) ##
       number_rows = r_sheet.nrows

       ## write titles of each column at top ##
       if(first_time == True):
              for number in range(len(titles)):
                     w_sheet.write(number_rows, number, titles[number])
                     print(titles[number])
              number_rows += 1
              first_time == False

       ## find the first row that has no data (empty) ##
       number_rows = r_sheet.nrows


       ## Write to writable sheet ##
       for col in range(len(data)):
              w_sheet.write(number_rows, col, data[col])
              print(data[col])

       ## save the writable workbook 
       wb.save(filename)
