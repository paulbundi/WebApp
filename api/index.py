from flask import Flask
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton

app = Flask(__name__)

@app.route('/')
def index():
    class DemoApp(MDApp):
        def build(self):
            return MDRectangleFlatButton(text='Hello, World!')

    DemoApp().run()

    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
