import os
from blog.app import app_freezer


def process_sitemap():
    os.rename('sitemap.xml', 'sitemap_unprocessed.xml')
    with open("sitemap_unprocessed.xml", "rt") as file_in:
        with open("sitemap.xml", "wt") as file_out:
            for line in file_in:
                file_out.write(line.replace('localhost', 'moosesloveforest.com'))
    os.remove('sitemap_unprocessed.xml')


if __name__ == '__main__':
    app_freezer.freeze()
    process_sitemap()
