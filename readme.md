# Heatmaps: Electric Charging Stations and Residents in Berlin

Electric mobility plays a crucial role in reducing greenhouse gas emissions. In recent years, the adoption and sales of electric vehicles have grown rapidly. However, the lack of electric charging stations in many regions remains a significant obstacle to further progress. Using geovisualization of various datasets for Berlin, we aim to analyze the demand for additional electric charging stations.

In general, areas with high population density and a low number of charging stations show a greater demand for additional infrastructure. Conversely, regions with a high proportion of single-family homes typically have lower demand, as homeowners often install private chargers on their properties. Unfortunately, comprehensive and freely available data on housing types is either unavailable or only partially accessible. As a result, this analysis will focus solely on population figures and the number of existing charging stations.

## Team members
1. Azimy Zabihullah, 945106
2. Immenroth Nina, 907261
3. Khan Muhammad Kamran, 106089
4. Muzaffar Kiran, 

---
## Table of Contents

1. [Data Sources](#datasources)
2. [Final Result](#result)
3. [Setup](#setup)
4. [Code Documentation](#code-documentation)
5. [Analysis](#interpretation)

---
## <a name="datasources">Data Sources</a>
### Charging Station Infrastructure by Postal Code

[Federal Network Agency - E-Mobility](https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/E-Mobilitaet/start.html)

Charging station list:  
Ladesaeulenregister.xlsx (XLSX, 8 MB)  
Ladesaeulenregister.csv (CSV, 11 MB)

### Population by Postal Code

[Population Data by ZIP Code](https://www.suche-postleitzahl.org/downloads)  
plz_einwohner.csv

---
## <a name="result">Final Result</a>
The streamlit app for our analysis can be viewed [here](https://aseproject-9hercgjdmeyphdljtnqpm6.streamlit.app/).

---
## <a name="setup">Setup</a>

### Prerequisites
install Python 3.10+ on your system, restart system

---
### Installation:
- Clone repository
- python -m venv .venv
- .venv\Scripts\activate.bat (Windows)
- source .venv/bin/activate (MacOS, Linux)
- pip install -r requirements.txt
- pip install spyder (or use vscode)

---
### Launch:

- .venv\Scripts\activate.bat (Windows)
- source .venv/bin/activate (MacOS, Linux)
- Start Streamlit App: streamlit run main.py

---
## <a name="code-documentation">Code Documentation</a>

### Project Structure
ase-berlingeoheatmap/  
├── data/                       --> Contains datasets used for analysis  
│ ├── plz_einwohner.csv         --> Population data per ZIP code  
│ └── Ladesaeulenregister.csv   --> Charging station data  
├── core/                       --> Source code for the project  
│ ├── methods.py                --> Methods to transform the data and generate heatmaps  
│ └── HelperTools.py            --> Helper functions  
├── config.py                   --> Configuration settings for the project  
├── main.py                     --> Main script to launch the application  
├── requirements.txt            --> Python dependencies  
└── README.md                   --> Project documentation  

### Key Functions/Modules
- `main.py`: The main script to launch the application and execute functions from methods.py with the correct data.
- `core/methods.py`: Contains helper functions such as data processing and creation of the streamlit app.
    - preprop_lstat(dfr, dfg, pdict): 
        - Preprocesses the dataframe from Ladesaeulenregister.csv and adds geographical information. 
        - Selects only the state Berlin with postal codes in range: 10115 < PLZ < 14200. 
        - Uses sort_by_plz_add_geometry(dfr, dfg, pdict)
    - sort_by_plz_add_geometry(dfr, dfg, pdict):
        - Sorts a dataframe by postal codes (PLZ), merges it with geographical data, and converts it into a GeoDataFrame with proper geometry.
    - count_plz_occurrences(df_lstat2):
        - Counts the charging stations for each postal code.
    - preprop_resid(dfr, dfg, pdict):
        - Preprocesses the dataframe from plz_einwohner.csv and adds geographical information. 
        - Selects only the state Berlin with postal codes in range: 10115 < PLZ < 14200. 
        - Uses sort_by_plz_add_geometry(dfr, dfg, pdict)
    - make_streamlit_electric_Charging_resid(dfr1, dfr2):
        - Creates a Streamlit app that displays heatmaps of electric charging stations and resident density by postal code (PLZ) on an interactive map.
        - Adds a radio button to allow users to select which dataset (layer) to visualize on the map.
        - Creates an interactive Folium map centered on Berlin with an initial zoom level of 10.
        - Creates a linear color map for the number of residents or electric car charging stations in each district of Berlin. Colors range from yellow (low density) to red (high density).
        - Adds polygon outlines for each district of Berlin.
        - Adds the color map legend to the Folium map.
- `config.py`: Handles configuration settings for the project, like the files to be used.

---
## <a name="interpretation">Analysis</a>

### Usage Instructions
The app shows two maps of Berlin, one highlighting the amounts of electric charging stations and one the amounts of inhabitants for each ZIP code. You can switch from one map to the other using the radio buttons under "Select Layer".

### Results
The analysis is based on two maps that visualize the density of electric car charging stations and population distribution across Berlin. The objective is to identify areas with potential demand for additional charging infrastructure by correlating population density with the existing distribution of charging stations.

#### Observations 

##### Residents - First Map
The first map highlights population density across Berlin. Higher population densities are shown in red, lower densities in yellow.
In general, population density appears to be higher in the central, northern and eastern districts of Berlin. Notably, Karow (postal code 13125) in the northeast stands out with a dark red color, indicating a particularly dense population. Similarly, areas in the southeast, such as Rudow (postal code 12353), also show elevated population density.

##### Charging Stations - Second Map
The second map illustrates the density of charging stations in Berlin, with regions color-coded to represent varying levels of station concentration.
Central urban areas of Berlin exhibit a higher concentration of charging stations, shown in red, indicating relatively high accessibility to charging infrastructure.
Areas depicted in yellow, primarily surrounding the city center and extending into peripheral regions, demonstrate a lower density of charging stations. However, some peripheral areas show a slight increase in charging station density.
Notably, Biesdorf (postal code 12683) and Mahlsdorf (postal code 12623), located in the eastern part of Berlin, stand out for having the highest density of charging stations.

#### Interpretation - Recommendations for Expanding Charging Infrastructure
Based on the observations of population density and the distribution of existing charging stations, several areas in Berlin have been identified as high-priority locations for infrastructure expansion. These areas demonstrate a combination of high population density and insufficient charging infrastructure, highlighting significant unmet demand.

The neighborhoods of Mitte, including postal codes 10119, 10178, and 10179, are densely populated and continue to attract a significant number of residents. While the current availability of charging stations in these areas is relatively higher compared to other parts of Berlin, there remains room for further expansion to accommodate the growing population and increasing demand for electric car charging infrastructure.

The central outskirts of Berlin, which appear orange on the population density map but yellow on the charging station map, represent regions where demand for charging stations remains unmet. Similarly, areas in the northeastern and southeastern peripheries, characterized by moderate population density but sparse station infrastructure, offer clear opportunities for expansion. Central Berlin, although equipped with a relatively higher concentration of charging stations due to its urban density, may still require additional infrastructure to meet the growing demand effectively.

In contrast, low-density areas with detached housing often rely on private charging solutions, leading to reduced public infrastructure requirements in these zones. However, certain specific locations stand out as immediate priorities. For instance, Northeast Berlin, particularly the postal code area 13125 (Karow), features a high population density but limited coverage of charging stations, indicating an urgent need for expansion. In Neukölln and Rudow, postal codes 12043 and 12353 respectively, the dense population is not adequately supported by the current low to moderate station density, making it an excellent candidate for new charging stations.

Eastern outer areas of Berlin also warrant attention, as these regions combine moderate to high population densities with modest charging station availability, suggesting significant potential for development. Only Biesdorf (postal code 12683) and Mahlsdorf (postal code 12623) seem to be well-equipped with charging stations so far. Addressing these gaps will enable Berlin to better align its charging infrastructure with the needs of its residents, supporting the growing adoption of electric vehicles and ensuring equitable access to charging facilities across the city.


