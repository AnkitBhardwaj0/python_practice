import pandas as pd
import plotly.graph_objs as go
import numpy as np 
from dash import html
from dash import dcc
import dash


app=dash.Dash()
app.layout=html.H1(children="My First Dashboard",style={'color':'red','text-align':'center'})

if __name__ == "__main__":
     app.run()