from flask import render_template, request, redirect, url_for
from app import app

@app.route("/", methods=["GET", "POST"])
def index():
    user_data = None
    if request.method == "POST":
        name = request.form.get("name")
        city = request.form.get("city")
        hobby = request.form.get("hobby")
        age = request.form.get("age")

        if name and city and hobby and age:
            user_data = {
                "name": name,
                "city": city,
                "hobby": hobby,
                "age": age
            }
            return render_template("index.html", user_data=user_data)

    return render_template("index.html", user_data=user_data)

if __name__ == "__main__":
    app.run(debug=True)