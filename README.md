## Abstract

Konverter - ein Programm zum Konvertieren tabellarisch erhobener Netzwerkdaten in ein für Gephi passendes Format.

## Nutzung

Das Script erwartet im Arbeitsordner eine Datei namens `netzwerk_stuttgarter_schule.xlsx` mit den folgenden Tabellen:

- Personen
- Institutionen
- Ereignisse
- Rel_Personen
- Rel_Person-Institution
- Rel-Pers-Ereignis
- Rel-Pers-Pub 

Die Tabellen müssen so gelabelt sein wie im beigefügten Excel-Dokument. (In development: Verallgemeinerung der Funktionen für die Verarbeitung beliebiger Spaltenbezeichnungen.)

Konverter erzeugt aus einer Excel-Datei mit den angegebenen Tabellen zwei csv-Dateien -- nodes.csv, edges.csv -- für den einfachen Import in Gephi. Alle Nodes und alle Edges werden berücksichtigt. Redundante Edges sind in den csv-Dateien redundant aufgeführt, werden aber beim Import in Gephi automatisch gewichtet. Beim Durchlauf legt das Programm einen Ordner `netzwerkdaten` im Arbeitsverzeichnis an, dorthin werden die csv-Dateien geschrieben. Eventuell schon vorhandene Dateien werden überschrieben.


## Forschungsdesign

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



