from fpdf import FPDF
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="lockandkey"
)

mycur = mydb.cursor()
mycur.execute("select * from it ")
data = mycur.fetchall()

pdf = FPDF()
pdf.add_page()

pdf.set_font('Arial', 'B', 16)
for i in data:
    for j in i:
        k=str(j)+"\t"
        pdf.cell(70,40, k)
        print(k)
pdf.output('tuto1.pdf', 'F')