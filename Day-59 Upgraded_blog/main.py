from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import requests 
import smtplib

load_dotenv()

my_email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

print(my_email)
print(password is None)
print(len(password) if password else "NO PASSWORD")


app = Flask(__name__)
msg_sent = False


@app.route("/")
def home():
    url = "https://api.npoint.io/278617d2001baf824074"
    data = requests.get(url)
    all_posts = data.json()
    return render_template("index.html", bg_image="home-bg.jpg", posts=all_posts)

@app.route("/about")
def about():
    return render_template("about.html", bg_image="about-bg.jpg")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", bg_image="contact-bg.jpg", msg_sent=True)
    return render_template("contact.html", bg_image="contact-bg.jpg", msg_sent=False)



@app.route('/post/<int:id>')
def post(id):
    url = "https://api.npoint.io/278617d2001baf824074"
    data = requests.get(url)
    all_posts = data.json()
    for blog_post in all_posts:
        if blog_post["id"] == id:
            requested_post = blog_post

    return render_template("post.html", post=requested_post, bg_image=requested_post["image_url"])

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)    
        connection.sendmail(
        from_addr=my_email,
        to_addrs="thawlinnoo7@gmail.com",
        msg=email_message
        )



if __name__ == "__main__":
    app.run(debug=True)

