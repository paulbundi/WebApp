from flask import Flask, render_template_string

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
        </div>
    </body>
    </html>
    """

    return render_template_string(html, css=css)

if __name__ == '__main__':
    app.run(debug=True)
