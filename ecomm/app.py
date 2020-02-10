from flask import Flask

from cart.cart import cart_bp
from products.products import products_bp

app = Flask(__name__)


app.register_blueprint(cart_bp, url_prefix='/cart')
app.register_blueprint(products_bp, url_prefix='/products')

app.config["DEBUG"] = True

if __name__ == "__main__":
    app.run(debug=True)
