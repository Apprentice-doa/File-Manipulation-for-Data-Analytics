#Importing the required libraries
import csv
import xlsxwriter


headers = ["First Name", "Last Name", "Marks"] # Column headers
students_list = [["Dele", "Ola", "50"], ["Chris", "Kelvin", "30"], ["David", "Dam", "90"],
                 ["Kunle", "Adebayo", "60"], ["Abu", "Philip", "100"], ["Seyi", "Adegboyega", "28"],
                 ["christie", "Queen", "16"], ["Ezra", "Daniels", "76"], ["Klaus", "John", "45"], ["Dele", "Ali", "87"],
                 ["Dele", "Ali", "87"], ["David", "Seeker", "75"], ["Kunle", "Fola", "12"], ["Enoch", "Fort", "10"],
                 ["Stan", "Best", "28"], ["Clifford", "James", "28"]] # Row by row entries

# Running a loop function to enter the header values and the row values
with open("students_list.csv", "w", newline="") as stud:
    student = csv.writer(stud)
    student.writerow(headers)
    student.writerows(students_list)

# Getting the mail addresses of the entries by concatinating their name first name and last and name
for mail in students_list:
    maile = mail[0] + "." + mail[1] + "@eng.uniben.edu"
    print(maile)

note = open("C:\\Users\\danie\\OneDrive\\Desktop\\Data Sets\\Aproko.csv",'w')  # To print  to another location other than IDE
# alvin.write()
note.close()

workbook = xlsxwriter.Workbook("newxcl.xlsx") # Creating a worksheet in a spreadsheet
worksheet = workbook.add_worksheet("iphone") # Creating worksheets in a workbook
worksheeet = workbook.add_worksheet("ipad") # Creating worksheets in a workbook
worksheeeet = workbook.add_worksheet("ipod") # Creating worksheets in a workbook
worksheet.write("A1", "Student Name") # Column A and Row 1
worksheet.write("B1", "Marks") # Column B and Row 2
rowindex = 2
workbook.close()
