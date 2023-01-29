import os
import dash
from dash import html, dcc, no_update, Input, Output, dash_table
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from app import app
from dash_bootstrap_templates import ThemeSwitchAIO

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd

popover_down = "Fazer download da base de dados."

df = pd.read_csv('airbnbJP.csv')
df = df.sort_values('preco_por_noite', ascending=True)

layout = dbc.Col([
    dbc.Row([
        dbc.Col([
            html.Img(src='../assets/logo data.png', className='logo-data'),
            dbc.ButtonGroup(
            [dbc.Button("SCRAPING", color='danger', style={'border-radius':'5px'}, className='btn-g'), dbc.Button("TABLES", color='danger', style={'border-radius':'5px'}, className='btn-g'), dbc.Button("GRAPHS", color='danger', style={'border-radius':'5px'}, className='btn-g')],
            size="sm",
            className='btn-group'
        ),
            dbc.Spinner(color="danger", type="grow", spinnerClassName='spinner-header'),
        ], width=12)
    ], className='header-intro'),
    dbc.Row([ 
        dbc.Col([
            html.H1(html.I(' Dados trabalhados', className='subtitle-intro'), className='fa fa-long-arrow-left tag-text'),
            html.Br(),
            html.Button("Download CSV", id="btn_xlsx hover-target4", className='btn-download me-1',
            n_clicks=0),
            html.Button(html.A('Site usado', href='https://www.airbnb.com.br/s/Jo%C3%A3o-Pessoa--Brasil/homes?adults=1&place_id=ChIJsfXbGgborAcRI1xwKg981_0&refinement_paths%5B%5D=%2Fhomes', className='link-a'), className='btn-download'),
            dcc.Download(id="download-dataframe-xlsx"),  
            dbc.Popover(
            popover_down,
            target="hover-target4",
            body=True,
            trigger="hover",
        ), 
        ])
    ]),
    dbc.Row([ 
        dbc.Col([ 
            dash_table.DataTable(
                    data=df.to_dict('records'),
                    columns=[{'id': c, 'name': c} for c in df.columns],
                    style_header={ 'border': '1px solid #1a1a1a', 'background':'transparent', 'color':'rgb(212, 58, 58)', 'text-align':'center', 'font-weight':'400'},
                    filter_action='native',
                    style_cell={ 'border': '1px solid #1c1c1c', 'textAlign': 'left', 'background-color':'transparent', 'color':'white'},
                    page_size=5,     
                    style_data={
                        'whiteSpace': 'normal',
                        'height': 'auto', 'color':'rgb(204, 204, 204)'
                    }, id='tableData')
        ], style={'margin-top':'10px'}, className='card-margin')
    ])
])

# Callbacks
@app.callback(
    Output("download-dataframe-xlsx", "data"),
    Input("btn_xlsx", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_data_frame(df.to_excel, "airbnbJp.csv", sheet_name="Sheet_name_1")