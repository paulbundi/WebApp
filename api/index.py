from flask import Flask, render_template_string, render_template
import firebase_admin
import requests
from firebase_admin import credentials, db
from barcode import EAN13, UPCA, EAN8
from pdf_mail import sendpdf
from cryptography.fernet import Fernet
from fpdf import FPDF
import os
from barcode.writer import ImageWriter
from PIL import Image

app = Flask(__name__)

@app.route('/')
def secretary2():
    global nine3, qp
    qp = []
    nine3 = database.reference("REQUESTS").child("SHOP").get()
    # barcode = database.reference("BARCODE").get()
    # print(nine3['pdfs'])
    if nine3 is not None and 'pdfs' in nine3:
        for keys, data in nine3['pdfs'].items():
            qp = data[0]
            sever_supreme(n=len(data[0]), b='many', p='many', e=data[1], k=keys, w='pdfs')

    if nine3 is not None and 'requests' in nine3:
        for keys, data in nine3['requests'].items():
            qp = []
            sever_supreme(n=data[0], b='any', p='any', e=data[1], k=f"{keys}", w='requests')

    if nine3 is not None and 'xuntian' in nine3:
        for keys, data in nine3['xuntian'].items():
            qp = []
            sever_supreme(n=data[2], b=f"{data[1]}", p=data[0], e=data[3], k=f'{keys}', w='xuntian')
    return 'Success!'
    
@app.route('/shh')
def sever_supreme(n, b, p, e, k, w):
    out = []
    names = []
    do = False

    for i in range(n):
        left = 50
        upper = 0
        right = 470
        lower = 200
        bar_number = ''
        if b == 'many' and w == 'pdfs':
            bar_number = f"{qp[i][0]}"
            names.append(qp[i][1])
        elif b == 'any':
            barcode = database.reference("bar").get()
            bar_number = f"{barcode['code']+1}"
            qp.append(f"STANDALONE PRODUCT {i+1}")
            database.reference("bar").update({'code': int(f"{barcode['code']+1}")})
        elif w == 'xuntian':
            bar_number = b

        if len(bar_number) == 8:
            ean = EAN8(bar_number, writer=ImageWriter())
            ean.save(f'{bar_number}{i+1}')
            right = 370
        elif len(bar_number) == 12 and b == 'many':)
            ean = UPCA(bar_number, writer=ImageWriter())
            ean.save(f'{bar_number}{i+1}')
        elif len(bar_number) == 12 and b == 'any':
            ean = EAN13(bar_number, writer=ImageWriter())
            ean.save(f'{bar_number}{i + 1}')
        elif len(bar_number) == 13 and b == 'many' or w == 'xuntian':
            ean = EAN13(bar_number, writer=ImageWriter())
            ean.save(f'{bar_number}{i+1}')
        image = Image.open(f'{bar_number}{i+1}.png')
        nue = image.crop((left, upper, right, lower))
        nue.save(f'{bar_number}{i+1}.png')
        out.append(f'{bar_number}{i+1}.png')
        if len(out) == n:
            do = True

    pdf = FPDF('P', 'mm', 'A4')

    def doer():
        while len(out) != 0 and do is True:
            pdf.add_page(orientation='P')
            pdf.ln(5)
            pdf.set_auto_page_break(auto=True, margin=1)
            pdf.set_top_margin(20)
            pdf.set_x(0)
            pdf.set_font("Arial", size=8)
            kill_em = out[:36]
            for j in kill_em:
                r = 0
                jj = kill_em.index(j) + 1
                # row = (n - 1) % 3 + 1
                # if row == 1:
                #     r = 5
                # elif row == 2:
                #     r = 70
                # elif row == 3:
                #     r =135
                if jj % 4 == 1:
                    r = 5
                elif jj % 4 == 2:
                    r = 55
                elif jj % 4 == 3:
                    r = 105
                elif jj % 4 == 0:
                    r = 155
                else:
                    break
                t = 0
                if 0 < jj <= 4:
                    t = 10
                elif 4 <= jj <= 8:
                    t = 41.5
                elif 8 < jj <= 12:
                    t = 73
                elif 12 < jj <= 16:
                    t = 104.5
                elif 16 < jj <= 20:
                    t = 136
                elif 20 < jj <= 24:
                    t = 167.5
                elif 24 < jj <= 28:
                    t = 199
                elif 28 < jj <= 32:
                    t = 231.5
                elif 28 < jj <= 36:
                    t = 261
                else:
                    break

                pdf.set_xy(r, t)
                pdf.image(j, w=50, h=20)
                if p == 'many':
                    pdf.text(r + 5, t, txt=qp[0][1])
                    qp.pop(0)
                elif p == 'any':
                    pdf.text(r + 5, t, txt=qp[0])
                    qp.pop(0)
                elif p == 'none':
                    pdf.text(r + 5, t, txt='Products of a kind')
                else:
                    pdf.text(r + 5, t, txt=p)
                # pdf.cell(r, t, txt="ITEM ONE", ln=True, align="C")
                # if
                # names.remove(kill_em.index(j))
                out.remove(j)
                os.remove(j)
                # pdf.set_font("Arial", size=13)
                pdf.text(81, 290, txt="From Moneyjar Solutions Barcode Server")

    if len(out) > 0:
        doer()
    pdf.output('BARCODES.pdf')
    # kk = sendpdf(sender_email=f"{mail}", sender_password=f"{pw}",
    #             subject="HERE IS YOUR BARCODES PDF", body="Thank you for using Moneyjar app in your business",
    #             filename="BARCODES",
    #             address_of_file="C:/Users/truth/Desktop/New folder",
    #             receiver_email=e)

    # kk.email_send()
    # database.reference("REQUESTS").child("SHOP").child(f'{w}').child(f"{k}").delete()
    return 'Success!'


if __name__ == '__main__':
    app.run(debug=True)
