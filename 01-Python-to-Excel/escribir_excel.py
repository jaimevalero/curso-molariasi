import pandas as pd

# Cargar datos de ejemplo
df = pd.read_excel("datos.xlsx")
df

usuarios = [{"Nombre": "Pepe1" , "Cargo" : "Director" },
      {"Nombre": "Jose" , "Cargo" : "Presidente" },
     ]
df_usuarios = pd.DataFrame(usuarios)

df_usuarios.to_excel("output.xlsx",
             sheet_name='Sheet_name_1',engine='openpyxl') 
