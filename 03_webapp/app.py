import web # Carga la libreria web.py

urls = (
    '/(.*)', 'Index'
)
app = web.application(urls, globals())

class index:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hola, ' + name + '!'

if __name__ == "__main__":
    app.run()