from flask import Flask, request, jsonify, redirect
import smtplib
import json
import requests
from email.mime.text import MIMEText
from email.message import EmailMessage

app = Flask(__name__)

initialized = False
posta_data = {}
some_data = {}
some_data_ = {}
some_data_r = {}

@app.route('/')
def landing_page():
    html_text = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>MONEYJAR</title>
        <link rel="icon" href="https://firebasestorage.googleapis.com/v0/b/silent-owl-flight.appspot.com/o/MoneyJar%20copy.png?alt=media&token=6dc4f279-8ed1-4088-ad46-a79dc38d66be" type="image/png">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
        <style>
            .hero-bg {
                background-image: url('');
                background-size: cover;
                background-position: center;
                background-color: #393D47;

            }
            .form-input {
                border-color: #FFC107;
            }
            .form-input:focus {
                border-color: #FFD700;
                box-shadow: 0 0 0 2px rgba(255, 215, 0, 0.25);
            }
            .btn {
                background-color: green;
                color: #ffffff;
                border-radius: 20px;
            }
            .btn:hover {
                background-color: #558b2f;
            }
            .container-bg {
                background-color: #4CAF50;
            }
            .container-text {
                color: #ffffff;
            }
            .floating-layout {
                position: fixed;
                bottom: 26%;
                right: 13px;
            }
            .floating-layout1 {
                position: fixed;
                bottom: 40%;
                right: 13px;
            }
            .cta-btn1 {
                display: flex;
                justify-content: center;
                align-items: center;
                width: 60px;
                height: 60px;
                border-radius: 50%;
                background-color: green;
                color: gold;
                text-decoration: none;
                animation: inflate-deflate 3.5s infinite ease-in-out;
            }

            .cta-btn1 i {
                font-size: 39px;
            }

            @keyframes inflate-deflate {
                0%, 100% {
                    transform: scale(.9);
                }

                50% {
                    transform: scale(1.3);
                }
            }

            .cta-btn {
                display: flex;
                justify-content: center;
                align-items: center;
                width: 60px;
                height: 60px;
                border-radius: 50%;
                background-color: green;
                color: white;
                text-decoration: none;
            }

            .cta-btn i {
                font-size: 39px;
            }

            .custom-card {
                width: 90%;
                margin: auto;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 1);
                border-radius: 20px;
                margin-top: 5vh;
            }
            .custom-card2 {
                width: 90%;
                margin: auto;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 1);
                border-radius: 20px;
                margin-top: 5vh;
            }
            .d-flex {
                display: flex;
            }

            .justify-content-center {
                justify-content: center;
            }

            .align-items-center {
                align-items: center;
            }
            .social-icons {
                display: flex;
                justify-content: center;
                gap: 23px;
            }
            .social-icons a {
                color: #000;
                font-size: 29px;
            }

            .social-icons a:hover {
                color: gold;
            }
            .footer {
                width: 100%;
                position: fixed;
                bottom: 0;
                background-color: #f8f9fa;
                text-align: center;
                padding: 10px 0;
            }

            .footer p {
                margin: 0;
                color: #6c757d;
            }
        </style>
        <script>
            let currentSlide = 0;

            function showSlide(n) {
                const slides = document.getElementsByClassName('carousel-slide');
                for (let i = 0; i < slides.length; i++) {
                    slides[i].style.display = 'none';
                }
                currentSlide = (n + slides.length) % slides.length;
                slides[currentSlide].style.display = 'block';
            }

            function nextSlide() {
                showSlide(currentSlide + 1);
            }

            setInterval(nextSlide, 7430);
        </script>
        <script>
            let currentSlide1 = 0;

            function showSlide1(n) {
                const slides1 = document.getElementsByClassName('carousel-slide1');
                for (let i = 0; i < slides1.length; i++) {
                    slides1[i].style.display = 'none';
                }
                currentSlide1 = (n + slides1.length) % slides1.length;
                slides1[currentSlide1].style.display = 'block';
            }

            function nextSlide1() {
                showSlide1(currentSlide1 + 1);
            }

            setInterval(nextSlide1, 4330);
        </script>
    </head>
    <body>
        <div class="flex items-center justify-center min-h-screen hero-bg flex-col"> <!-- Added flex-col class for vertical flex container -->
            <div class="custom-card mx-auto bg-white shadow-lg rounded-lg overflow-hidden mb-8" style="height: 30%;"> <!-- Added inline style for width -->
                <div class="container-bg py-4 px-6 container-text text-center">
                    <h1 class="text-2xl font-bold">MONEYJAR SOLUTIONS</h1>
                    <p class="text-sm">We are a Kenyan Software as a Service company offering state-of-the-art and affordable software for all businesses.</p>
                    <p class="text-sm">Our platform is built with Cloud, Big Data and Merchine Learning technologies.</p>
                    <p class="text-sm">You will not need complementary hardware to get started with our app.</p>
                </div>
                <div class="p-6 text-center" style="background-image: url('https://firebasestorage.googleapis.com/v0/b/silent-owl-flight.appspot.com/o/MoneyJar%20copy.png?alt=media&token=6dc4f279-8ed1-4088-ad46-a79dc38d66be'); background-size: cover; background-position: center;">
                    <form class="space-y-4">
                        <div>
                            <a href="https://bit.ly/M-Jar" class="btn w-9/10 py-2 px-4 rounded-md font-medium">Install App</a>
                        </div>
                        <div>
                            <a href="https://bit.ly/pricing-paige" class="btn w-9/10 py-2 px-4 rounded-md font-medium">Pricing</a>
                        </div>
                        <div>
                            <a href="https://bit.ly/web-invictus" class="btn w-9/10 py-2 px-4 rounded-md font-medium">Share</a>
                        </div>
                        <div>
                            <a href="https://bit.ly/moneyjar-privacy-policy" class="btn w-9/10 py-2 px-4 rounded-md font-medium">Privacy Policy</a>
                        </div>
                        <div>
                            <a href="tel:+254112037947" class="btn w-9/10 py-2 px-4 rounded-md font-medium">Call Us</a>
                        </div>
                    </form>
                </div>
            </div>

            <div class="custom-card mx-auto bg-white shadow-lg rounded-lg overflow-hidden mb-8">
                <div class="container-bg py-4 px-6 container-text text-center">
                    <h1 class="text-2xl font-bold">Request Information</h1>
                </div>
                <div class="p-6 text-center">
                    <form action="/send_newsletter" method="POST" class="space-y-4">
                        <div>
                            <label for="name" class="block text-gray-700 font-medium">Your full name</label>
                            <input type="text" id="name" name="name" class="form-input w-full rounded-md bg-amber-200" style="width: 280px; height: 40px; text-align: center;" onfocus="this.style.boxShadow='0.5 0.5 0.5 2px gold';" onblur="this.style.boxShadow='none';">
                        </div>
                        <div>
                            <label for="email" class="block text-gray-700 font-medium">Your email address</label>
                            <input type="email" id="email" name="email" class="form-input w-full rounded-md bg-amber-200" style="width: 280px; height: 40px; text-align: center;" onfocus="this.style.boxShadow='0.5 0.5 0.5 2px gold';" onblur="this.style.boxShadow='none';">
                        </div>
                        <div>
                            <button type="submit" class="btn w-full py-2 px-4 rounded-md font-medium">Make inquiries</button>
                        </div>
                    </form>
                </div>
            </div>

            <!-- Card 2 content -->
            <div class="custom-card2 mx-auto bg-white shadow-lg rounded-lg overflow-hidden mb-8" style="height: 65%;"> <!-- Added inline style for width -->
                <div class="container-bg py-4 px-6 container-text text-center">
                    <div class="carousel-slide" style="display: none;">
                        <h1 class="text-2xl font-bold">How SHOP POS works</h1>
                        <p class="text-sm"> Our POS app will let you convert every product (goods & services) that your business offers into a barcode.</p>
                        <p class="text-sm"> That means that every item in a hotel menu and even re-packed products by retailers.</p>
                        <p class="text-sm"> Every time you make a sale you scan the barcode related to the product and the sale is recorded.</p>
                    </div>
                    <div class="carousel-slide" style="display: block;">
                        <h1 class="text-2xl font-bold">SHOP MONEYJAR POS</h1>
                        <p class="text-sm">📈 Round the clock app support.</p>
                        <p class="text-sm">📈 Built-in Barcode Scanner.</p>
                        <p class="text-sm">📈 Built-in Text Receipt System.</p>
                        <p class="text-sm">📈 Built-in AI Business Intelligence Dashboard for you 📊.</p>
                    </div>
                    <div class="carousel-slide" style="display: none;">
                        <h1 class="text-2xl font-bold">SHOP MONEYJAR POS</h1>
                        <p class="text-sm">📈 One and multiple-stores e-shop set up.</p>
                        <p class="text-sm">📈 Barcode Inventory System.</p>
                        <p class="text-sm">📈 Dedicated Barcode Server for your Re-packed & locally produced goods and services.</p>
                        <p class="text-sm">📈 Zero limit on products added to your inventory.</p>
                    </div>
                    <div class="carousel-slide" style="display: none;">
                        <h1 class="text-2xl font-bold">SHOP MONEYJAR POS</h1>
                        <p class="text-sm">📈 Employee performance monitoring.</p>
                        <p class="text-sm">📈 Ready to work in every business environment.</p>
                        <p class="text-sm">📈 Ask for M-pesa integration and e-cash drawer.</p>
                        <p class="text-sm">📈 Chat with our developers via WhatsApp.</p>
                    </div>
                    <div class="carousel-slide" style="display: none;">
                        <h1 class="text-2xl font-bold">How SHOP POS works</h1>
                        <p class="text-sm"> Our POS app will let you convert every product (goods & services) that your business offers into a barcode.</p>
                        <p class="text-sm"> That means that every item in a hotel menu and even re-packed products by retailers.</p>
                        <p class="text-sm"> Every time you make a sale you scan the barcode related to the product and the sale is recorded.</p>
                    </div>
                    <div class="carousel-slide" style="display: none;">
                        <h1 class="text-2xl font-bold">Suitable Businesses</h1>
                        <p class="text-sm">📈 Small and large wholesalers & retailers</p>
                        <p class="text-sm">📈 Spa, Beauty, Salon & Barber Shops</p>
                        <p class="text-sm">📈 Restaraunts, Hotels, Movies & Sports</p>
                        <p class="text-sm">📈 Garage & Carwash 📈 Wines & Spirits</p>
                        <p class="text-sm">📈 Hardware & Auto Spare shops</p>
                        <p class="text-sm">📈 Bookshops 📈 Butchery 📈 Boutiques</p>
                    </div>
                </div>
            </div>

        </div>
        <div class="flex items-center justify-center min-h-screen hero-bg flex-col"> <!-- Added flex-col class for vertical flex container -->
            <!-- Card 2 content -->
            <div class="custom-card2 mx-auto bg-white shadow-lg rounded-lg overflow-hidden mb-8" style="height: 65%;"> <!-- Added inline style for width -->
                <div class="p-6 text-center d-flex justify-content-center align-items-center">
                    <div class="carousel-slide1" style="display: none;">
                        <p1 class="text-sm">POS SCANNER</p1>
                        <a href="your_link_here">
                            <img src="https://firebasestorage.googleapis.com/v0/b/silent-owl-flight.appspot.com/o/b_scan.png?alt=media&token=214f65f1-80ff-47b8-af6b-61a77d469d28" width="180" height="180" alt="POS scanner">
                        </a>
                    </div>
                    <div class="carousel-slide1" style="display: block;">
                        <p1 class="text-sm">MONEYJAR POS SETUP</p1>
                        <a href="your_link_here">
                            <img src="https://firebasestorage.googleapis.com/v0/b/silent-owl-flight.appspot.com/o/holder.jpg?alt=media&token=494c75a7-94cb-46eb-be0c-22dcbd8f24ef" width="180" height="180" alt="POS Setup">
                        </a>
                    </div>
                    <div class="carousel-slide1" style="display: block;">
                        <p1 class="text-sm">MONEYJAR SCREENSHOTS</p1>
                        <a href="your_link_here">
                            <img src="https://firebasestorage.googleapis.com/v0/b/silent-owl-flight.appspot.com/o/1.png?alt=media&token=403287fe-de82-4fcc-a5ad-e3ea3790c0a5" width="350" height="300" alt="POS ScreenShots">
                        </a>
                    </div>
                    <div class="carousel-slide1" style="display: block;">
                        <p1 class="text-sm">MONEYJAR SCREENSHOTS</p1>
                        <a href="your_link_here">
                            <img src="https://firebasestorage.googleapis.com/v0/b/silent-owl-flight.appspot.com/o/2.png?alt=media&token=dfeadc3a-3906-48dc-9f93-9cddc04d9bd5" width="350" height="300" alt="POS ScreenShots">
                        </a>
                    </div>
                    <div class="carousel-slide1" style="display: block;">
                        <p1 class="text-sm">MONEYJAR SCREENSHOTS</p1>
                        <a href="your_link_here">
                            <img src="https://firebasestorage.googleapis.com/v0/b/silent-owl-flight.appspot.com/o/3.png?alt=media&token=00ab8213-f482-4186-8aac-3b49baa7fd4b" width="350" height="300" alt="POS ScreenShots">
                        </a>
                    </div>
                </div>
            </div>

            <div class="custom-card mx-auto bg-gold shadow-lg rounded-lg overflow-hidden mb-8"> <!-- Added mb-8 for some margin between the cards -->
                <div class="text-center">
                    <p1 class="text-sm">Watch Shop Moneyjar Demo</p1>
                </div>
                <div class="p-6 text-center d-flex justify-content-center align-items-center">
                    <!-- Add content for the second card here, similar to the first card -->
                    <iframe width="244" height="244" src="https://firebasestorage.googleapis.com/v0/b/silent-owl-flight.appspot.com/o/600%20(2).mp4?alt=media&token=e9eedba8-843a-49bc-9fb1-71eb87c9d978" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
                    </iframe>
                </div>
            </div>

        </div>
        <div class="flex items-center justify-center hero-bg flex-col" style="height: 180px;"> <!-- Added flex-col class for vertical flex container -->
            <!-- Card 2 content -->

            <div class="custom-card mx-auto bg-white shadow-lg rounded-lg overflow-hidden">
                <div class="container-bg py-4 px-6 container-text text-center">
                    <!-- Add content for the second card here, similar to the first card -->
                    <div class="social-icons">
                        <a href="https://facebook.com/LabdaTheTool"><i class="fab fa-facebook-f"></i></a>
                        <a href="https://instagram.com/labda_the_tool"><i class="fab fa-instagram"></i></a>
                        <a href="https://bit.ly/clinked-in"><i class="fab fa-linkedin-in"></i></a>
                        <a href="https://bit.ly/46zmsps"><i class="fab fa-whatsapp"></i></a>
                        <a href="https://twitter.com/Paul1Bundi"><i class="fab fa-xing"></i></a>
                    </div>
                </div>
            </div>

        <footer class="footer">
            <p>&copy; 2023 Moneyjar Solutions. All rights reserved.</p>
        </footer>
        <!-- Floating layout -->
        <div class="floating-layout1">
            <a href="https://bit.ly/M-Jar" class="cta-btn1">
                <i class="fab fa-google-play"></i>
            </a>
        </div>
        <!-- Floating layout -->
        <div class="floating-layout">
            <a href="https://bit.ly/46zmsps" class="cta-btn">
                <i class="fab fa-whatsapp"></i>
            </a>
        </div>
    </body>
    </html>
    """
    return html_text

@app.route('/forward_link')
def forward_link():
    link = "https://bit.ly/M-Jar"
    link2 = "https://bit.ly/46zzOCZ"
    whatsapp_url = f"https://api.whatsapp.com/send?text=Install this business app today.\n{requests.utils.quote(link)}.\n\nVisit Moneyjar Website:\n{requests.utils.quote(link2)}"
    return redirect(whatsapp_url)

@app.route('/send_newsletter', methods=['POST'])
def send_newsletter():
    name = request.form['name']
    email = request.form['email']

    message = EmailMessage()
    message['Subject'] = 'Moneyjar Information'
    message['From'] = 'moneyjarsolutions@gmail.com'
    message['To'] = email
    message.set_content(f'Dear {name},\n\nThank you for taking time to inquire. You will receive an email from someone soon!\n\nKind Regards\nMoneyjar Team')

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "moneyjarsolutions@gmail.com"
    smtp_password = "oxrflckpjennxxiw"

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(message)

    return landing_page()

@app.route('/Pricing')
def pricing_page():
    html_text = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Moneyjar App</title>
        <link rel="icon" href="https://firebasestorage.googleapis.com/v0/b/silent-owl-flight.appspot.com/o/MoneyJar%20copy.png?alt=media&token=6dc4f279-8ed1-4088-ad46-a79dc38d66be" type="image/png">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
        <style>
            .hero-bg {
                background-image: url('');
                background-size: cover;
                background-position: center;
                background-color: #393D47;
            }
            .form-input {
                border-color: #FFC107;
            }
            .form-input:focus {
                border-color: #FFD700;
                box-shadow: 0 0 0 2px rgba(255, 215, 0, 0.25);
            }
            .btn {
                background-color: #FFBF00;
                color: #ffffff;
                border-radius: 20px;
            }
            .btn:hover {
                background-color: #558b2f;
            }
            .container-bg {
                background-color: #4CAF50;
            }
            .container-text {
                color: #ffffff;
            }
            .floating-layout {
                position: fixed;
                bottom: 26%;
                right: 13px;
            }
            .floating-layout1 {
                position: fixed;
                bottom: 40%;
                right: 13px;
            }
            .cta-btn1 {
                display: flex;
                justify-content: center;
                align-items: center;
                width: 60px;
                height: 60px;
                border-radius: 50%;
                background-color: green;
                color: gold;
                text-decoration: none;
                animation: inflate-deflate 3.5s infinite ease-in-out;
            }

            .cta-btn1 i {
                font-size: 39px;
            }

            @keyframes inflate-deflate {
                0%, 100% {
                    transform: scale(.9);
                }

                50% {
                    transform: scale(1.3);
                }
            }
            .cta-btn {
                display: flex;
                justify-content: center;
                align-items: center;
                width: 60px;
                height: 60px;
                border-radius: 50%;
                background-color: green;
                color: white;
                text-decoration: none;
            }

            .cta-btn i {
                font-size: 39px;
            }


            .custom-card {
                width: 90%;
                margin: auto;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 1);
                border-radius: 20px;
                margin-top: 5vh;
            }
            .footer {
                width: 100%;
                position: fixed;
                bottom: 0;
                background-color: #f8f9fa;
                text-align: center;
                padding: 10px 0;
            }

            .footer p {
                margin: 0;
                color: #6c757d;
            }

        </style>

    </head>
    <body>
        <div class="flex items-center justify-center min-h-screen hero-bg flex-col"> <!-- Added flex-col class for vertical flex container -->
            <div class="custom-card mx-auto bg-white shadow-lg rounded-lg overflow-hidden mb-8"> <!-- Added mb-8 for some margin between the cards -->
                <div class="container-bg py-4 px-6 container-text text-center">
                    <!-- Add content for the second card here, similar to the first card -->
                    <h1 class="text-2xl font-bold">One Month + Free Trial</h1>
                    <p class="text-sm">USD 5/pm.</p>
                </div>
            </div>

            <!-- Card 2 content -->
            <div class="custom-card mx-auto bg-white shadow-lg rounded-lg overflow-hidden">
                <div class="container-bg py-4 px-6 container-text text-center">
                    <!-- Add content for the second card here, similar to the first card -->
                    <h1 class="text-2xl font-bold">Quaterly Subscription</h1>
                    <p class="text-sm">USD 15/=</p>
                </div>
            </div>
            <!-- Card 2 content -->
            <div class="custom-card mx-auto bg-white shadow-lg rounded-lg overflow-hidden">
                <div class="container-bg py-4 px-6 container-text text-center">
                    <!-- Add content for the second card here, similar to the first card -->
                    <h1 class="text-2xl font-bold">Yearly Subscription</h1>
                    <p class="text-sm">USD 60/=</p>
                </div>
            </div>
            <div class="custom-card mx-auto bg-white shadow-lg rounded-lg overflow-hidden">
                <div class="container-bg py-4 px-6 container-text text-center">
                    <!-- Add content for the second card here, similar to the first card -->
                    <form class="space-y-4">
                        <p class="text-sm">*Prices are subject to inflation.</p>
                        <div>
                            <a href="https://bit.ly/M-Jar" class="btn w-9/10 py-2 px-4 rounded-md font-medium">Install App</a>
                        </div>
                        <div>
                            <a href="/" class="btn w-9/10 py-2 px-4 rounded-md font-medium">Go Home</a>
                        </div>
                    </form>
                </div>
            </div>
        </div>
        <div class="text-center">
            <p class="text-sm">THIS WEBPAGE IS DESIGNED FOR HANDSET VIEW</p>
        </div>
        <div class="custom-card mx-auto bg-white shadow-lg rounded-lg overflow-hidden">
        </div>
        <div class="custom-card mx-auto bg-white shadow-lg rounded-lg overflow-hidden">
        </div>

        <footer class="footer">
            <p>&copy; 2023 Moneyjar Solutions. All rights reserved.</p>
        </footer>
        <!-- Floating layout -->
        <div class="floating-layout1">
            <a href="https://bit.ly/M-Jar" class="cta-btn1">
                <i class="fab fa-google-play"></i>
            </a>
        </div>
        <!-- Floating layout -->
        <div class="floating-layout">
            <a href="https://bit.ly/46zmsps" class="cta-btn">
                <i class="fab fa-whatsapp"></i>
            </a>
        </div>
    </body>
    </html>
    """
    return html_text

@app.route('/posta_lone', methods=['POST'])
def process_posta():
    if request.is_json:
        data = request.get_json()
        global posta_data
        new_data = {f"{data['Body']['stkCallback']['CheckoutRequestID']}": data}
        posta_data.update(new_data)
        # database.reference('EASTATE').child('Trasactions_Rent').update(new_data)
        # cursor = connection.cursor()
        # query = "INSERT INTO Mpesa (receipts) VALUES (%s)"  # Adjust the table and column names
        # cursor.execute(query, (new_data,))
        # connection.commit()
        # cursor.close()

        # Convert the dictionary to JSON
        json_data = json.dumps(new_data)

        # Set up the email parameters
        sender = "moneyjarsolutions@gmail.com"
        receiver = "juan16paul@gmail.com"
        subject = "POS Honey"
        message = MIMEText(json_data)
        message['Subject'] = subject
        message['From'] = sender
        message['To'] = receiver

        # Connect to the SMTP server and send the email
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_username = "moneyjarsolutions@gmail.com"
        smtp_password = "oxrflckpjennxxiw"

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(message)

        response = {'message': 'Data processed successfully'}
        return jsonify(response), 200
    else:
        error_response = {'message': 'Invalid JSON data'}
        return jsonify(error_response), 400

@app.route('/process_data', methods=['POST'])
def process_data():
    if request.is_json:
        data = request.get_json()
        global some_data
        new_data = {f"{data['Body']['stkCallback']['CheckoutRequestID']}": data}
        some_data.update(new_data)
        # database.reference('EASTATE').child('Trasactions_Rent').update(new_data)
        # cursor = connection.cursor()
        # query = "INSERT INTO Mpesa (receipts) VALUES (%s)"  # Adjust the table and column names
        # cursor.execute(query, (new_data,))
        # connection.commit()
        # cursor.close()

        # Convert the dictionary to JSON
        json_data = json.dumps(new_data)

        # Set up the email parameters
        sender = "moneyjarsolutions@gmail.com"
        receiver = "juan16paul@gmail.com"
        subject = "Money Inn"
        message = MIMEText(json_data)
        message['Subject'] = subject
        message['From'] = sender
        message['To'] = receiver

        # Connect to the SMTP server and send the email
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_username = "moneyjarsolutions@gmail.com"
        smtp_password = "oxrflckpjennxxiw"

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(message)

        response = {'message': 'Data processed successfully'}
        return jsonify(response), 200
    else:
        error_response = {'message': 'Invalid JSON data'}
        return jsonify(error_response), 400

@app.route('/the_results', methods=['POST'])
def handle_timeout():
    if request.is_json:
        data = request.get_json()
        global some_data_r
        # new_data = {f"{data['Body']['stkCallback']['CheckoutRequestID']}": data}
        some_data_r.update(data)

        # Convert the dictionary to JSON
        json_data = json.dumps(data)

        # Set up the email parameters
        sender = "moneyjarsolutions@gmail.com"
        receiver = "juan16paul@gmail.com"
        subject = "Many Results"
        message = MIMEText(json_data)
        message['Subject'] = subject
        message['From'] = sender
        message['To'] = receiver

        # Connect to the SMTP server and send the email
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_username = "moneyjarsolutions@gmail.com"
        smtp_password = "oxrflckpjennxxiw"

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(message)

        response = {'message': 'Data processed successfully'}
        return jsonify(response), 200
    else:
        error_response = {'message': 'Invalid JSON data'}
        return jsonify(error_response), 400

@app.route('/then_timeout', methods=['POST'])
def handle_results():
    if request.is_json:
        data = request.get_json()
        global some_data_
        new_data = {f"{data['Result']['ConversationID']}": data}
        some_data_.update(new_data)

        # Convert the dictionary to JSON
        json_data = json.dumps(new_data)

        # Set up the email parameters
        sender = "moneyjarsolutions@gmail.com"
        receiver = "juan16paul@gmail.com"
        subject = "Money Mite"
        message = MIMEText(json_data)
        message['Subject'] = subject
        message['From'] = sender
        message['To'] = receiver

        # Connect to the SMTP server and send the email
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_username = "moneyjarsolutions@gmail.com"
        smtp_password = "oxrflckpjennxxiw"

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(message)

        response = {'message': 'Data processed successfully'}
        return jsonify(response), 200
    else:
        error_response = {'message': 'Invalid JSON data'}
        return jsonify(error_response), 400

@app.route('/receive_some_data', methods=['POST'])
def receive_data():
    if request.is_json:
        data = request.get_json()
        global some_data
        # new_data = {f"{data['Body']['stkCallback']['CheckoutRequestID']}": data}
        some_data.update(data)
        response = {'message': 'Data processed successfully'}
        return jsonify(response), 200
    else:
        error_response = {'message': 'Invalid JSON data'}
        return jsonify(error_response), 400

@app.route('/do_something')
def do_something():
    global some_data
    return some_data

@app.route('/do_something_else')
def do_something_else():
    global some_data_
    return some_data_

@app.route('/do_something_else_completely')
def do_something_else_1():
    global some_data_r
    return some_data_r

@app.route('/pos_sales')
def do_somtn():
    global posta_data
    return posta_data

@app.route('/bundu')
def hom():
    return home()

@app.route('/bunduki')
def home():
    return redirect("https://bit.ly/M-Jar", code=302)

@app.errorhandler(404)
def page_not_found(error):
    return "404 - Page Not Found"

@app.errorhandler(500)
def internal_server_error(error):
    return "500 Server Error - Page Not Found"

@app.errorhandler(Exception)
def unhandled_exception(error):
    return "Exception Error - Page Not Found"


if __name__ == '__main__':
    app.run()
