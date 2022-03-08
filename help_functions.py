"""

Data Cleaning Codes

quick reference


"""
## libraries
import os
import shutil
from datetime import datetime
from datetime import timedelta
import time
import pathlib
import pandas as pd
import numpy as np
import zipfile
import glob
import win32com.client as client
#import win32api
#import ctypes


## importing and exporting
# importing
df = pd.read_excel(files, skiprows = 2)
df = pd.read_excel("Planned Numbers V3.xlsx",sheet_name = "In-Situ + MVT + LVT")
df = pd.read_csv("name.csv",skiprows = 5)

# exporting
file.to_excel(outputname +".xlsx", index = False)
file.to_csv(outputname + "_"+date+".csv",sep = "|", index = False)


## slicing rows/ columns
# rows

df = df[(df['caa'] > (date_td - timedelta(days=30))) & (df['caa'] < date_td)]
df_merge = df_merge.dropna(axis = 0, subset = ["Name"]) ##
df_merge = df_merge.dropna(axis = 0, subset = ["Name","Amount"])

df_unmatch = df_merge[df_merge['Name'].isnull()]

df = df[df["Type"].notna()]

df_unmatch = df_unmatch.drop_duplicates(subset = ["Vaccination Site"])  ## drop duplicates

frame_total = frame[frame["Type"]== "Total"] # selecting certain types

# columns

frame.drop(frame.iloc[:,8:10],axis = 1, inplace = True)

df = df.drop(['CAT 1', 'CAT 2','Balance Name','Assigned_brand'], axis=1,errors='ignore')

df = df.drop(["VC(s)",'module', 'calculate', "calculate2"], axis=1)

# combining columns
df['Gathered Name'] = df[['Vaccination Cluster', 'Community Hospital', 'Home Care Services (HCS)',
        'Hospice', 'National Specialist Centre (NSC)', 'Nursing Home',
        'Polyclinic', 'Private Acute Hospital (PAH)',
        'Public Health Preparedness Clinic (PHPC)',
          'Singapore Prison Service',
        'Senior Activity Centre (SAC)', 'MVT', 'MOM',
        'Senior Care Centre (SCC)', 'Vaccination Centre', 'SAF', 'MOE',
        'MOE MVT', 'LVT/HVT', 'Others', 'Others.1']].apply(lambda x: ','.join(x.dropna().astype(str)),axis=1) # add more if theres new category

df = df[['Vaccination Site', 'Cluster', 'Projected Insitu Dose 1',
   'Projected Insitu Dose 2', 'Projected Ext Dose 1',
   'Projected Ext Dose 2', 'Date of Appointment', 'vacc type']]


## pivoting dataset

# wide to long
df = pd.melt(df.reset_index(), id_vars=['Public Health Preparedness Clinic (PHPC)'], value_vars=['Tracking of Vaccine Expiring (Number of vials, Expiry date (DD/MM/YYYY))',



#long to wide
dosesplit = dosesplit.pivot_table(index = ['new group name','variable'] , columns = "Type", values = "value")
dosesplit = dosesplit.reset_index()



## changing variable type
# changing column to type integer
df[col] = df[col].astype(int)
df['OrderQuantity'] = df['OrderQuantity'].fillna(0).astype(int)

# changing column to type datatime
df['date_time']= pd.to_datetime(df['date_time'])
df_merge['Dates'] = pd.to_datetime(df_merge['Dates'], errors='coerce', dayfirst = True)


# changing column from datetime to string
new_df['caa'] = new_df['caa'].dt.strftime('%Y-%m-%d')




## merging dataset 

# merge by index
df = pd.merge(df, df1, left_index=True, right_index=True)

# outer merge by name
new_df = pd.merge(df, totalblock,  how='outer', left_on=['name','Day of appointment_datetime_local'], right_on = ['new group name','variable'])




## renaming columns
renaming_col = ["Count","Date","Sites"]
for col in range(len(df_merge.columns)):
    df_merge.rename(columns={ df_merge.columns[col]: renaming_col[col]}, inplace = True)
    
## creating new columns based on prev columns
df["module"] = np.arange(df.shape[0])
df["calculate"] = df["module"] % 4
df["calculate2"] = df["module"] // 4


## appending multiple dataframe
fullblockbk = []
fullblockbk.append(df)
frame = pd.concat(fullblockbk, axis=0, ignore_index=True)



## renaming variables in a column
frame['new group name'] = frame['new group name'].replace({'CHANGI T4': 'Changi Airport Terminal 4', 
                              'MARSILING CC': 'Marsiling Community Club', 
                              'WOODLANDS GALAXY CC': 'Woodlands Galaxy Community Club', 
                              'RCC1': 'Raffles City Convention Centre',
                              'TAMPINES EAST CC' : "Tampines East Community Centre",
                              'YUHUA CC' : "Yuhua Community Club",
                              'KOLAM AYER CC' : "Kolam Ayer Community Club",
                              'HONG KAH SECONDARY SCHOOL' : "Former Hong Kah Secondary School",
                              "BUONA VISTA CC":"Buona Vista Community Club"})



## groupby latest date
df['Timestamp']= pd.to_datetime(df['Timestamp'])
df = df.loc[df.groupby('Public Health Preparedness Clinic (PHPC)').Timestamp.idxmax()]

# seperate a column to 2 different columns
df[['Amount', 'Dates']] = df['batch'].str.split(';', 1, expand=True)

## replacing character in a column
df['Public Health Preparedness Clinic (PHPC)'] = df['Public Health Preparedness Clinic (PHPC)'].str.replace("_","").str.replace(","," ").str.replace("/","").str.replace("-","").str.replace("(","").str.replace(")","").str.lower().str.strip()

df_merge['Dates'] = df['Dates'].str.replace("-","/")

## replace NA with blank string
df_merge['Amount'].replace('', np.nan, inplace=True)



