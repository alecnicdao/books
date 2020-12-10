from functools import wraps

from flask import ( Flask, render_template, request, redirect, url_for, flash, g, session )

from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///{}/{}".format(
    app.root_path, "books.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "b2de7FkqvkMyqzNFzxCkgnPKIGP6i4"

db = SQLAlchemy(app)

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.Text, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"), nullable=False)
    genre = db.relationship("Genre", backref=db.backref("Book", lazy=True))
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"), nullable=False)
    author = db.relationship("Author", backref=db.backref("Book", lazy=True))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def check_password(self, value):
        return check_password_hash(self.password, value)

db.create_all()

@app.before_request
def load_user():
    user_id = session.get("user_id")
    g.user = User.query.get(user_id) if user_id is not None else None

def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)

    return decorated_function

@app.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        error = None

        user = User.query.filter_by(username=username).first()

        if user is None:
            error = "Incorrect username."
        elif not user.check_password(password):
            error = "Incorrect password."

        if error is None:
            session.clear()
            session["user_id"] = user.id 
            return redirect(url_for("books"))

        flash(error)

    return render_template("admin/login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/register")
def register():
    user = User(username="admin", password=generate_password_hash("admin4book"))
    db.session.add(user)
    db.session.commit()

    return redirect(url_for("index"))

@app.route("/")
def index():
    books = Book.query.all()
    return render_template("index.html", books=books)

@app.route("/admin")
@app.route("/admin/books")
@login_required
def books():
    books = Book.query.all()
    return render_template("admin/books.html", books=books)

@app.route("/admin/create/book", methods=("GET", "POST"))
@login_required
def create_book():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        author_id = request.form["author_id"]
        genre_id = request.form["genre_id"]

        error = None

        if not name:
            error = "Name is required."

        if error is None:
            book = Book(
                name=name,
                description=description,
                author_id=author_id,
                genre_id=genre_id,
            )
            db.session.add(book)
            db.session.commit()

            return redirect(url_for("books"))

        flash(error)

    authors = Author.query.all()
    genres = Genre.query.all()
    return render_template("admin/book_form.html", authors=authors, genres=genres)

@app.route("/admin/edit/book/<id>", methods=("GET", "POST"))
@login_required
def edit_book(id):
    book = Book.query.get_or_404(id)

    if request.method == "POST":
        book.name = request.form["name"]
        book.description = request.form["description"]
        book.author_id = request.form["author_id"]
        book.genre_id = request.form["genre_id"]

        error = None

        if not request.form["name"]:
            error = "Name is required."

        if error is None:
            db.session.commit()

            return redirect(url_for("books"))

        flash(error)

    authors = Author.query.all()
    genres = Genre.query.all()
    return render_template(
        "admin/book_form.html",
        name=book.name,
        description=book.description,
        authors=authors,
        author_id=book.author_id,
        genres=genres,
        genre_id=book.genre_id,
    )

@app.route("/admin/delete/book/<id>")
@login_required
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()

    return redirect(url_for("books"))

@app.route("/admin/create/genre", methods=("GET", "POST"))
@login_required
def create_genre():
    if request.method == "POST":
        name = request.form["name"]

        error = None

        if not name:
            error = "Name is required."

        if error is None:
            genre = Genre(name=name)
            db.session.add(genre)
            db.session.commit()

            return redirect(url_for("books"))

        flash(error)

    return render_template("admin/genre_form.html")

@app.route("/admin/create/author", methods=("GET", "POST"))
@login_required
def create_author():
    if request.method == "POST":
        name = request.form["name"]

        error = None

        if not name:
            error = "Name is required."

        if error is None:
            author = Author(name=name)
            db.session.add(author)
            db.session.commit()

            return redirect(url_for("books"))

        flash(error)

    return render_template("admin/author_form.html")