from flask import Flask, send_file
import firebase_admin
from firebase_admin import credentials, db
from barcode import EAN13, UPCA, EAN8
from pdf_mail import sendpdf
from fpdf import FPDF
import os
from barcode.writer import ImageWriter
from PIL import Image


cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "silent-owl-flight",
    "private_key_id": "c949f25c81e713a4ca169808342f4038f5bd08de",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDO2CvYUwEZ81N3\n7BuS4IO2NwBOxg4SBSkkwAjkvqySV3QUWJeESLXdp571VZAuQnny62Dp34Ki0AYu\n3vmJ1cwuekBfoB6XhhTPflgpNJGWko1H3qRUVVrvSGhJhFsZV0KjL1ZCxo+hrfxx\nfkre6JvBvt81GbKbX3V5nMePcza8yznmCJFiw7G05VmR2Orvb0XrMoVXVm222I0c\nGM4LoEzGK3kP4nxewXqM3xiRzLMolTS//hMtezXf2MhWarhgO0Pr9WW6TjOVclrY\nkZyfTVSyxLcdd1wyzCktCvuu9cSvg06K/tB6TrxSeerH0Tfc/Y5bIXs4PEPvmKxc\n50zVu0ufAgMBAAECggEANbiFIqjkJ1Y//mxu+OWgr6l3Rf5AV0PJ3MaXSLmQ3m0i\nM8qSh4PO4CORsEwppyoSvBmP0Q4AwsJeaLv2eWrynbuYjn1qlJX5P66jvQfvK/ki\nAmF7sn98n5rhov5iHqHAJ9u6fptNYINshhlz3pLxKQ+mrwbekWXof85NMh+NPtjd\nbZNebPxs0ai+9zcuHGxGkZCMWR5QQxurCfJQOuL9YRRXWHENUOBqHrnSBMsxJnIa\nv0rzIv0Zw8M0O8CbLQwQXJLGYbz1WxHh/70tO131Ef52/DQimafkdlJkaDpxvokb\nRLfpHYamUkfEyTj05wwf9kI3fnr3CWLsoZgELd3H4QKBgQD4f+Ezk4ERxNXnLjwR\nBkmdpaH6sLGpoPgQWP5k7x0VFmGpx4inyuxRxE0X5bHLlXH2xacWy0k91wdVXxUE\n5uey6RJzYrV92k0iz0FeIliG1J3CenY+9TBpy0BhKD3wU0Z6U+JG7lMZhdPO6xSL\ntQvtKTCTKYObJ7Q5Mem493mO0QKBgQDVFm2x0a8ZEhKn8rA319CesYlp8YTf+pCb\nPUzDPpsB13BIpUdRyeBVkjsWwdXHzNffXmg3LUPXJLu7JRrKHV3kmGohCM+D30iT\n1SqRl6KDLbyyVEwEgKpZkkSwecVKfJdnffLF5ZDxVzK/yTf4dINqJFtlJtqgn6zk\nFRExiW4vbwKBgQCHYlxWFiG2hY+oELdm6w8GVWvnQYa5jNo5RdLrOJ6Wk4gH0I6y\nI8sWTSVXRKvV54icUljTAVPY3iK/rzqrXgWToomL1ZZdh6aItXO+jmW+p21/u+pa\nKIkEylg71onQOf5mvPbFgChD+nZIAClEaBGkVtGBC5gI2tvEYV4diK5wUQKBgA2f\nl3fM7iLuMt8l9vo7BA2BUEXDuTkQrfoe2y+IaySc/4LFfl/ORldyN/Dmh6J0iECx\nqnwMms/Ae3glkSbm5b/dtrtR8uJ9fghlkokoZq14WR4VoZ6QE1QSs+2Me36dpJhr\nRwA8Ax5K8uWsGbX6zQQWOvmmmEe4rbcPWcAPB0plAoGAFhI5zBP7PLTMmuYIaFnl\nIbdO0Yc27ABkaFHxqrVexJzClqQ64KiSiJv4yb+gO0ux3kbpE6grt2/YlJkCjdzI\nh323NvVto1Fo+CjtAwyWH7+DlGGk4ThQM62JmXk9NcG4tS1xOZrkA4zakaWBtz35\n4q+b0suRRrNNZ+u0ruFlLxI=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-q168e@silent-owl-flight.iam.gserviceaccount.com",
    "client_id": "113686962064434702925",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-q168e%40silent-owl-flight.iam.gserviceaccount.com"
})
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://silent-owl-flight-default-rtdb.europe-west1.firebasedatabase.app",
    'storageBucket': "silent-owl-flight.appspot.com"
})
database = db

app = Flask(__name__)

barcodes_arrays = []

@app.route('/')
def secretary2():
    global nine3, qp
    qp = []
    nine3 = database.reference("REQUESTS").child("SHOP").get()
    barcode = database.reference("BARCODE").get()
    
    if nine3 is not None and 'pdfs' in nine3:
        for keys, data in nine3['pdfs'].items():
            qp = data[0]
            return sever_supreme(n=len(data[0]), b='many', p='many', e=data[1], k=keys, w='pdfs')

    if nine3 is not None and 'requests' in nine3:
        for keys, data in nine3['requests'].items():
            qp = []
            return sever_supreme(n=data[0], b='any', p='any', e=data[1], k=f"{keys}", w='requests')

    if nine3 is not None and 'xuntian' in nine3:
        for keys, data in nine3['xuntian'].items():
            qp = []
            return sever_supreme(n=data[2], b=f"{data[1]}", p=data[0], e=data[3], k=f'{keys}', w='xuntian')
    return 'Success Now!'
    
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
            # ean.save(f'{bar_number}{i+1}')
            right = 370
            barcodes_arrays.append(ean.save(f'{bar_number}{i+1}'))
        elif len(bar_number) == 12 and b == 'many':)
            ean = UPCA(bar_number, writer=ImageWriter())
            # ean.save(f'{bar_number}{i+1}')
            barcodes_arrays.append(ean.save(f'{bar_number}{i+1}'))
        elif len(bar_number) == 12 and b == 'any':
            ean = EAN13(bar_number, writer=ImageWriter())
            # ean.save(f'{bar_number}{i + 1}')
            barcodes_arrays.append(ean.save(f'{bar_number}{i+1}'))
        elif len(bar_number) == 13 and b == 'many' or w == 'xuntian':
            ean = EAN13(bar_number, writer=ImageWriter())
            # ean.save(f'{bar_number}{i+1}')
            barcodes_arrays.append(ean.save(f'{bar_number}{i+1}'))
    #     image = Image.open(f'{bar_number}{i+1}.png')
    #     nue = image.crop((left, upper, right, lower))
    #     nue.save(f'{bar_number}{i+1}.png')
    #     out.append(f'{bar_number}{i+1}.png')
    #     if len(out) == n:
    #         do = True

    # pdf = FPDF('P', 'mm', 'A4')

    # def doer():
    #     while len(out) != 0 and do is True:
    #         pdf.add_page(orientation='P')
    #         pdf.ln(5)
    #         pdf.set_auto_page_break(auto=True, margin=1)
    #         pdf.set_top_margin(20)
    #         pdf.set_x(0)
    #         pdf.set_font("Arial", size=8)
    #         kill_em = out[:36]
    #         for j in kill_em:
    #             r = 0
    #             jj = kill_em.index(j) + 1
    #             if jj % 4 == 1:
    #                 r = 5
    #             elif jj % 4 == 2:
    #                 r = 55
    #             elif jj % 4 == 3:
    #                 r = 105
    #             elif jj % 4 == 0:
    #                 r = 155
    #             else:
    #                 break
    #             t = 0
    #             if 0 < jj <= 4:
    #                 t = 10
    #             elif 4 <= jj <= 8:
    #                 t = 41.5
    #             elif 8 < jj <= 12:
    #                 t = 73
    #             elif 12 < jj <= 16:
    #                 t = 104.5
    #             elif 16 < jj <= 20:
    #                 t = 136
    #             elif 20 < jj <= 24:
    #                 t = 167.5
    #             elif 24 < jj <= 28:
    #                 t = 199
    #             elif 28 < jj <= 32:
    #                 t = 231.5
    #             elif 28 < jj <= 36:
    #                 t = 261
    #             else:
    #                 break

    #             pdf.set_xy(r, t)
    #             pdf.image(j, w=50, h=20)
    #             if p == 'many':
    #                 pdf.text(r + 5, t, txt=qp[0][1])
    #                 qp.pop(0)
    #             elif p == 'any':
    #                 pdf.text(r + 5, t, txt=qp[0])
    #                 qp.pop(0)
    #             elif p == 'none':
    #                 pdf.text(r + 5, t, txt='Products of a kind')
    #             else:
    #                 pdf.text(r + 5, t, txt=p)
    #             # pdf.cell(r, t, txt="ITEM ONE", ln=True, align="C")
    #             # if
    #             # names.remove(kill_em.index(j))
    #             out.remove(j)
    #             os.remove(j)
    #             # pdf.set_font("Arial", size=13)
    #             pdf.text(81, 290, txt="From Moneyjar Solutions Barcode Server")

    # if len(out) > 0:
    #     doer()
    # pdf.output('BARCODES.pdf')
    
    # kk = sendpdf(sender_email=f"{mail}", sender_password=f"{pw}",
    #             subject="HERE IS YOUR BARCODES PDF", body="Thank you for using Moneyjar app in your business",
    #             filename="BARCODES",
    #             address_of_file="C:/Users/truth/Desktop/New folder",
    #             receiver_email=e)

    # kk.email_send()
    # database.reference("REQUESTS").child("SHOP").child(f'{w}').child(f"{k}").delete()
    return 'Success Then!'


if __name__ == '__main__':
    app.run(debug=True)
