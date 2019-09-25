import os
from flask import Flask, render_template, send_from_directory
from controller.alerts import alert_blueprint
from controller.stores import store_blueprint
from controller.users import user_blueprint


app = Flask(__name__)
app.secret_key = 'watanabeyouisbestgirl'
app.config.update(
    ADMIN=os.environ.get('ADMIN')
)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static', 'images'),
                               'favicon.ico', mimetype='image/png')


app.register_blueprint(alert_blueprint, url_prefix='/alerts')
app.register_blueprint(store_blueprint, url_prefix='/stores')
app.register_blueprint(user_blueprint, url_prefix='/users')


if __name__ == '__main__':
    app.run(debug=False)