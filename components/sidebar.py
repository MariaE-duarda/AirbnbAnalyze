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

popover_infor = "Informações principais sobre o projeto final."
popover_table = "Detalhamento dos dados usados para a análise Airbnb."
popover_dash = "Tela com os gráfico para a análise visual dos dados coletados."

layout = dbc.Col([
    html.Img(src='../assets/logo dash.png', className='title'),
    dbc.Nav([
        dbc.NavLink(
            html.I('ﾠINFORMAÇÕES', className='point-nav'), href='/', className='fa fa-bookmark class-color me-1', id="hover-target", n_clicks=0),
    ]),
    dbc.Popover(
        popover_infor,
        target="hover-target",
        body=True,
        trigger="hover",
    ),
    html.Hr(className='hr'),
    dbc.Nav([
        dbc.NavLink(
            html.I('ﾠDADOS', className='point-nav'), href='/tabela', className='fa fa-table class-color me-1', id="hover-target2", n_clicks=0),
    ]),
    dbc.Popover(
        popover_table,
        target="hover-target2",
        body=True,
        trigger="hover",
    ),
    html.Hr(className='hr'),
    dbc.Nav([
        dbc.NavLink(
            html.I('ﾠDASHBOARDS', className='point-nav'), href='/dashboards', className='fa fa-bar-chart class-color me-1', id="hover-target3", n_clicks=0)
    ]),
    dbc.Popover(
        popover_dash,
        target="hover-target3",
        body=True,
        trigger="hover",
    ),

    html.Img(src='../assets/living-room-animate.svg', className='img-found'),
    dbc.Button(id="open", n_clicks=0, className='btn-code fa fa-code'),
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Link para o código")),
        dbc.ModalBody("https://github.com/MariaE-duarda/AirbnbAnalyze"),
        dbc.ModalFooter(
        dbc.Button(
            "Fechar", id="close", className="ms-auto btn-fechar", n_clicks=0
        )),],
        id="modal",
        is_open=False,
        ),
], sm=20, lg=12, style={'height':'100vh', 'margin-top':'10px', 'margin':'0', 'margin-left':'-13px'}, className='sidebar')

# Callbacks
@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open