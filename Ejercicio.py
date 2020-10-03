import pandas as pd

data = pd.read_excel("D:/Curso Python/Sesión 3/RecursoDatos.xlsx")
heands = data.columns.values.tolist()

import plotly.express as px

colpatria = data[data["BANCO"] == "BANCO COLPATRIA"]

fig = px.histogram(colpatria, x="fecha_reporte", y="CLIENTES")
fig.show()