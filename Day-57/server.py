from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    current_year = datetime.now().year
    random_num = random.randint(1,10)
    return render_template("index.html", num=random_num, year=current_year)

@app.route("/guess/<name>")
def guess(name):
    gender_guess = requests.get("https://api.genderize.io", params={"name": name})
    age_guess = requests.get("https://api.agify.io", params={"name": name})

    gender = gender_guess.json()["gender"]
    age = age_guess.json()["age"]

    return render_template("guess.html", user_name=name, gender=gender,age=age)

@app.route("/blog/<num>")
def blog(num):
    print(num)
    url = "https://api.npoint.io/d9d18a1395c345165d7f"
    data = requests.get(url)
    all_posts = data.json()

    return render_template("blog.html", post=all_posts)




if __name__ == "__main__":
    app.run(debug=True)