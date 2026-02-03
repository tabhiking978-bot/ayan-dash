
from flask import Flask, render_template

app = Flask(__name__)

apps = [
    {"name":"Token Server 1","image":"images/token_server_1.png","link":"http://fi8.bot-hosting.net:20448"},
    {"name":"Token Server 2","image":"images/token_server_2.png","link":"http://fi10.bot-hosting.net:20775/"},
    {"name":"Cookies Server","image":"images/cookies_server.png","link":"http://fi8.bot-hosting.net:20448"},
    {"name":"WhatsApp Loader","image":"images/whatsapp_loader.png","link":"https://fi10.bot-hosting.net:21949"}
]

@app.route("/")
def home():
    return render_template("index.html", apps=apps)

if __name__ == "__main__":
    app.run()
