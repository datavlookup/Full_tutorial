from flask import *


app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    first_name = 'Orhan'
    stuff = 'This is <strong> bold </strong> '
    favorite_pizza = ['paperroni', 'mushrooms', 'Cheese', 'pizza', 'Salami']
        
    return render_template('index.html', first_name=first_name, stuff=stuff, favorite_pizza=favorite_pizza)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)

# Custom Error Pages

#Invalid Page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'),500


if __name__ == '__main__':
    app.run(debug=True)