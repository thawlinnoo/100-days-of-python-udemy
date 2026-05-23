from flask import Flask, render_template
import requests 

app = Flask(__name__)


@app.route("/")
def home():
    url = "https://api.npoint.io/278617d2001baf824074"
    data = requests.get(url)
    all_posts = data.json()
    return render_template("index.html", bg_image="home-bg.jpg", posts=all_posts)

@app.route("/about")
def about():
    return render_template("about.html", bg_image="about-bg.jpg")

@app.route("/contact")
def contact():
    return render_template("contact.html", bg_image="contact-bg.jpg")

@app.route('/post/<int:id>')
def post(id):
    url = "https://api.npoint.io/278617d2001baf824074"
    data = requests.get(url)
    all_posts = data.json()
    for blog_post in all_posts:
        if blog_post["id"] == id:
            requested_post = blog_post

    return render_template("post.html", post=requested_post, bg_image=requested_post["image_url"])

if __name__ == "__main__":
    app.run(debug=True)

