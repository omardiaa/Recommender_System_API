import pandas as pd
from datetime import date
import recommender_system  
import os 

if __name__ == "__main__":
    
    employee_index = "F" #A, B, F, N, P
    country_residence = "ES"
    sex = "V"
    age = 56
    province_name = "MADRID"
    
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