from flask import Flask, url_for, redirect, request

my_app = Flask(__name__)


@my_app.route('/')
def hello_world():
    return 'Hello, World!'



@my_app.route('/user')
def hello_user():
    return 'Hello, User!'

@my_app.route('/user/<name>')
def hello_user_name(name):
    # return f'Hello, user {name}!'
    if name == "admin":
        # redirect("/user/admin")
        return redirect(url_for("hello_admin"))
    return f'Hello, user {name}!'

@my_app.route('/user/id/<int:id>')
def hello_user_id(id):
    return f'Hello, user {id=}!'

@my_app.route('/admin',  methods=['GET', 'POST'])
def hello_admin():
    if request.method == "POST":
        return {"data":155}
    return f'Hello, Admin!'
    


if __name__ == '__main__':
    # my_app.run(host="0.0.0.0", port=80)
    # with my_app.test_request_context():
    #     print(url_for("hello_user"))
    #     print(url_for("hello_user_name", name="test"))
    #     print(url_for("hello_user_id", id=555))


    my_app.run(host="0.0.0.0", port=8080)