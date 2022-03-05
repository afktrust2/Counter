from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = 'test key'

app.static_folder = 'static'

@app.route('/')
def index():
    if 'visits' not in session:
        session['visits'] = 1
    else:
        session['visits'] += 1
    return render_template("index.html")

@app.route('/destroy_session')
def hard_reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True, host='localhost', port=8000)