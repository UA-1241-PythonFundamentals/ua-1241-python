from flask import Flask, url_for, redirect, request, render_template
from models import USERS
my_app = Flask(__name__)


@my_app.route('/')
def user_list():
    data =  [user.to_dict() for user in USERS]
    return render_template('user_list_template.html', user_data=data)


@my_app.route('/<user_id>')
def user_info(user_id):
    data =  {
        "id": user_id,
        "user": [user.to_dict() for user in USERS if str(user.user_id) == user_id],
    }
    print(data)
    return render_template('user_info_template.html', data=data)
    
    


if __name__ == '__main__':
    my_app.run(host="0.0.0.0", port=8080)