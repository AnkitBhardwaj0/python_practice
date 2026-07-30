from datetime import datetime

from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(200),
        nullable=False
    )

    desc = db.Column(
        db.String(500),
        nullable=False
    )

    date_created = db.Column(
        db.DateTime,
        default=datetime.now
    )

    def __repr__(self):
        return f"{self.sno} - {self.title}"


with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        title = request.form["title"]
        desc = request.form["description"]

        new_todo = Todo(
            title=title,
            desc=desc
        )

        db.session.add(new_todo)
        db.session.commit()

        return redirect("/")

    all_todo = Todo.query.all()

    return render_template(
        "index.html",
        all_todo=all_todo
    )


@app.route("/delete/<int:sno>")
def delete(sno):

    todo = db.get_or_404(
        Todo,
        sno
    )

    db.session.delete(todo)
    db.session.commit()

    return redirect("/")


if __name__ == "__main__":
    app.run(
        debug=True,
        port=8000
    )
