from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Here you can perform authentication or any other required actions
        return f"Logged in with email: {email}"
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
