import web
from setup import SkeleSetup

urls = (
        '/setup', 'setup'
        )

app = web.application(urls, globals())

class setup:
    def GET(self):
        #Here, we initialize a Sqlite Database and create the necessary tables
        return SkeleSetup()

if __name__ == "__main__": app.run()
