import os
import dash
from dash import html, dcc, no_update
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash import Input, Output, html, no_update
from app import app
from dash_bootstrap_templates import ThemeSwitchAIO

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd

df = pd.read_csv('airbnbJP.csv')
df = df.sort_values('estrelas', ascending=False)

cama = df.groupby('quantidade_cama').sum().reset_index()
name = df.groupby(['estrelas'])['quantidade_cama'].sum()
pnoite = df.groupby('preco_por_noite').sum().reset_index().head(5)

fig = px.bar(cama, x='quantidade_cama', y='preco_por_noite')
fig_pizza = px.pie(
    pnoite, values='quantidade_cama', 
    names='preco_por_noite', hole=.3)


layout = dbc.Col([
    dbc.Row([
        dbc.Col([
            html.Img(src='../assets/logo graph.png', className='logo-graph'),
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
            html.H1(html.I(' Análise dos Dados', className='subtitle-intro'), className='fa fa-long-arrow-left tag-text')
        ])
    ]),
    dbc.Row([ 
        dbc.Col([ 
            dbc.Card([
                html.Label('Filtros:', className='label-filters'),
                dbc.Card([
                html.Span('Quantidade de camas:'),
                dcc.Dropdown(
                    id='dropdown-bed', 
                    clearable=False,
                    style={'width':'100%'},
                    persistence=True,
                    persistence_type="session", 
                    multi=True, options=[{"label":x, "value":x} for x in df['quantidade_cama'].unique()], 
                    value=df['quantidade_cama'].unique(),
                    className='dropdown'
                ) 
            ], style={'padding':'5px'}, className='card-card'),
            dbc.Card([
                html.Span('Avaliação:'),
                dcc.Dropdown(
                    id='dropdown-star', 
                    clearable=False,
                    style={'width':'100%'},
                    persistence=True,
                    persistence_type="session", 
                    multi=True, options=[{"label":x, "value":x} for x in df['estrelas'].unique()], 
                    value=df['estrelas'].unique(),
                    className='dropdown'
                ) 
            ], style={'padding':'5px'}, className='card-card')
          ], className='container-cardFilter')
        ], width=3),
        dbc.Col([
            dbc.Card([ 
                dcc.Graph(id='graph1', figure=fig)
            ])
        ], width=5),
        dbc.Col([ 
            dbc.Card([
                dcc.Graph(id='graph2', figure=fig_pizza)
            ])
        ], width=4)
    ]),
    dbc.Row([ 
        dbc.Col([
        ])
    ])
])

# Callbacks
@app.callback([
    Output('graph1', 'figure'),
    Output('graph2', 'figure')
], [
        Input('dropdown-bed', 'value'),
        Input('dropdown-star', 'value')
    ]
)

def ind1(bed, star):
    df_geral = df[(df["estrelas"].isin(star)) & df['quantidade_cama'].isin(bed)]

    cama = df_geral.groupby('quantidade_cama').sum().reset_index()
    name = df_geral.groupby(['estrelas'])['quantidade_cama'].sum()
    pnoite = df_geral.groupby('preco_por_noite').sum().reset_index().head(5)

    fig = px.bar(cama, x='quantidade_cama', y='preco_por_noite')
    fig_pizza = px.pie(
        pnoite, values='quantidade_cama', 
        names='preco_por_noite', hole=.3)

    return fig, fig_pizza