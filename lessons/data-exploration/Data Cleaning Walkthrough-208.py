## 4. Reading in the Data ##

import pandas as pd
data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {}
for f in data_files:
    d = pd.read_csv("schools/{0}".format(f))
    key_name = f.replace(".csv", "")
    data[key_name] = d

## 5. Exploring the SAT Data ##


print(data["sat_results"].head())

## 6. Exploring the Remaining Data ##


for k in data:
    print(data[k].head())

## 8. Reading in the Survey Data ##


all_survey = pd.read_csv("schools/survey_all.txt", delimiter="\t", encoding='windows-1252')
d75_survey = pd.read_csv("schools/survey_d75.txt", delimiter="\t", encoding='windows-1252')
survey = pd.concat([all_survey, d75_survey], axis=0)

print(survey.head())

## 9. Cleaning Up the Surveys ##

wanted_cols =["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11",]

survey['DBN']=survey['dbn']

survey = survey.loc[:,wanted_cols]
data["survey"] = survey

print(data["survey"].shape)

## 11. Inserting DBN Fields ##

import string

data['hs_directory']['DBN'] = data['hs_directory']['dbn']

data['class_size']['padded_csd']= data["class_size"]["CSD"].apply(lambda x: str(x).zfill(2) )

data['class_size']['DBN']=data['class_size']['padded_csd']+data['class_size']['SCHOOL CODE']
print(data['class_size']['DBN'].head())

## 12. Combining the SAT Scores ##

print(data['sat_results'].columns)
cols = ['SAT Math Avg. Score', 'SAT Critical Reading Avg. Score', 'SAT Writing Avg. Score']

for col in cols:
    data["sat_results"][col] = pd.to_numeric(data['sat_results'][col], errors='coerce')

data['sat_results']['sat_score']=data['sat_results'][cols[0]] + data['sat_results'][cols[1]] + data['sat_results'][cols[2]]

print(data['sat_results']['sat_score'].head())

## 13. Parsing Geographic Coordinates for Schools ##

import re

def get_coords(s):
    line = re.findall("\(.+\)", s)[0]
    line = re.sub('[(,)]', '', line)
    vals = line.split(" ")
    return vals[0]
    
data['hs_directory']['lat']=data['hs_directory']['Location 1'].apply(lambda x: get_coords(x) )

## 14. Extracting the Longitude ##

import re

def get_coords(s, coord):
    line = re.findall("\(.+\)", s)[0]
    line = re.sub('[(,)]', '', line)
    vals = line.split(" ")
    if coord=='lat': 
        return vals[0]
    else:
        return vals[1]
    
data['hs_directory']['lon']=data['hs_directory']['Location 1'].apply(lambda x: get_coords(x,'lon') )

data["hs_directory"]['lon'] = pd.to_numeric(data['hs_directory']['lon'], errors='coerce')
data["hs_directory"]['lat'] = pd.to_numeric(data['hs_directory']['lat'], errors='coerce')

print(data["hs_directory"].head)

