import pandas as pd
from datetime import date
import recommender_system  
import os 
from flask import Flask, request

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/get_recommendations',methods = ['POST'])
def get_recommendations():
    employee_index = request.form.get("employee_index") or "F" #A, B, F, N, P
    sex = request.form.get('sex') or "V"
    country_residence = request.form.get("country_residence") or "ES"
    age = request.form.get("age") or 56
    province_name = request.form.get("province_name") or "MADRID"

    # return province_name
    df = pd.DataFrame([{
        
        'fecha_dato': "2016-06-28",
        'ncodpers': 15889,
        'ind_empleado': employee_index,
        'pais_residencia': country_residence,
        'sexo': sex ,
        'age': age,
        'fecha_alta': "1995-01-16",
        'ind_nuevo': '0',
        'antiguedad': 256,
        'indrel': '1',
       'ult_fec_cli_1t': "",
        'indrel_1mes': '1.0',
        'tiprel_1mes': "A",
        'indresi': "S",
        'indext': "N",
       'conyuemp': "N",
        'canal_entrada': "KAT",
        'indfall': "N",
        'tipodom': 1,
        'cod_prov': 28.0,
        'nomprov': province_name,
        'ind_actividad_cliente': '1',
        'renta': 326124.90,
        'segmento': "03 - UNIVERSITARIO"
    }])
    
    print(df)
    df.to_csv("Data/test_ver2.csv", index=True)
    print("running")
    
    recommender_system.main()
    
    products = pd.read_csv("sub_xgb_new.csv")
    print(products)
    
    return products["added_products"][0]

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000)
    