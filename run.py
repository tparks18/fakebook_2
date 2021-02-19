from app import db, create_app, cli
from app.blueprints.auth.models import User
from app.blueprints.blog.models import  Post
from app.blueprints.shop.models import Product, Cart

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    return { 'db': db, 'User': User, 'Post': Post, 'Product': Product, 'Cart': Cart }