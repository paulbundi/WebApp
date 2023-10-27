from flask import Flask, render_template_string, render_template

app = Flask(__name__)

@app.route('/')
def plot():
    # Define your CSS
    css = """
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }
    h1 {
        text-align: center;
    }
    """

    # Define your HTML
    html = """
    <html>
    <head>
        <style>
            {{css}}
        </style>
    </head>
    <body>
        <div>
            <h1>Hello, World!</h1>
            <p>This is a simple Flask application.</p>
            <button onclick="window.location.href='/plot'">Generate Plot</button>
        </div>
        <h1>Bar Graph</h1>
        <img src="data:image/png;base64,{{ plot_url }}">
    </body>
    </html>
    """

    return render_template_string(html, css=css)


@app.route('/plot')
def plot():
    # Data to plot
    labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    men_means = [20, 35, 30, 35, 27]
    
    # Create bar chart
    plt.bar(labels, men_means)
    
    # Convert plot to PNG image
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    
    # Convert PNG image to base64 encoding
    plot_url = urllib.parse.quote(base64.b64encode(img.read()).decode())
    
    return render_template('index.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
