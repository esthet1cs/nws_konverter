## Abstract

Konverter - ein Programm zum Konvertieren tabellarisch erhobener Netzwerkdaten in ein für Gephi passendes Format.

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

#### Prototyp 1: all edges are equal
Konverter erzeugt aus einer Excel-Datei mit den angegebenen Tabellen zwei csv-Dateien -- nodes.csv, edges.csv -- für den einfachen Import in Gephi. Alle Nodes und alle Edges werden berücksichtigt. Redundante Edges sind in den csv-Dateien redundant aufgeführt, werden aber beim Import in Gephi automatisch gewichtet.



