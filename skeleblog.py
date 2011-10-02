import web
import controllers
import models

urls = (
        '/', 'controllers.allPosts',
        '/add', 'controllers.addPost',
        '/new', 'controllers.newPost',
        '/setup', 'controllers.setup',
        '/get/?', 'controllers.getAllPosts',
        '/get/(\\w+)/?', 'controllers.getYearPosts',
        '/get/(\\w+)/(\\w+)/?', 'controllers.getMonthPosts',
        '/get/(\\w+)/(\\w+)/(\\w+)/?', 'controllers.getDayPosts'
        )

### Templates
app = web.application(urls, globals())

if __name__ == "__main__": app.run()
