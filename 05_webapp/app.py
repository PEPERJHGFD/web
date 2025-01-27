import web
import json  
urls = (
    '/', 'Index'
)

app = web.application(urls, globals())


render = web.template.render('views/') 

class Index:
    def GET(self):
       
        return render.index()

    def POST(self):
        form = web.input() 
        nombre = form.nombre 
        email = form.email    

        response = { 
            "nombre": nombre,
            "email": email
        }

        web.header('Content-Type', 'application/json')  
        return json.dumps(response)  

if __name__ == "__main__":
    app.run()
