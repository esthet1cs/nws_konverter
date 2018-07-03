#!/usr/bin/python3
# coding: utf-8


import os
import csv
import pandas as pd


## check if we have a folder for the nodes and edges data
if not os.path.exists('netzwerkdaten'):
    os.mkdir('netzwerkdaten')
    print('Datenordner netzwerkdaten wurde angelegt.')


# import the complete excel file

xls = pd.ExcelFile('netzwerk_stuttgarter_schule.xlsx')

# build the dataframes

df = pd.read_excel(xls, None)   # read all sheets into a dictionary

nodes_keys = [key for key in df.keys() if not 'Rel' in key]     # sort the keys into nodes and edges
edges_keys = [key for key in df.keys() if 'Rel' in key]     


# prepare minimal datapoints for use in gephi (nodes: ID, Label; edges: ID, Source, Target, Type)
#############################################

## helper functions

def change_id(ID, prefix):
    '''
    take the numeric ID and a prefix as input and return the ID plus the prefix for the node type
    '''
    return prefix + str(ID)


def export_nodes(dataframe, filename):
    '''
    export IDs, Labels and Type to csv
    '''
    dataframe.to_csv('netzwerkdaten/' + filename, columns=['ID', 'Label', 'Type'], index=False, quoting=csv.QUOTE_ALL)
    print('Export successful:', filename)


## nodes

# process and export all node sets individually

### Personen
dfp = df['Personen']                                    # checkout Personen-sheet
dfp = dfp.fillna('fehlt')                               # fill all empty fields with the value 'fehlt' (to prevent failure when exporting to csv)
dfp['Label'] = dfp['Vorname'] + ' ' + dfp['Nachname']   # Label = Vorname + Nachname
dfp['ID'] = dfp['ID'].apply(lambda x: change_id(x, 'p'))    # add Prefix to ID
dfp['Type'] = 'Person'
export_nodes(dfp, 'personen.csv')                       # export node data

### Institutionen
dfi = df['Institutionen']                               # checkout Institutionen-sheet
dfi = dfi.fillna('fehlt')                               # fill all empty fileds with the value 'fehlt'
dfi.rename(columns={'Name': 'Label'}, inplace=True)                   # rename column Name to Label
dfi['ID'] = dfi['ID'].apply(lambda x: change_id(x, 'i')) # add prefix
dfi['Type'] = 'Institution'
export_nodes(dfi, 'institutionen.csv')

### Ereignisse
dfe = df['Ereignisse']
dfe = dfe.fillna('fehlt')
dfe.rename(columns={'Name': 'Label'}, inplace=True)
dfe['ID'] = dfe['ID'].apply(lambda x: change_id(x, 'e'))
dfe['Type'] = 'Ereignis'
export_nodes(dfe, 'ereignisse.csv')

### Publikationen (have to be extracted from the edges-Tabel Person-Publikation for now)
dfpub = df['Rel_Pers-Pub'].copy()                       # checkout table
labels = pd.Series(dfpub['Publikation (PUMA-ID)'])    # extract the labels for the publications
labels = pd.Series(list(set(labels)))                   # remove duplicates
dfpub2 = pd.DataFrame()
dfpub2['Label'] = labels                                # construct a second dataframe from the extracted labels
dfpub2['ID'] = labels                                   
dfpub2['Type'] = 'Publikation'
export_nodes(dfpub2, 'publikationen.csv')

df_nodes = pd.concat([dfp, dfi, dfe, dfpub], ignore_index=True) # concatenate all nodes sets
export_nodes(df_nodes, 'nodes.csv')                             # write the full set to disk

## edges

# construct the dataframes, rename the columns, and concat the dataframes to one edges dataframe; export to file

### person -> person
dfpp = df['Rel_Personen'].copy()
dfpp.rename(columns={'Person1 (ID)': 'Source', 'Person2 (ID)': 'Target', 'Nachweis /Quelle': 'Nachweis'}, inplace=True)
dfpp['Source'] = dfpp['Source'].apply(lambda x: change_id(x, 'p'))
dfpp['Target'] = dfpp['Target'].apply(lambda x: change_id(x, 'p'))
dfpp = dfpp.fillna('fehlt')

### person -> institution
dfpi = df['Rel_Person-Institution'].copy()
dfpi.rename(columns={'Person (ID)': 'Source', 'Institution (ID)': 'Target', 'Nachweis/Quelle': 'Nachweis'}, inplace=True)
dfpi['Source'] = dfpi['Source'].apply(lambda x: change_id(x, 'p'))
dfpi['Target'] = dfpi['Target'].apply(lambda x: change_id(x, 'i'))
dfpi = dfpi.fillna('fehlt')

### person -> ereignis
dfpe = df['Rel_Pers-Ereignis'].copy()
dfpe.rename(columns={'Ereignis (ID)': 'Source', 'Person (ID)': 'Target', 'Nachweis/Quelle': 'Nachweis'}, inplace=True)
dfpe['Source'] = dfpe['Source'].apply(lambda x: change_id(x, 'e'))
dfpe['Target'] = dfpe['Target'].apply(lambda x: change_id(x, 'p'))
dfpe = dfpe.fillna('fehlt')

### person -> publikation
dfppu = df['Rel_Pers-Pub'].copy()
dfppu.rename(columns={'Person (ID)': 'Source', 'Publikation (PUMA-ID)': 'Target'}, inplace=True)
dfppu['Source'] = dfppu['Source'].apply(lambda x: change_id(x, 'p'))
dfppu = dfppu.fillna('fehlt')

### todo: 'Rel_Person-KW', 'Rel_Pub-Pub', 'Rel_Ereignis-KW' (derzeit noch ohne daten, 3.7.2018)

df_edges = pd.concat([dfpp, dfpe, dfpi, dfppu], ignore_index=True)
df_edges['Type'] = 'undirected'

df_edges.to_csv('netzwerkdaten/edges.csv', columns=['Source', 'Target', 'Type', 'Nachweis'], quoting=csv.QUOTE_ALL)


