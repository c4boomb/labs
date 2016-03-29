from spyre import server

import pandas as pd
import urllib2
import json

class StockExample(server.App):
    title = "Inputs"

    inputs = [{     "type":'dropdown',
                    "label": 'Index  ', 
                    "options" : [ {"label": "VCI", "value":"vci"},
                                  {"label": "TCI", "value":"tci"},
                                  {"label": "VHI", "value":"vhi"},],
                    "key": 'ticker', 
                    "action_id": "update_data"},

                {     "type":'dropdown',
                      "label": 'Region', 
                      "options" : [ {"label": "Vinnitsya", "value":"01"},
                                    {"label": "Volyn", "value":"02"},
                                    {"label": "Dnipropetrovsk", "value":"03"},
                                    {"label": "Donetsk", "value":"04"},
                                    {"label": "Zhytomyr", "value":"05"},
                                    {"label": "Transcarpathia", "value":"06"},
                                    {"label": "Zaporizhzhya", "value":"07"},
                                    {"label": "Ivano-Frankivsk", "value":"08"},
                                    {"label": "Kiev", "value":"09"},
                                    {"label": "Kirovohrad", "value":"10"},
                                    {"label": "Luhansk", "value":"11"},
                                    {"label": "Lviv", "value":"12"},
                                    {"label": "Mykolayiv", "value":"13"},
                                    {"label": "Odessa", "value":"14"},
                                    {"label": "Poltava", "value":"15"},
                                    {"label": "Rivne", "value":"16"},
                                    {"label": "Sumy", "value":"17"},
                                    {"label": "Ternopil", "value":"18"},
                                    {"label": "Kharkiv", "value":"19"},
                                    {"label": "Kherson", "value":"20"},
                                    {"label": "Khmelnytskyy", "value":"21"},
                                    {"label": "Cherkasy", "value":"22"},
                                    {"label": "Chernivtsi", "value":"23"},
                                    {"label": "Chernihiv", "value":"24"},
                                    {"label": "Crimea", "value":"25"},
                                    {"label": "Kiev City", "value":"26"},
                                    {"label": "Sevastopol", "value":"27"}],
                      "key": 'ticker', 
                      "action_id": "update_data"},

                { "input_type":"text",
                  "variable_name":"year",
                  "label": "Year",
                  "value":1981,
                  "action_id":"update_data"},

                { "type":'slider',
                  "label": 'First week', 
                  "min" : 1,"max" : 52,"value" : 35,
                  "key": 'first', 
                  "action_id": 'update_data'},

                { "type":'slider',
                  "label": 'Last week', 
                  "min" : 1,"max" : 52,"value" : 35,
                  "key": 'last', 
                  "action_id": 'update_data'},]


app = StockExample()
app.launch()