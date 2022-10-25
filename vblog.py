from flask import Flask
from flask import render_template

app = Flask(__name__)

posts = [{
    'author': 'Vinay Pursnani',
    'posted_on:': '10/24/2022',
    'blog_content': 'Portfolio using Flask'
},
    {
        'author': 'Varun Pursnani',
        'posted_on:': '10/25/2022',
        'blog_content': 'Checking future progress'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
