# StrongsDicGermanHebrew

Strongs based dictionary Hebrew <-> German.

*Warning*: A very first draft.

## Basis 

Die Basis dieses Lexikons bildet das englischsprachige, gemeinfreie Strong-Wörterbuch von Crosswire. 

Die Einträge werden nach und nach von Hand überarbeitet (Hilfe ist dabei gerne gesehen). Grundlage der Überarbeitung bildet 

* Jens Grebner's Strong's Hebrew (Englisch)
* Gesenius von 1905 (https://archive.org/download/hebrischesund00gese/hebrischesund00gese.pdf)
* Weitere Lexika

```
[1] Gesenius, 1905
[2] Fohrer, 1997
```

Wie es aussehen könnte, kann man sich in den ersten paar Einträgen anschauen. Eine Kombination wird angestrebt. 

Die Einträge werden in einem Mediawiki gepflegt und können dort praktisch und von allen editiert werden. Unter ``scripts`` liegt liegt ein Pythonscript, dass diese Einträge automatisch konvertiert. Als einzigen Parameter verlangt das Skript einen Pfad zu einer import.cfg Datei mit folgenden Inhalten:

```
[SERVER]
site = <URL>
path = <toAPI>
login = <yes/no>
name = <loginname>
pw = <password>
[PATH]
filename = ../tei/strongshebr-german.tei.xml
```

## Zustand

Es ist noch viel Arbeit zu erledigen. Als erste Orientierung mag es reichen...
