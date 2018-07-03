# coding: utf-8
import pandas as pd
def change_id(ID, prefix):
    '''
    take the numeric ID as input and return the ID plus the prefix for the node type
    '''
    return prefix + str(ID)
change_id(20, 'P')
dfp = pd.read_csv('nodes_personen.csv')
dfp
def idp(ID):
    '''
    take the persons ID and change it to 'p' + str(ID)
    '''
    return 'p' + str(ID)
dfp['ID'] = dfp['ID'].apply(lambda x: 'p' + str(x))
dfp
dfp['Name'] = dfp['Vorname'] + ' ' + dfp['Nachname']
dfp
dfp.to_csv('netzwerkdaten/personen.csv', columns=['ID', 'Name'])
dfp.fillna('fehlt')
dfp['Name'] = dfp['Vorname'] + ' ' + dfp['Nachname']
dfp
dfp
dfp.fillna('fehlt')
dfp = dfp.fillna('fehlt')
dfp
dfp['Name'] = dfp['Vorname'] + ' ' + dfp['Nachname']
dfp
dfp.to_csv('netzwerkdaten/personen.csv', columns=['ID', 'Name'])
dfp.to_csv('netzwerkdaten/personen.csv', columns=['ID', 'Name'], index=False)
dfp.to_csv('netzwerkdaten/personen.csv', columns=['ID', 'Name'], index=False, quoting=csv.QUOTE_ALL)
dfp.to_csv('netzwerkdaten/personen.csv', columns=['ID', 'Name'], index=False, quoting='csv.QUOTE_ALL')
dfp.to_csv('netzwerkdaten/personen.csv', columns=['ID', 'Name'], index=False, quoting=QUOTE_ALL)
dfp.to_csv('netzwerkdaten/personen.csv', columns=['ID', 'Name'], index=False, quoting='QUOTE_ALL')
dfp.to_csv('netzwerkdaten/personen.csv', columns=['ID', 'Name'], index=False, quoting=csv.QUOTE_ALL)
import csv
dfp.to_csv('netzwerkdaten/personen.csv', columns=['ID', 'Name'], index=False, quoting=csv.QUOTE_ALL)
get_ipython().magic('ls ')
dfi = pd.read_csv('nodes_institutionen.csv')
dfi
dfi['ID'] = dfi['ID'].apply(lambda x: 'i' + str(x))
dfi
get_ipython().magic('ls ')
dfi.to_csv('netzwerkdaten/institutionen.csv', index=False, columns=['ID', 'Name'], quoting=csv.QUOTE_ALL)
get_ipython().magic('ls ')
dfe = pd.read_csv('nodes_ereignisse.csv')
dfe
dfe['ID'] = dfe['ID'].apply(lambda x: 'e' + str(x))
dfe.to_csv('netzwerkdaten/ereignisse.csv', index=False, columns=['ID', 'Name'], quoting=csv.QUOTE_ALL)
df_nodes = dfp['ID'] + dfp['Name']
df_nodes
df_nodes = pd.DataFrame
df_nodes
get_ipython().magic('ls ')
dfpp = df.read_csv('rel_personen.csv')
dfpp = pd.read_csv('rel_personen.csv')
dfpp
dfpp
df_edges = pd.DataFrame('Source', 'Target', 'Type')
dfpp
dfpp['Person1 (ID)'] = dfpp['Person1 (ID)'].apply(lambda x: 'p' + str(x))
dfpp['Person2 (ID)'] = dfpp['Person2 (ID)'].apply(lambda x: 'p' + str(x))
dfpp
dfpp.to_csv('netzwerkdaten/edges_person-person.csv', columns=['Person1 (ID)', 'Person2 (ID)', 'Direction'])
dfpp['Direction'] = e
dfpp['Direction'] = 'undirected'
dfpp
dfpp.to_csv('netzwerkdaten/edges_person-person.csv', columns=['Person1 (ID)', 'Person2 (ID)', 'Direction'], quoting=csv.QUOTE_ALL)
get_ipython().magic('ls ')
dfpe = pd.read_csv('rel_person-ereignis.csv')
dfpe
dfpe['Ereignis (ID)'] = dfpe['Ereignis (ID)'].apply(lambda x: 'e' + str(x))
dfpe['Person (ID)'] = dfpe['Person (ID)'].apply(lambda x: 'p' + str(x))
dfpe
dfpe['Direction'] = 'undirected'
dfpe
df_edges
dir()
dfpe
dfpp
# relations dataframes: change names of nodes to source, id (for use in gephi)
# make relations dataframes with the required columns only
# concatenate relations dataframes
# export concatenated relations dataframe to csv
dfpp
dfpp.tail()
get_ipython().magic('who')
dfpp = dfpp.rename(columns={'Person1 (ID)': 'Source', 'Person2 (ID)': 'Target', 'Direction': 'Type'})
dfpp.tail()
dfpe.tail()
dfpe.rename(columns={'Ereignis (ID)': 'Target', 'Person (ID)': 'Source', 'Direction': 'Type'}, inplace=True)
dfpe.tail()
dfpi
get_ipython().magic('who')
idp.tail()
get_ipython().magic('ls ')
dfpi = pd.read_csv('rel_person-institution.csv')
dfpi.tail()
dfpi['Person (ID)'] = dfpi['Person (ID)'].apply(lambda x: 'p' + str(x))
dfpi.tail()
dfpi['Institution (ID)'] = dfpi['Institution (ID')].apply(lambda x: 'i' + str(x))
dfpi['Institution (ID)'] = dfpi['Institution (ID)'].apply(lambda x: 'i' + str(x))
dfpi.rename(columns={'Person (ID)': 'Source', 'Institution (ID)': 'Target'}, inplace=True)
dfpi['Type'] = 'undirected'
dfpi.tail()
get_ipython().magic('ls ')
dfpp
get_ipython().magic('who')
get_ipython().magic('ls ')
dfppu = pd.read_csv('rel_person-publikation.csv')
dfppu.tail()
dfppu.head()
dfppu['Person (ID)'] = dfppu['Person (ID)'].apply(lambda x: 'p' + str(x))
dfppu.rename(columns={'Person (ID)': 'Source', 'Publikation (PUMA-ID)': 'Target'}, inplace=True)
dfppu['Type'] = 'directed'
dfppu.head()
get_ipython().magic('who')
dfpe.head()
dfpi.head()
dfpp.head()
dfppu.head()
get_ipython().magic('who')
df_edges = pd.concat([dfpp, dfpe, dfpi, dfppu])
df_edges.head()
df_edges.tail()
get_ipython().magic('ls ')
df_edges.to_csv('netzwerkdaten/edges_raw.csv', quoting=csv.QUOTE_ALL)
df_edges_reduced = df_edges['Source', 'Target', 'Type']
df_edges.tail()
df_edges
df_edges = pd.concat([dfpp, dfpe, dfpi, dfppu], ignore_index=True)
df_edges
df_edges.to_csv('netzwerkdaten/edges_raw.csv', quoting=csv.QUOTE_ALL)
df_edges_reduced = df_edges.copy()
df_edges_reduced.head()
for col in ['Bemerkungen', 'Funktion', 'Nachweis /Quelle', 'Nachweis Seitenzahl', 'Nachweis/Quelle', 'Relationstyp']:
    del df_edges_reduced[col]
    
df_edges_reduced.head()
del df_edges_reduced['Relationstyp']
df_edges_reduced.head()
del df_edges_reduced['Relationstyp ']
df_edges_reduced.head()
get_ipython().magic('ls netzwerkdaten')
df_edges_reduced.to_csv('netzwerkdaten/edges.csv', index=True, quoting=csv.QUOTE_ALL)
