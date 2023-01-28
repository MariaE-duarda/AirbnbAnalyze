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


layout = dbc.Col([
    dbc.Row([
        dbc.Col([
            html.Img(src='../assets/logo scraping.png', className='logo-header'),
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
            html.H1(html.I(' Introdução', className='subtitle-intro'), className='fa fa-long-arrow-left tag-text')
        ])
    ]),
    dbc.Row([
        dbc.Col(
        html.Div(
            [
                html.H3("Web Scraping", className="display-6"),
                html.Hr(className="my-2"),
                html.P(
                    "Obtenção de dados de um certo programa a"
                    "partir de outro de forma a extrair conteúdo de alto valor que sejam, prioritariamente, de fácil interpretação a humanos."
                ),
                dbc.Button(html.A("Ler resumo", href='https://github.com/MariaE-duarda/Google-Colab/blob/main/WEB_SCRAPING.ipynb', className='btn-resumo'), outline=True, color="light", className='btn-btn'),
            ],
            className="h-80 p-3 rounded-3 cor-fundo",
        ),
        md=6, style={'margin-top':'10px'}, className='card-margin'
    ),

    dbc.Col(
        html.Div(
            [
                html.H3("Raspar dados significa...", className="display-6"),
                html.Hr(className="my-2"),
                html.P(
                    "Utilizar scripts, programas ou APIs para obter dados relevantes de sites, páginas, blogs, repositórios, ou qualquer outro lugar acessível por conectividade e requisição."
                ),
            ],
            className="h-100 p-3 rounded-3 cor-fundo",
        ),
        md=6, style={'margin-top':'10px', 'margin-left':'-10px'}, className='card-margin'
    ),

    ], style={'margin-left':'-15px'}),
    dbc.Card([ 
        dbc.Accordion([
            dbc.AccordionItem(
                [
                    html.P("A maioria das páginas da internet hoje são escritas em uma linguagem chamada HTML (HyperText Markup Language), desenvolvida no início da década de 1990 como a linguagem básica da internet. "),
                ],
                title="HTML 5",
                className='accordion-item',
                style={'background':'#131313', 'border-radius':'10px'}
            ),
            dbc.AccordionItem(
                [
                    html.P("Os navegadores da web interpretam o código HTML e transformam em uma “árvore”. Esta árvore caracteriza o modelo de objetos do documento, ou, formalmente, DOM (Document Object Model)."),
                ],
                title="Árvore DOM",
                className='accordion-item',
                style={'background':'#131313', 'border-radius':'10px'}
            ),
            dbc.AccordionItem(
                "APIs são parecidas com módulos, mas não oferecem meramente um conjunto de funções, mas sim um programa capaz de operar com muitos dados. Embora uma API possa funcionar localmente (offline), sua utilidade para raspagem de dados é melhor exibida quando se conecta a aplicativos da web (online).",
                title="API",
                style={'background':'#131313', 'border-radius':'10px'},
                className='accordion-item'
            ),
        ], className='accordion-button'
    )
    ], className='card card-margin'),
], className='color-found')
