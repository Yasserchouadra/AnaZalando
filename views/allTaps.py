from dash import dcc,html
import dash_bootstrap_components as dbc
from dash import Input, Output,  html,State
from maindash import app


import time

from assets.additional_css import containerStyle
from assets.additional_css import TabContainerStyle
from assets.additional_css import tab_style
from assets.additional_css import tab_selected_style


from views.price import price
from views.brand import make_marque









def make_taps():
    return   html.Div(
                        [                        
                            dbc.Container(
                                style= containerStyle,
                                children=[
                                dcc.Tabs(
                                        id="tabs-example-graph", 
                                        value='tab-1-example-graph',
                                        style=  TabContainerStyle,
                                        vertical= True,
                                        children=[

                                                
                                                    dcc.Tab(
                                                                label='Best recommanded products',
                                                                style=tab_style, 
                                                                selected_style=tab_selected_style,
                                                                children=[
                                                                    dbc.Container(
                                                                        style = {
                                                                            "width":"1000px",
                                                                            'height': '1200px',
                                                                            'padding': '25px',

                                                                        },
                                                                        children=[
                                                                               price("best")
                                                                         ]
                                                                        ),
                                                                                
                                                                            
                                                                        ]
                                                            ),


                                                    dcc.Tab(
                                                                label='Cheapest products',
                                                                style=tab_style, 
                                                                selected_style=tab_selected_style,
                                                                children=[
                                                                    dbc.Container(
                                                                        style = {
                                                                            "width":"1000px",
                                                                            'height': '1200px',
                                                                            'padding': '25px',

                                                                        },
                                                                        children=[
                                                                               price("cheap")
                                                                         ]
                                                                        ),
                                                                                
                                                                            
                                                                        ]
                                                            ),


                                                    dcc.Tab(
                                                                label='Average price products',
                                                                style=tab_style, 
                                                                selected_style=tab_selected_style,
                                                                children=[
                                                                    dbc.Container(
                                                                        style = {
                                                                            "width":"1000px",
                                                                            'height': '1200px',
                                                                            'padding': '25px',

                                                                        },
                                                                        children=[
                                                                               price("average")
                                                                         ]
                                                                        ),
                                                                                
                                                                            
                                                                        ]
                                                            ),

                                                    dcc.Tab(
                                                                label='Top expensive products',
                                                                style=tab_style, 
                                                                selected_style=tab_selected_style,
                                                                children=[
                                                                    dbc.Container(
                                                                        style = {
                                                                            "width":"1000px",
                                                                            'height': '1200px',
                                                                            'padding': '25px',

                                                                        },
                                                                        children=[
                                                                               price("expensive")
                                                                         ]
                                                                        ),
                                                                                
                                                                            
                                                                        ]
                                                            ),                                                                                                                      

                                                    dcc.Tab(
                                                                label='Find your best Brand', 
                                                                style=tab_style, 
                                                                selected_style=tab_selected_style,
                                                                children=[
                                                                    dbc.Container(
                                                                        style = {
                                                                            "width":"1000px",
                                                                            'height': '1200px',
                                                                            'padding': '25px',

                                                                        },
                                                                        children=[
                                                                            make_marque()

                                                                        ]
                                                                        ),
                                                                                
                                                                            
                                                                                ]
                                                            ),

                                                
                                                            
                                                  


                                                
                                                
                                                ]
                                        ),
                                    
                                ]
                                    ),
                    

                        ])
    

