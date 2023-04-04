from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/404')
def error():
    return render_template('404.html')

@app.route('/500')
def error():
    return render_template('500.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/add', methods=['POST'])
def submit_form():
   
    data = {
        'title': request.form['title'],
        'author': request.form['author'],
        'pages': request.form['pages']
    }
   
   
    data_list.append(data)
   
    return redirect('/')