# url_for => Se puede usar desde cualquier parte de nuestra web (MIRAR LAYOUT.HTML)
from flask import Flask, render_template, url_for

# Se importa de forms las clases creadas
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# Configura la app
app.config['SECRET_KEY'] = "5555555555555555"

posts = [
    {
        "author": "Corey Schafer",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "April 20, 2018"
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "April 21, 2018"
    }
]


@app.route("/")
@app.route("/home")
def home():
    # Carga el template y le pasa como variable el dic posts
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register")
def register():
    # Se crea una instancia del formulario de registro y se le pasa por el render
    form = RegistrationForm()
    return render_template("register.html", title="register", form=form)


@app.route("/login")
def login():
    # Se crea una instancia del formulario de login y se le pasa por el render
    form = LoginForm()
    return render_template("login.html", title="login", form=form)


if __name__ == "__main__":
    app.run(debug=True)

