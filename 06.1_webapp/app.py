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
        num1 = float(form.get('num1', 0))  
        num2 = float(form.get('num2', 0))  
        operation = form.get('operation')  

    
        if operation == 'sumar':
            result = num1 + num2
        elif operation == 'restar':
            result = num1 - num2
        elif operation == 'multiplicar':
            result = num1 * num2
        elif operation == 'dividir':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: División entre 0 no permitida"
        else:
            result = "Operación no válida"

        response = { 
            "num1": num1,
            "num2": num2,
            "operation": operation,
            "result": result
        }

        web.header('Content-Type', 'application/json')  
        return json.dumps(response)  

if __name__ == "__main__":
    app.run()
