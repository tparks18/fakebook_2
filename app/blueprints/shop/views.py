from .import bp as shop_bp
from flask import render_template, redirect, url_for, flash, request
from app.blueprints.shop.models import Product, Cart
from flask_login import current_user
from app import db


@shop_bp.route('/')
def home():
    context = {
        'products': Product.query.all()
    }
    return render_template('shop/home.html', **context)


@shop_bp.route('/product/add')
def add_product():
    try:
        _id = request.args.get('id')
        p = Product.query.get(_id)
        c = Cart(user_id=current_user.id, product_id=p.id)
        c.save()
        flash(f'{p.name} was added successfully', 'success')
    except Exception as error:
        print(error)
        flash(f'{p.name} was not added successfully. Try again.', 'danger')
    return redirect(url_for('shop.home'))


@shop_bp.route('/cart')
def cart():
    context = {}
    return render_template('shop/cart.html', **context)


@shop_bp.route('/cart/delete', methods=['GET', 'POST'])
def delete_product():
    p = Product.query.get(request.args.get('product_id'))
    cart = current_user.cart
    if request.method == "POST":
        res = request.form
        item_delete = int(res['delete_item'])

        counter = 0
        while counter < item_delete:
            try:
                # print(counter)
                _id = request.args.get('id')
                p = Product.query.get(request.args.get('product_id'))
                for i in cart:
                    if i.product_id == p.id and current_user.id == i.user_id:
                        cart_item = Cart.query.filter_by(
                            user_id=current_user.id).first()
                        db.session.delete(cart_item)
                        db.session.commit()
                        break
                flash(f'Product was removed successfully', 'success')
                counter += 1
            except Exception as error:
                print(error)
                flash(f'Product was not removed successfully', 'danger')
        return redirect(url_for('shop.cart'))


@shop_bp.route('/checkout')
def checkout():
    context = {}
    return render_template('shop/checkout.html', **context)
