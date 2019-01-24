# url_for => Se puede usar desde cualquier parte de nuestra web (MIRAR LAYOUT.HTML)
# flash => Para mandar mensajes de alerta
# redirect ==> Para redirigir la página
from flask import Flask, render_template, url_for, flash, redirect

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


# Se puede exponer los métodos que están permitidos
@app.route("/register", methods=['GET', 'POST'])
def register():
    # Se crea una instancia del formulario de registro y se le pasa por el render
    form = RegistrationForm()

    # Comprueba estado de la validación en la acción del submit (true o false)
    if form.validate_on_submit():
        # Si el estado es correcto, se manda un mensaje, con el estado de bootstrap success
        flash(f'Account created for {form.username.data}!', 'success')
        # Si ha tenido éxito redirigimos
        return redirect(url_for('home'))

    return render_template("register.html", title="register", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    # Se crea una instancia del formulario de login y se le pasa por el render
    form = LoginForm()

    # Validación provisional de login por no tener BBDD
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            # Si el estado es correcto, se manda un mensaje, con el estado de bootstrap success
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful!. Please check username and password', 'danger')

    return render_template("login.html", title="login", form=form)


if __name__ == "__main__":
    app.run(debug=True)

