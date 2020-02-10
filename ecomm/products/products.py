from flask import Blueprint, render_template

products_bp = Blueprint('products_bp', __name__,
                        template_folder='templates',
                        static_folder='static', static_url_path='assets')


def add(a, b):
    return a+b


@products_bp.route('/')
def listp():
    return render_template('products/list.html', sum="Yikes")


@products_bp.route('/view/<int:product_id>')
def viewp(product_id):
    return render_template('products/view.html')
