import random
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
import argparse

parser = argparse.ArgumentParser(description="Mitt program för att skapa enkla träningspapper för matte")
parser.add_argument("uträkning", choices=["x","-","+","/"], help="Välj uträkning (+,-,x,/)")
parser.add_argument("-d1","--digitsone", type=int, default=2, help="antal siffror i det första talet")
parser.add_argument("-d2","--digitstwo", type=int, default=2, help="antal siffror i det andra talet")
args = parser.parse_args()


def create_basic_canvas(path="övningar.pdf"):
    c = Canvas(path, pagesize=A4)
    width, height = A4
    uträknare = args.uträkning
    d1 = args.digitsone
    d2 = args.digitstwo

    low1 = 10 ** (d1-1)
    high1 = (10 ** d1) -1
    low2 = 10 ** (d2-1)
    high2 = (10 ** d2) -1

    
    #Rubrik
    c.setFont("Helvetica-Bold", 20)
    c.drawString(20*mm, height - 20*mm, "Matte papper uträkningar")

    #Förklaring
    c.setFont("Helvetica", 12)
    c.drawString(20 * mm, height - 30 * mm, "40 övningar i matte")

    #Avgränsare
    c.setStrokeColor(colors.HexColor("#333333"))
    c.setLineWidth(1.2)
    c.line(20 * mm, height - 35 * mm, width - 20 * mm, height - 35 * mm)

    #Uträkningar
    c.setFont("Helvetica", 11)
    for y in range (10):
        for x in range(4):
            c.drawString(20*mm + (x*45)*mm, (height-50*mm) - (y*20)*mm, f"{random.randint(low1,high1)}{uträknare}{random.randint(low2,high2)}= ____")

    c.showPage()
    c.save()

if __name__ == "__main__":
    create_basic_canvas()
