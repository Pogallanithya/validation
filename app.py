from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        age = request.form['age']
        gender = request.form['gender']

        # Do something with the data here (like save to database)
        return f"Registration successful! Welcome, {username}."

    return render_template('registration.html')

if __name__ == '__main__':
    app.run(debug=True)
