from flask import Flask, render_template, request, redirect, flash, url_for, session

from users import User

app=Flask(__name__)
db="users_schema"
@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def users():
    return render_template("users.html",users=User.get_all())


@app.route('/user/new')
def new():
    return render_template("new_user.html")

@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

def show_user(user_id):
    user = User.query.get(user_id)
    return render_template("read_user.html", user=user)

@app.route('/user/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully', 'success')
    return redirect(url_for('users'))

if __name__=="__main__":
    app.run(debug=True)