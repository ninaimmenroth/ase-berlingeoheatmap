# Heatmaps: Electric Charging Stations and Residents in Berlin

Electric mobility plays a crucial role in reducing greenhouse gas emissions. In recent years, the adoption and sales of electric vehicles have grown rapidly. However, the lack of electric charging stations in many regions remains a significant obstacle to further progress. Using geovisualization of various datasets for Berlin, we aim to analyze the demand for additional electric charging stations.

In general, areas with high population density and a low number of charging stations show a greater demand for additional infrastructure. Conversely, regions with a high proportion of single-family homes typically have lower demand, as homeowners often install private chargers on their properties. Unfortunately, comprehensive and freely available data on housing types is either unavailable or only partially accessible. As a result, this analysis will focus solely on population figures and the number of existing charging stations.

## Team members
1. Azimy Zabihullah, 
2. Immenroth Nina, 907261
3. Khan Muhammad Kamran, 106089
4. Muzaffar Kiran, 

## Table of Contents

1. [Data Sources](#datasources)
2. [Final Result](#result)
3. [Setup](#setup)
4. [Code Documentation](#code-documentation)
5. [Interpretation](#interpretation)

---

## <a name="datasources">Data Sources</a>
### Charging Station Infrastructure by Postal Code

[Federal Network Agency - E-Mobility](https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/E-Mobilitaet/start.html)

Charging station list (XLSX, 8 MB)
Charging station list (CSV, 11 MB)

### Population by Postal Code

[Population Data by ZIP Code](https://www.suche-postleitzahl.org/downloads)
plz_einwohner.csv

## <a name="result">Final Result</a>
The outcome of our analysis can be viewed [here](https://aseproject-9hercgjdmeyphdljtnqpm6.streamlit.app/).

---

## <a name="setup">Setup</a>

### Prerequisites
install Python 3.10+ on your system, restart system

---
### Installation:
- Clone reposetory
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
├── data/ # Contains datasets used for analysis  
│ ├── plz_einwohner.csv # Population data per ZIP code  
│ └── charging_stations/ # Charging station data  
├── core/ # Source code for the project  
│ ├── methods.py # Methods to transform the data and generate heatmaps  
│ └── HelperTools.py # Helper functions  
├── config.py # Configuration settings for the project  
├── main.py # Main script to launch the application  
├── requirements.txt # Python dependencies  
└── README.md # Project documentation  

### Key Functions/Modules
- `main.py`: The main script to launch the application.
- `core/methods.py`: Contains helper functions such as data processing and validation.
- `config.py`: Handles configuration settings for the project.

---
## <a name="interpretation">Interpretation</a>

### Usage Instructions
The app shows two maps of Berlin, one highlighting the amounts of electric charging stations and one the amounts of inhabitants for each ZIP code. You can switch from one map to the other using the radio buttons under "Select Layer".

### Results


