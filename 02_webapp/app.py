import web # Carga la libreria web.py

urls = (
    '/', 'Index'
)
app = web.application(urls, globals())
render = web.template.render('views')

class index:
    def GET(self):
        return 'render.index()'

if __name__ == "__main__":
    app.run()