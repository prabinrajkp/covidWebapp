from api import data
import pandas as pd
from plotly.express import line as px_line
import plotly.graph_objs as go

def lineState(State,Feature):
    swave=data.daily()
    s=swave[swave.State.isin(State)]
    return px_line(s, x="Date", y=Feature,color='State',title='Comparison of '+Feature+' Cases in '+State[0]+' and '+State[1])


def pie_chart(State):
    df=data.vac_percent()
    pi=df[df.State.isin([State])].T
    pi.reset_index(inplace=True)
    pi.drop([0,1,2],inplace=True)
    pi.columns=['x','Total']
    x=pi['x'].tolist()
    y=pi['Total'].tolist()
    trace = go.Pie(labels=x,values=y)
    data_to_plot = [trace]
    layout_one = go.Layout(height=900, width=900,title=go.layout.Title(text='Vaccination status of '+State))
    pie_chart = go.Figure(data = data_to_plot,layout=layout_one)
    return pie_chart

def barChart():
    last37=data.daily()
    last37=last37.tail(37)
    last37.sort_values(by='Death_Rate',inplace=True,ascending=False)
    data_to_plot = [go.Bar(x =last37['State'],y =last37['Death_Rate'] ,orientation="v")]
    layout=go.Layout(height=900, width=900,title=go.layout.Title(text="Statewise Death Rates"))
    fig = go.Figure(data=data_to_plot,layout=layout)
    return fig
