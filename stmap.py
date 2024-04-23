import folium
from folium import Choropleth
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import geopandas as gpd



st.set_page_config(layout="wide")



geojson_file = "Malaysia_MBB_Q4_2022.json"
gdf = gpd.read_file(geojson_file)
st.markdown("<h1 style='text-align: center; font-size: 40px;'>Streamlit Map</h1>", unsafe_allow_html=True)

m = folium.Map(location=[4.1093195, 109.45547499999998], tiles='openstreetmap', zoom_start=6)

d = gdf[gdf.avg_d_mbps <= 100].set_index("quadkey")

Choropleth(
    geo_data=d.geometry.__geo_interface__,
    data=d.avg_d_mbps,
    legend_name="Average Download speed",
    fill_color="RdPu",
    opacity=1.5,
    highlight=True,
    key_on="feature.id",
    ).add_to(m)
    
st_data = st_folium(m, width=1600, height = 500)