import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import pandas as pd
import requests
from io import StringIO
import numpy as np
orig_url='https://drive.google.com/file/d/1FW9JcMoovgV3pEq4TJiqQ4DqSWC0JbfE/view'
file_id = orig_url.split('/')[-2]
dwn_url='https://drive.google.com/uc?export=download&id=' + file_id

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)



def data():
    sheet = client.open("Worldometers_Live").sheet1
    df = pd.DataFrame(sheet.get_all_values())
    df.columns = df.iloc[1]
    df = df.iloc[3:]
    df.reset_index(level=0, inplace=True)
    df = df.drop(columns=["index"], axis=1)
    col = df.columns
    df[col[0]] = df[col[0]].apply(lambda x: x.upper())
    return df

class calcData:
    def __init__(self):
        pass
    def GloBal_Total(self):
        sheet = client.open("Worldometers_Live").sheet1
        df = pd.DataFrame(sheet.get_all_values())
        df.columns = df.iloc[1]
        df = df.iloc[3:]
        df.reset_index(level=0, inplace=True)
        df = df.drop(columns=["index"], axis=1)
        col = df.columns
        df[col[0]] = df[col[0]].apply(lambda x: x.upper())
        #df = data()
        data1 = df.iloc[df.shape[0]-1]
        cases = []
        col = df.columns
        for item in col[1:10]:
            cases.append(item + ": " + data1[item] + "\n")
        mytext = "".join(cases)
        return mytext

    def country_data(self, country_name):
        my_country = country_name.upper()
        sheet = client.open("Worldometers_Live").sheet1
        df = pd.DataFrame(sheet.get_all_values())
        df.columns = df.iloc[1]
        df = df.iloc[3:]
        df.reset_index(level=0, inplace=True)
        df = df.drop(columns=["index"], axis=1)
        col = df.columns
        df[col[0]] = df[col[0]].apply(lambda x: x.upper())
        col = df.columns
        data1 = df[df[col[0]]==my_country]
        cases = []
        for item in col[1:]:
            if(data1[item].values[0]==""):
                cases.append(item + ": " + "0"+ "\n")
            else:

                cases.append(item + ": " + data1[item].values[0]+"\n")
        my_text = "".join(cases)

        return my_text
    def country_list(self):
        #url = requests.get(dwn_url).text
        #csv_raw = StringIO(url)
        #dfs = pd.read_csv(csv_raw)
        list_cntry = ['USA',	'Spain',	'Italy',	'France',	'Germany',	'UK',	'China',	'Iran',	'Turkey',	'Belgium',	'Netherlands',	'Canada',	'Switzerland',	'Brazil',	'Russia',	'Portugal',	'Austria',	'Israel',	'India',	'Ireland',	'Sweden',	'S. Korea',	'Peru',	'Chile',	'Japan',	'Ecuador',	'Poland',	'Romania',	'Norway',	'Denmark',	'Australia',	'Czechia',	'Pakistan',	'Saudi Arabia',	'Philippines',	'Mexico',	'Malaysia',	'UAE',	'Indonesia',	'Serbia',	'Panama',	'Qatar',	'Ukraine',	'Luxembourg',	'Dominican Republic',	'Belarus',	'Singapore',	'Finland',	'Colombia',	'Thailand',	'South Africa',	'Egypt',	'Argentina',	'Greece',	'Algeria',	'Moldova',	'Morocco',	'Iceland',	'Croatia',	'Bahrain',	'Hungary',	'Iraq',	'Estonia',	'New Zealand',	'Kuwait',	'Kazakhstan',	'Slovenia',	'Azerbaijan',	'Uzbekistan',	'Bosnia and Herzegovina',	'Lithuania',	'Armenia',	'Hong Kong',	'Bangladesh',	'North Macedonia',	'Cameroon',	'Slovakia',	'Oman',	'Cuba',	'Tunisia',	'Afghanistan',	'Bulgaria',	'Diamond Princess',	'Cyprus',	'Latvia',	'Andorra',	'Lebanon',	'Ivory Coast',	'Ghana',	'Costa Rica',	'Niger',	'Burkina Faso',	'Uruguay',	'Albania',	'Channel Islands',	'Kyrgyzstan',	'Honduras',	'Jordan',	'Taiwan',	'Malta',	'Réunion',	'San Marino',	'Djibouti',	'Guinea',	'Bolivia',	'Nigeria',	'Mauritius',	'Palestine',	'Senegal',	'Georgia',	'Montenegro',	'Vietnam',	'Isle of Man',	'DRC',	'Sri Lanka',	'Mayotte',	'Kenya',	'Venezuela',	'Faeroe Islands',	'Guatemala',	'Paraguay',	'Martinique',	'El Salvador',	'Guadeloupe',	'Mali',	'Brunei',	'Rwanda',	'Gibraltar',	'Cambodia',	'Trinidad and Tobago',	'Madagascar',	'Monaco',	'Aruba',	'French Guiana',	'Ethiopia',	'Liechtenstein',	'Togo',	'Jamaica',	'Barbados',	'Myanmar',	'Congo',	'Somalia',	'Liberia',	'Bermuda',	'Gabon',	'French Polynesia',	'Cayman Islands',	'Uganda',	'Tanzania',	'Sint Maarten',	'Bahamas',	'Guyana',	'Zambia',	'Macao',	'Equatorial Guinea',	'Haiti',	'Guinea-Bissau',	'Benin',	'Eritrea',	'Sudan',	'Saint Martin',	'Mongolia',	'Syria',	'Mozambique',	'Libya',	'Antigua and Barbuda',	'Chad',	'Maldives',	'Angola',	'Laos',	'Belize',	'New Caledonia',	'Zimbabwe',	'Malawi',	'Nepal',	'Dominica',	'Fiji',	'Namibia',	'Saint Lucia',	'Eswatini',	'Curaçao',	'Grenada',	'Botswana',	'Saint Kitts and Nevis',	'St. Vincent Grenadines',	'Cabo Verde',	'CAR',	'Falkland Islands',	'Greenland',	'Montserrat',	'Seychelles',	'Sierra Leone',	'Suriname',	'Turks and Caicos',	'MS Zaandam',	'Gambia',	'Nicaragua',	'Vatican City',	'Mauritania',	'St. Barth',	'Timor-Leste',	'Western Sahara',	'Burundi',	'Bhutan',	'Sao Tome and Principe',	'South Sudan',	'Anguilla',	'British Virgin Islands',	'Caribbean Netherlands',	'Papua New Guinea',	'Saint Pierre Miquelon',	'Yemen']
        text_cntry = ["Countries: \n"]
        for index, item in enumerate(list_cntry):
            text_cntry.append(str(index + 1)+ ": "+ item +"\n")
        message_cntry = " ".join(text_cntry)
        return message_cntry
