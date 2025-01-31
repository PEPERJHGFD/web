import web
import requests
import json

urls = (
    '/', 'Index'
)

URI="https://bd-nube-d4ff8-default-rtdb.firebaseio.com/personas.json"

app = web.application(urls, globals())
render = web.template.render('views')

class Index:
    def GET(self):
        return render.index()

    def POST(self):
        form = web.input()
        nombre = form.nombre
        email = form.email
        data = {
                "nombre": nombre,
                "email": email 
                }
        response = requests.post(URI,json.dumps(data))
        return render.index()

if _name_ == "_main_":
    app.run()