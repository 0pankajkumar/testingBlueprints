from flask import Blueprint, render_template

cart_bp = Blueprint('cart_bp', __name__,
                    template_folder='templates',
                    static_folder='static', static_url_path='assets')


@cart_bp.route('/')
def list():
    return render_template('cart/list.html')


@cart_bp.route('/view/<int:product_id>')
def view(product_id):
    return render_template('cart/view.html')
