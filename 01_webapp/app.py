import web # Carga la libreria web.py

urls = (
    '/', 'hello'
    '/bye', 'Bye'
)
app = web.application(urls, globals())

class hello:
    def GET(self):
        
        return 'Hola, Web.py!'


class Bye:
    def GET(self):
        
        return 'Bye, Web.py!'

    app.run()

