from flask import Flask, request, render_template
from flask_restful import Api, Resource
import pandas as pd
import functions.creargrupoMD as md
 
 #Traer spreadsheet y convertirlo en df
# sheet_id = '1LB-L7Jbux8GjE7s_W9OPA38zf_xjvBdL6dPoEuXaM30'
# df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
# records = df.to_dict(orient='records')

# print(df)


##Nueva app Flask
app = Flask(__name__)
##Inicar objeto API desde Flask
api = Api(app)

## Rutas - paginas
@app.route('/')
def index():
    return render_template('index.html')

##API Requests
class All(Resource):

    def get(self):
        return md.dfdict


##Register API Resources
api.add_resource(All, '/api/')

if __name__ == "__main__":
    app.run(host = '127.0.0.1', port = 5000, debug = True)





##––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# @app.route("/webhook/monday", methods=['POST'])
# def additemsmo():
#     if request.method == 'POST':
#         res = request.get_json()
#         print(res)
#         md.crearProyecto(res)
        
#     return {"statusCode":200}

# if __name__ == "__main__":
#     app.run(debug=True) # Quitar el host en el deploy