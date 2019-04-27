import datetime

from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from flask_sitemap import Sitemap

app = Flask(__name__)
app.config.from_pyfile('settings.py')
ext = Sitemap(app=app)
pages = FlatPages(app)
app_freezer = Freezer(app)


@app.route('/')
def home():
    posts = [page for page in pages if 'date' in page.meta]
    # Sort pages by date
    sorted_posts = sorted(
        posts, reverse=True,
        key=lambda page: datetime.datetime.strptime(page.meta['date'], '%d %B %Y')
    )
    return render_template('index.html', pages=sorted_posts, number_of_pages=len(sorted_posts))


@ext.register_generator
def home():
    yield 'home', {}


@app.route('/posts/<path:path>/')
def page(path):
    # Path is the filename of a page, without the file extension
    # e.g. "first-post"
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)


@ext.register_generator
def page():
    for p in pages:
        yield 'page', {'path': p.path}


@app.route('/about/')
def about():
    return render_template('about.html')


@ext.register_generator
def about():
    yield 'about', {}
