import streamlit as st
import requests, uuid, json
import pandas as pd
import numpy as np
import pydeck as pdk

st.title("Divvy Bikes - Chicago")


#
#df = pd.DataFrame(
#    np.random.randn(1000, 2) / [50, 50] + [41.9, -87.7],
#    columns=['lat', 'lon'])

json_data = 'https://azradls.blob.core.windows.net/bike-data/user/trusted-service-user/station_metrics_live/part-00000-de812749-e90b-4db8-b0e0-b6ae56e0367c-c000.json'


df = pd.DataFrame(pd.read_json(json_data, lines= True), columns = ['lat', 'lon','num_bikes_available', 'capacity', 'trend'])



tooltip = {
    "html": "<b>{num_bikes_available}</b> bikes available of <b>{capacity}</b><b>Average trip for current hour:  {trend}</b ",
    "style": {"background": "grey", "color": "white", "font-family": '"Helvetica Neue", Arial', "z-index": "10000"},
}


st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state=pdk.ViewState(
         latitude=41.87,
         longitude=-87.6,
         zoom=11,
         pitch=50,
     ),
     tooltip=tooltip,
     layers=[
         pdk.Layer(
            'ColumnLayer',
            data= df,
            get_position='[lon, lat]',
            radius=50,
            auto_highlight=True,
            get_elevation="capacity",
            get_fill_color=["num_bikes_available * 10", "num_bikes_available", "num_bikes_available * 10", 140],
            elevation_scale=10,
            elevation_range=[0, 30],
            pickable=True,
            extruded=True,            
         )
     ],
 ))

