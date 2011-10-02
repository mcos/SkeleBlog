import web

from models import Post, BlogPost

import os
from os import path

import datetime
t_globals = {
    'datestr': web.datestr
}

render = web.template.render('templates/', base='base', globals=t_globals)

class allPosts:
    def GET(self):
        posts = web.ctx.orm.query(Post).order_by(Post.id).all()
        return "\n".join(str(post.title) for post in posts)

class addPost:
    def GET(self):
        post = Post('Post', 'Post Body')
        web.ctx.orm.add(post)
        web.ctx.orm.commit()
        return post

class newPost:
    form = web.form.Form(
            web.form.Textbox('title', web.form.notnull, 
                size=30,
                description="Post title:"),
            web.form.Textarea('content', web.form.notnull, 
                rows=30, cols=80,
                description="Post content:"),
            web.form.Button('Post entry'),
        )

    def GET(self):
        form = self.form()
        return render.new(form)

    def POST(self):
        form = self.form()
        if not form.validates():
            return render.new(form)
        model.new_post(form.d.title, form.d.content)
        raise web.seeother('/')

class setup:
    def GET(self):
        #Here, we initialize a Sqlite Database and create the necessary tables
        models.setup()
        return 'Tables Created'

#File based controllers
class getAllPosts:
    def GET(self):
        """ Get all the folders at the root, then loop through each folder
            until we have a list of BlogPost objects built up from the
            files present in the folders """
        postspath = "./posts/"
        posts = recurseFolder(postspath)
        return "\n".join(str(post.title) + str(post.date) for post in posts)

class getYearPosts:
    def GET(self, year):
        return "Year:" + year

class getMonthPosts:
    def GET(self, year, month):
        return "Month:" + year + month

class getDayPosts:
    def GET(self, year, month, day):
        return "Day:" + year + month + day

def recurseFolder(path):
    posts = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in [f for f in filenames if f.endswith(".mkd")]:
            curpath = os.path.join(dirpath, filename)
            curfile = open(curpath, 'r')
            post = BlogPost(filename, curfile.read, datetime.datetime.now(),
                    curpath)
            posts.append(post)
    return posts
