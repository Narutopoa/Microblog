flask db init
flask db migrate -m "users table"
flask run --port 5001
flask db upgrade
flask db migrate -m "posts table"
app.app_context().push()
u = User(username='john', email='john@example.com')
db.session.add(u)
db.session.commit()
db.session.rollback()
query = sa.select(User)
users = db.session.scalars(query).all()
users
users = db.session.scalars(query)
for u in users:
    print(u.id, u.username)
u = db.session.get(User, 1)
p = Post(body='my first post!', author=u)
db.session.add(p)
db.session.commit()
query = sa.select(User).order_by(User.username.desc())
db.session.scalars(query).all()
query = sa.select(User).where(User.username.like('s%'))
db.session.scalars(query).all()
db.session.scalar()
flask db downgrade base
flask db downgrade head
from app import app, db
from app.models import User, Post
import sqlalchemy as sa
app.app_context().push()
flask shell