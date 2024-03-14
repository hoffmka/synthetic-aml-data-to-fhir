import json
import os
import sys
import pandas as pd
from resources.patient import Patient

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Read ctab source data
df = pd.read_csv('src/synthetic_aml_data_ctab.csv', sep=";")
# Replace value for gender
df['SEX'].replace('m', 'male', inplace=True)
df['SEX'].replace('f', 'female', inplace=True)

###############################
# PATIENTS
###############################
# Create fhir resources "Patient" for each row in dataframe
for index, row in df.iterrows():
    patient = Patient(
        id=str(row['SUBJID']),
        gender=(row['SEX'])
        )
    # WRITE TO FILE
    # create folder "output/patient" if not exists
    if not os.path.exists(os.path.join(BASE_DIR, "output/patient")):
        os.makedirs(os.path.join(BASE_DIR, "output/patient"))
    with open(
        os.path.join(BASE_DIR, "output/patient/") + "Patient_" + str(row['SUBJID']) + ".json", "w",
    ) as f:
        json.dump(json.loads(patient.json()), f, indent=4)

###############################
# Observations
###############################
# get column names
col_list = df.columns.tolist()
# make wide to long (exclude column AGE, SEX)
df_melted = pd.melt(df, id_vars=["SUBJID"], value_vars=col_list[3:])
# get terminology mapping
df_terminology = pd.read_csv('src/terminology_mapping.csv', sep=";")
# merge data and terminology
df_merge = df_melted.merge(
        df_terminology, how="left", left_on="variable", right_on="Name"
    )

df_wbc=df_merge[df_merge['variable'] == "WBC"]

df_filtered = df_merge[df_merge['Concept_ID'].notna()]


# To do: extra observation for age