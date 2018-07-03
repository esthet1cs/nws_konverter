## Abstract

Konverter - ein Programm zum Konvertieren der tabellarisch erhobenen Netzwerkdaten in ein für Gephi passendes Format.

# Forschungsdesign

## Tabellenstruktur (Erhebungstabelle)

### Nodes (Knoten)

- Personen
- Institutionen
- Ereignisse
- Kunstwerke
- Publikationen (ausgelagert in PUMA)

### Relationen (Edges/Kanten)

- Person - Person
- Person - Institution
- Person - Ereignis
- Person - Kunstwerk
- Person - Publikation
- Publikation - Publikation
- Ereignis - Kunstwerk

=> personenzentriertes Netzwerk mit weiterem Fokus auf Ereignisse, Kunstwerke, Publikationen


## Konverter

### Prototyp 1: all edges are equal

- nodelist aus allen nodes; 
	- IDs umbenennen in Typ+ID

- edges
	- einzelne csv-dateien verarbeiten
	- IDs an die nodes gesamtliste anpassen
	- gesamtliste edges 
	- no weights, no attributes


