# create a empty text file
from fpdf import FPDF
import mysql.connector
import  webbrowser
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="lockandkey"
)
text="\n"
fp = open('recrd.txt', 'w')
mycur = mydb.cursor()
mycur.execute("select * from it ")
data = mycur.fetchall()
print(data)
fp.write("Depeartment Name\t\t\t\t\t Name \t\t\t Assgin Lockers \t Key Holder Name \t Type \n\n")
for i in data:
    for j in i:
        #print(j)
        line =""
        line=str(j)+"\t\t"
        fp.write(" | ")
        fp.write(line)
    fp.write("\n")
fp.close()

from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.set_font("Arial", size=15)
pdf.rect(10, 10, 180, 400)

f = open("recrd.txt", "r")
c=0
count=0

for x in f:
    print(x)
    pdf.cell(200, 8, txt=text, ln=1 ,align='C')

    pdf.cell(180, 8, txt=x, ln=1,align='C')

pdf.output("record.pdf")
webbrowser.open_new_tab(r"C:/Users/rupal/PycharmProjects/lockerproj/record.pdf")

