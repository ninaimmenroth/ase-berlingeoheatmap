import pandas                        as pd
import geopandas                     as gpd
import core.HelperTools              as ht

import folium
# from folium.plugins import HeatMap
import streamlit as st
from streamlit_folium import folium_static
from branca.colormap import LinearColormap



def sort_by_plz_add_geometry(dfr, dfg, pdict):
    """
    Sorts a dataframe by postal codes (PLZ), merges it with geographical data, and 
    converts it into a GeoDataFrame with proper geometry.
    
    Args:
        dfr (pd.DataFrame): Main dataframe with data to process.
        dfg (pd.DataFrame): Dataframe containing geographical information.
        pdict (dict): Dictionary containing keys for column mapping (e.g., geocode column).
    
    Returns:
        gpd.GeoDataFrame: A GeoDataFrame with sorted and geometry-enriched data.
    """
    # Make copies of input dataframes to ensure the originals are not modified
    dframe = dfr.copy()
    df_geo = dfg.copy()

    # Sort the dataframe by 'PLZ' (postal code), reset the index, and ensure order consistency
    sorted_df = dframe\
        .sort_values(by='PLZ')\
        .reset_index(drop=True)\
        .sort_index()

    # Merge the sorted dataframe with geographical data on the key defined in 'pdict["geocode"]'
    # This adds geographical data (like coordinates or polygons) to the dataframe
    sorted_df2 = sorted_df.merge(df_geo, on=pdict["geocode"], how='left')

    # Drop rows where the 'geometry' column is missing, as these rows lack valid geographical data
    sorted_df3 = sorted_df2.dropna(subset=['geometry'])

    # Convert the 'geometry' column (stored as WKT strings) into GeoSeries objects
    sorted_df3['geometry'] = gpd.GeoSeries.from_wkt(sorted_df3['geometry'])

    # Convert the dataframe into a GeoDataFrame with the 'geometry' column as its geometry field
    ret = gpd.GeoDataFrame(sorted_df3, geometry='geometry')

    # Return the resulting GeoDataFrame
    return ret


# -----------------------------------------------------------------------------
@ht.timer
def preprop_lstat(dfr, dfg, pdict):
    """
    Preprocessing dataframe from Ladesaeulenregister.csv
    
    Args:
        dfr (pd.DataFrame): Main dataframe to preprocess.
        dfg (pd.DataFrame): Dataframe containing geographical information.
        pdict (dict): Dictionary to assist in data processing (likely for mappings).
    
    Returns:
        pd.DataFrame: Processed dataframe with applied filters and added geometry.
    """
    # Make copies of input dataframes to avoid modifying original data
    dframe = dfr.copy()
    df_geo = dfg.copy()

    # Select relevant columns and rename them for clarity and brevity
    dframe2 = dframe.loc[:, ['Postleitzahl', 'Bundesland', 'Breitengrad', 
                             'Längengrad', 'Nennleistung Ladeeinrichtung [kW]']]
    dframe2.rename(columns={"Nennleistung Ladeeinrichtung [kW]": "KW", 
                            "Postleitzahl": "PLZ"}, inplace=True)

    # Convert latitude and longitude to string type (preparing for text-based operations)
    dframe2['Breitengrad'] = dframe2['Breitengrad'].astype(str)
    dframe2['Längengrad'] = dframe2['Längengrad'].astype(str)

    # Replace commas with periods in latitude and longitude (converting to proper decimal format)
    dframe2['Breitengrad'] = dframe2['Breitengrad'].str.replace(',', '.')
    dframe2['Längengrad'] = dframe2['Längengrad'].str.replace(',', '.')

    # Apply filters:
    # - Only rows where the Bundesland (state) is "Berlin".
    # - Postal codes (PLZ) are within a specific range: 10115 < PLZ < 14200.
    dframe3 = dframe2[(dframe2["Bundesland"] == 'Berlin') & 
                      (dframe2["PLZ"] > 10115) &  
                      (dframe2["PLZ"] < 14200)]

    # Call an external function `sort_by_plz_add_geometry` to:
    # - Sort the filtered dataframe by PLZ.
    # - Integrate additional geometry data from `df_geo` based on mapping logic in `pdict`.
    ret = sort_by_plz_add_geometry(dframe3, df_geo, pdict)

    # Return the processed dataframe.
    return ret

    

# -----------------------------------------------------------------------------
@ht.timer
def count_plz_occurrences(df_lstat2):
    """Counts loading stations per PLZ"""
    # Group by PLZ and count occurrences, keeping geometry
    result_df = df_lstat2.groupby('PLZ').agg(
        Number=('PLZ', 'count'),
        geometry=('geometry', 'first')
    ).reset_index()
    
    return result_df
    
# -----------------------------------------------------------------------------
# @ht.timer
# def preprop_geb(dfr, pdict):
#     """Preprocessing dataframe from gebaeude.csv"""
#     dframe      = dfr.copy()
    
#     dframe2     = dframe .loc[:,['lag', 'bezbaw', 'geometry']]
#     dframe2.rename(columns      = {"bezbaw":"Gebaeudeart", "lag": "PLZ"}, inplace = True)
    
    
#     # Now, let's filter the DataFrame
#     dframe3 = dframe2[
#         dframe2['PLZ'].notna() &  # Remove NaN values
#         ~dframe2['PLZ'].astype(str).str.contains(',') &  # Remove entries with commas
#         (dframe2['PLZ'].astype(str).str.len() <= 5)  # Keep entries with 5 or fewer characters
#         ]
    
#     # Convert PLZ to numeric, coercing errors to NaN
#     dframe3['PLZ_numeric'] = pd.to_numeric(dframe3['PLZ'], errors='coerce')

#     # Filter for PLZ between 10000 and 14200
#     filtered_df = dframe3[
#         (dframe3['PLZ_numeric'] >= 10000) & 
#         (dframe3['PLZ_numeric'] <= 14200)
#     ]

#     # Drop the temporary numeric column
#     filtered_df2 = filtered_df.drop('PLZ_numeric', axis=1)
    
#     filtered_df3 = filtered_df2[filtered_df2['Gebaeudeart'].isin(['Freistehendes Einzelgebäude', 'Doppelhaushälfte'])]
    
#     filtered_df4 = (filtered_df3\
#                  .assign(PLZ=lambda x: pd.to_numeric(x['PLZ'], errors='coerce'))[['PLZ', 'Gebaeudeart', 'geometry']]
#                  .sort_values(by='PLZ')
#                  .reset_index(drop=True)
#                  )
    
#     ret                     = filtered_df4.dropna(subset=['geometry'])
        
#     return ret
    
# -----------------------------------------------------------------------------
@ht.timer
def preprop_resid(dfr, dfg, pdict):
    """Preprocessing dataframe from plz_einwohner.csv"""
    dframe                  = dfr.copy()
    df_geo                  = dfg.copy()    
    
    dframe2               	= dframe.loc[:,['plz', 'einwohner', 'lat', 'lon']]
    dframe2.rename(columns  = {"plz": "PLZ", "einwohner": "Einwohner", "lat": "Breitengrad", "lon": "Längengrad"}, inplace = True)

    # Convert to string
    dframe2['Breitengrad']  = dframe2['Breitengrad'].astype(str)
    dframe2['Längengrad']   = dframe2['Längengrad'].astype(str)

    # Now replace the commas with periods
    dframe2['Breitengrad']  = dframe2['Breitengrad'].str.replace(',', '.')
    dframe2['Längengrad']   = dframe2['Längengrad'].str.replace(',', '.')

    dframe3                 = dframe2[ 
                                            (dframe2["PLZ"] > 10000) &  
                                            (dframe2["PLZ"] < 14200)]
    
    ret = sort_by_plz_add_geometry(dframe3, df_geo, pdict)
    
    return ret


# -----------------------------------------------------------------------------
@ht.timer
def make_streamlit_electric_Charging_resid(dfr1, dfr2):
    """
    Creates a Streamlit app that displays heatmaps of electric charging stations 
    and resident density by postal code (PLZ) on an interactive map.
    
    Args:
        dfr1 (pd.DataFrame): DataFrame containing data for electric charging stations by PLZ.
            Columns include 'PLZ', 'Number' (number of charging stations), and 'geometry' (spatial data).
        dfr2 (pd.DataFrame): DataFrame containing data for resident numbers by PLZ.
            Columns include 'PLZ', 'Einwohner' (number of residents), and 'geometry' (spatial data).
    
    Returns:
        None. The function generates and displays an interactive Streamlit app.
    """
    
    # Create copies of the input DataFrames to avoid modifying the original data
    dframe1 = dfr1.copy()
    dframe2 = dfr2.copy()

    # Initialize Streamlit app title
    st.title('Heatmaps: Electric Charging Stations and Residents')

    # Add a radio button to allow users to select which dataset (layer) to visualize on the map
    # Options: Residents or Charging Stations
    layer_selection = st.radio("Select Layer", ("Residents", "Charging_Stations"))

    # Create an interactive Folium map centered on Berlin with an initial zoom level of 10
    m = folium.Map(location=[52.52, 13.40], zoom_start=10)

    if layer_selection == "Residents":
        # If the user selects "Residents," display a heatmap of resident density
        
        # Create a linear color map for the number of residents
        # Colors range from yellow (low density) to red (high density)
        color_map = LinearColormap(
            colors=['yellow', 'red'], 
            vmin=dframe2['Einwohner'].min(), 
            vmax=dframe2['Einwohner'].max()
        )

        # Add GeoJSON polygons to the map for each postal code area, styled based on resident density
        for idx, row in dframe2.iterrows():
            folium.GeoJson(
                row['geometry'],  # Spatial data for the postal code
                style_function=lambda x, color=color_map(row['Einwohner']): {
                    'fillColor': color,  # Color based on resident density
                    'color': 'black',   # Border color for the polygon
                    'weight': 1,        # Border thickness
                    'fillOpacity': 0.7  # Transparency level of the fill color
                },
                tooltip=f"PLZ: {row['PLZ']}, Einwohner: {row['Einwohner']}"  # Display PLZ and number of residents on hover
            ).add_to(m)

    else:
        # If the user selects "Charging_Stations," display a heatmap of charging station density
        
        # Create a linear color map for the number of charging stations
        # Colors range from yellow (low density) to red (high density)
        color_map = LinearColormap(
            colors=['yellow', 'red'], 
            vmin=dframe1['Number'].min(), 
            vmax=dframe1['Number'].max()
        )

        # Add GeoJSON polygons to the map for each postal code area, styled based on charging station density
        for idx, row in dframe1.iterrows():
            folium.GeoJson(
                row['geometry'],  # Spatial data for the postal code
                style_function=lambda x, color=color_map(row['Number']): {
                    'fillColor': color,  # Color based on charging station density
                    'color': 'black',   # Border color for the polygon
                    'weight': 1,        # Border thickness
                    'fillOpacity': 0.7  # Transparency level of the fill color
                },
                tooltip=f"PLZ: {row['PLZ']}, Number: {row['Number']}"  # Display PLZ and number of charging stations on hover
            ).add_to(m)

    # Add the color map legend to the Folium map
    color_map.add_to(m)

    # Render the Folium map within the Streamlit app
    folium_static(m, width=800, height=600)







