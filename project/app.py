from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup')
def signup():
    return render_template('signup_form.html')

@app.route('/employee')
def employee():
    return render_template('employee_reg.html')

@app.route('/productTable')
def productTable():
    return render_template('product_table.html')

@app.route('/eventTable')
def eventTable():
    return render_template('event_table.html')



if __name__ == '__main__':
    app.run(debug=True)
