from .import bp as blog_bp
from flask import request, flash, redirect, url_for
from .models import Post
from app import db
from flask_login import current_user

@blog_bp.route('/post/create', methods=['POST'])
def create_post():
    if request.method == 'POST':
        try:
            data = request.form['status_update']
            p = Post(body=data, user_id=current_user.id)
            db.session.add(p)
            db.session.commit()
            flash('Post was created successfully', 'info')
        except:
            flash('There was an error creating your post. Try again.', 'danger')
    return redirect(url_for('main.home'))