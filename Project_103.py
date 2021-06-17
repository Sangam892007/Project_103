import pandas as pd
import plotly.express as pe

import1 = pd.read_csv("C:\Desktop\Coding\PYTHON\Copy+of+data+-+data.csv")

graph = pe.scatter(import1, x = "date", y = "cases",title = "Number of cases of covid in different countries", color="country", size = "cases", size_max=80)
graph.show()