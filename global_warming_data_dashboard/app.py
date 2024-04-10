import plotly.express as px
import chart_studio.plotly as py
import plotly.graph_objs as go
import pandas as pd

# from plotly.offline import download_plotlyjs, init_notebook_mode, iplot, plot
# init_notebook_mode(connected = True)
avg_temp = pd.DataFrame()
fig = px.choropleth(avg_temp,locations='Country',locationmode='country names',color='AverageTemperature')
fig.update_layout(title='Choropleth Map of AverageTemperature ',template="plotly_dark")
fig.show()