from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import *
from components import sidebar, informations, table, dashboards

# =========  Layout  =========== #
content = html.Div(id="page-content")

app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            dcc.Location(id='url'),
            sidebar.layout
        ], sm=2),
        dbc.Col([
            content
        ], md=10)
    ])    
], fluid=True, className='cor-fundogr')

# ======  Callbacks  ====== #
@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def render_page(pathname):
    if pathname == '/' or pathname == '/introdução':
        return informations.layout
    if pathname == '/tabela':
        return table.layout
    if pathname == '/dashboards':
        return dashboards.layout

if __name__ == '__main__':
    app.run_server(debug=True,port=8080)
    #app.run_server(debug=False,port=8080,host='0.0.0.0')