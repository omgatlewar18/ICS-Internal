from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed to use sessions

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['guesses'] = 0

    message = ""
    if request.method == 'POST':
        guess = int(request.form['guess'])
        session['guesses'] += 1

        if guess < session['number']:
            message = "Too low! Try again."
        elif guess > session['number']:
            message = "Too high! Try again."
        else:
            message = f"🎉 Correct! You guessed it in {session['guesses']} tries."
            session.pop('number')  # Reset game
            session.pop('guesses')

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

