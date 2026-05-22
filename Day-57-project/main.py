from flask import Flask, render_template
import requests


app = Flask(__name__)



@app.route('/blog')
def blog():
    url = "https://api.npoint.io/d9d18a1395c345165d7f"
    data = requests.get(url)
    all_posts = data.json()

    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:id>')
def post(id):
    url = "https://api.npoint.io/d9d18a1395c345165d7f"
    data = requests.get(url)
    all_posts = data.json()
    for blog_post in all_posts:
        if blog_post["id"] == id:
            requested_post = blog_post

    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
