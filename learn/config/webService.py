import web
from config.DBO import conn


urls=(
    '/config','list_config'
)

app = web.application(urls,globals())



class list_config:


    def GET(self):
        c = conn()
        configList = c.getAllInfo()
        return configList


if __name__ == '__main__':
        app.run()