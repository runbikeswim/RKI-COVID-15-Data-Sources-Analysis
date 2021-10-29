import datetime as dt

# define constants that are used for formatting output 
 
INTEGER_FORMAT_STR = "{:,.0f}"
FOUR_DIGIT_YEAR_FORMAT_STR = "{:.0f}"
LOW_PRECISION_FLOAT_FORMAT_STR = "{:,.1f}"
MEDIUM_PRECISION_FLOAT_FORMAT_STR = "{:,.3f}"
HIGH_PRECISION_FLOAT_FORMAT_STR = "{:,.6f}" 
PERCENT_FORMAT_STR = "{:.2%}"
PER_THOUSAND_FORMATTER = lambda p: f"{p*1000:.2f}\u2030"
DATE_FORMATTER = lambda d: d.strftime("%m-%d")
DUMMY_FORMAT_STR = "{:}"

FORMAT_MAPPER = {"area": INTEGER_FORMAT_STR,
                 "category": DUMMY_FORMAT_STR,
                 "cases": INTEGER_FORMAT_STR,
                 "cases last 7 days": INTEGER_FORMAT_STR,
                 "cases per 100k": LOW_PRECISION_FLOAT_FORMAT_STR,
                 "cases per pop.": PERCENT_FORMAT_STR,
                 "cases last 7 days per 100k": LOW_PRECISION_FLOAT_FORMAT_STR,
                 "deaths": INTEGER_FORMAT_STR,
                 "deaths last 7 days": INTEGER_FORMAT_STR,
                 "deaths per 100k": HIGH_PRECISION_FLOAT_FORMAT_STR,
                 "deaths per pop.": PER_THOUSAND_FORMATTER,
                 "deaths last 7 days per 100k": MEDIUM_PRECISION_FLOAT_FORMAT_STR,
                 "death rate": PERCENT_FORMAT_STR,
                 "death rate last 7 days": PERCENT_FORMAT_STR,
                 "recovered": INTEGER_FORMAT_STR,
                 "recovered last 7 days": INTEGER_FORMAT_STR,
                 "recovered per 100k": LOW_PRECISION_FLOAT_FORMAT_STR,
                 "recovered per pop.": PERCENT_FORMAT_STR,
                 "recovered last 7 days per 100k": LOW_PRECISION_FLOAT_FORMAT_STR,
                 "district name": DUMMY_FORMAT_STR ,
                 "population": INTEGER_FORMAT_STR,
                 "state ID": DUMMY_FORMAT_STR,
                 "state name": DUMMY_FORMAT_STR ,
                 "state pop.": INTEGER_FORMAT_STR,
                 "update time": DATE_FORMATTER,
}

# URL for loading data as comma-seperated-data-file

RKI_ARCGIS_URL = "https://opendata.arcgis.com/datasets/917fc37a709542548cc3be077a786c17_0.csv"

# dictionary for renaming and harmonizing column names 

RKI_ARCGIS_COLUMN_NAME_MAPPER = {"cases7_per_100k": "cases last 7 days per 100k",
                                 "cases7_lk" : "cases last 7 days",
                                 "county": "district name",
                                 "cases_per_100k": "cases per 100k",
                                 "cases_per_population": "cases per pop.",
                                 "cases": "cases",
                                 "deaths": "deaths",
                                 "death_rate": "death rate",
                                 "death7_lk": "deaths last 7 days",
                                 "EWZ": "population",
                                 "BL_ID": "state ID",
                                 "EWZ_BL": "state pop.",
                                 "last_update": "update time",
                                 "RS": "district ID",
                                 "BEZ": "category",
                                 "GEN": "municipality name",
                                 "BL": "state name",
                                 "KFL": "area",
}

# define constants for the URLs that give access to data

RKI_GITHUB_REPOSITORY_URL = "https://github.com/robert-koch-institut/SARS-CoV-2_Infektionen_in_Deutschland"
RKI_GITHUB_RAW_DATA_BASE_URL = RKI_GITHUB_REPOSITORY_URL + "/raw/master"
RKI_GITHUB_ZENODO_REL_URL = "/.zenodo.json"
RKI_GITHUB_COVID_INFECTIONS_REL_URL = "/Aktuell_Deutschland_SarsCov2_Infektionen.csv"

# dictionary for renaming and harmonizing column names 

RKI_GITHUB_COLUMN_NAME_MAPPER = {
    "IdLandkreis": "district ID", 
    "Gemeindename": "municipality name", 
    "Flaeche": "area", 
    "EW_insgesamt": "population",
    "EW_maennlich": "population male", 
    "EW_weiblich" : "population female",
    "Altersgruppe": "age group", 
    "Geschlecht": "sex", 
    "Meldedatum": "reporting date", 
    "Refdatum": "reference date",
    "IstErkrankungsbeginn": "is start of desease", 
    "NeuerFall": "is new case", 
    "NeuerTodesfall": "is new death", 
    "NeuGenesen": "is new recovered",
    "AnzahlFall": "cases", 
    "AnzahlTodesfall": "deaths", 
    "AnzahlGenesen": "recovered",
}

unknown_converter = lambda s : "unknown" if s == "unbekannt" else s

RKI_GITHUB_VALUE_CONVERTERS = {
    "Altersgruppe": unknown_converter,
    "Geschlecht": lambda s: "F" if s == "W" else unknown_converter(s), 
}

# dictionary for setting the date type for some of the columns

RKI_GITHUB_COLUMN_TYPES_MAPPER = {
    "district ID": "int16",
    "reporting date": "datetime64", 
    "reference date": "datetime64",
    "is start of desease": "int32", 
    "is new case": "int8", 
    "is new death": "int8", 
    "is new recovered": "int8",
}

WHO_COLUMN_NAME_MAPPER = {
    "Date_reported": "reporting date", 
    "Country_code": "country code", 
    "Country": "country", 
    "WHO_region": "WHO region", 
    "New_cases": "cases", 
    "Cumulative_cases": "cumulative cases",  
    "New_deaths": "deaths", 
    "Cumulative_deaths": "cumulative deaths"
}

if __name__ == "__main__":
    pass