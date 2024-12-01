# Heatmaps: Electric Charging Stations and Residents in Berlin

Electric mobility plays a crucial role in reducing greenhouse gas emissions. In recent years, the adoption and sales of electric vehicles have grown rapidly. However, the lack of electric charging stations in many regions remains a significant obstacle to further progress. Using geovisualization of various datasets for Berlin, we aim to analyze the demand for additional electric charging stations.

In general, areas with high population density and a low number of charging stations show a greater demand for additional infrastructure. Conversely, regions with a high proportion of single-family homes typically have lower demand, as homeowners often install private chargers on their properties. Unfortunately, comprehensive and freely available data on housing types is either unavailable or only partially accessible. As a result, this analysis will focus solely on population figures and the number of existing charging stations.

## Data Sources
### Charging Station Infrastructure by Postal Code

[Federal Network Agency - E-Mobility](https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/E-Mobilitaet/start.html)

Charging station list (XLSX, 8 MB)
Charging station list (CSV, 11 MB)

### Population by Postal Code

[Population Data by ZIP Code](https://www.suche-postleitzahl.org/downloads)
plz_einwohner.csv

## Final Result
The outcome of our analysis can be viewed [here](https://aseproject-9hercgjdmeyphdljtnqpm6.streamlit.app/).

---

## Table of Contents

1. [Setup](#setup)
2. [Code Documentation](#code-documentation)
3. [Interpretation](#interpretation)

---

## <a name="setup"/>Setup

### Prerequisites
install Python 3.10+ on your system, restart system


# -------------------------------
### Installation:
- Clone reposetory
- python -m venv .venv
- .venv\Scripts\activate.bat (Windows)
- source .venv/bin/activate (MacOS, Linux)
- pip install -r requirements.txt
- pip install spyder (or use vscode)


# -------------------------------
### Launch:

- .venv\Scripts\activate.bat (Windows)
- source .venv/bin/activate (MacOS, Linux)
- Start Streamlit App: streamlit run main.py

# -------------------------------
## <a name="code-documentation"/>Code Documentation

### Project Structure
. ├── src/ │ ├── main.py # Entry point of the application │ ├── utils.py # Helper functions │ ├── config.py # Configuration setup ├── docs/ # Documentation files ├── tests/ # Unit and integration tests └── README.txt # Project documentation

### Key Functions/Modules
- `main.py`: The main script to launch the application.
- `core/methods.py`: Contains helper functions such as data processing and validation.
- `config.py`: Handles configuration settings for the project.


# -------------------------------
## <a name="interpretation"/>Interpretation

### Usage Instructions
- Describe how to use your project and interpret its output. Provide examples:
- **Input:** What kind of data or parameters should be given.
- **Output:** What results to expect.

### Examples
#### Input Example:


