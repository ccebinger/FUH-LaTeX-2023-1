# FUH-LaTeX-2023-1

Materialien für den ersten LaTeX-Kurs 2023 an der Fernuni Hagen

Die Materialien können frei von jedermann genutzt und verändert werden, entsprechende Hinweise auf meine Urheberschaft werden aber gern gesehen.

## Wie kommt man an die Materialien?

git installieren und dann auf der Kommandozeile

git clone https://github.com/UweZiegenhagen/FUH-LaTeX-2023-1.git

Updates holt man wie folgt, lokal geänderte Dateien werden dabei überschrieben!

git fetch --all
git reset --hard origin/main

In den nächsten Monaten wird das Repository noch öffentlich zugänglich sein, 
irgendwann werde ich es auf privat setzen. Ihr könnt es gern forken, aber dann
vorzugsweise in ein privates Repo da ich gern Wildwuchs verhindern möchte.

## Der Kurs

Der Kurs findet an mehreren Samstagen online statt, als Plattform nutzen wir BigBlueButton von senfcall.de, der Link wird vorab per E-Mail versandt.

* **Tag 1**: 22.04.2023
* **Tag 2**: 29.04.2023, Beginn 9:00 Uhr
* **Tag 3**: ~~06.05.2023~~ an diesem Tag kann ich leider nicht tagsüber, wir werden daher a) die Zeit auf die anderen Termine verteilen oder b) am ersten Tag einen Ausweichtermin festlegen
* **Tag 4**: ~~20.05.2023~~ 27.05.2023, Beginn: 09:00 Uhr
* **Tag 5**: 03.06.2023 von 9:00 bis 11:00 Uhr

Jeweils grundsätzlich von 10:00 Uhr bis 12:00 Uhr und 13:00 Uhr bis 15:00 Uhr, in Summe also 16 Stunden.

## Was wird benötigt

* Ein Rechner (Laptop, Desktop) mit Windows, MacOS oder Linux
* TeX Live 2023 herunterladen und installieren von tug.org/texlive. Eine Anleitung (für TeX Live 2022, es hat sich aber fast nichts geändert) habe ich unter https://www.youtube.com/watch?v=k9KhuZz7k-Q veröffentlicht.
* Wenn ihr unter Linux arbeitet: Bitte nicht aus den Distributionsquellen nehmen, sondern auch von tug.org installieren. Das TeX Live in den Distributionen ist oft nicht aktuell. 
* Mac-User installieren bitte MacTeX (auch auf der tug.org Seite frei verfügbar)
* Ein Editor zur Bearbeitung der TeX-Dateien: TeX Live bringt für Mac und Windows TeXworks mit, einen guten und einfach zu bedienenden Editor, den ich gern benutze. TeX Studio und Visual Studio Code (mit der ``LaTeX Workshop`` Erweiterung von James Yu) kann ich ebenfalls sehr empfehlen.
* Grundkenntnisse von Git bzw. Github sind nicht verkehrt, da alle meine Dateien im Github liegen.

## Kursinhalte

Die Kursinhalte sind flexibel und orientieren sich am Bedarf und Tempo der Teilnehmerinnen und Teilnehmer, mit dem folgenden Ablauf plane ich:

### Tag 1 - Grundlagen

* Vorstellung der Beteiligten, wer bin ich und wer seid ihr, was sind eure Lernziele?
* Historie von TeX und LaTeX
* Check der Umgebungen bzw. Installationen mittels "Hallo \LaTeX" Dokument
* Klassen, Pakete, Umgebungen und Befehle
* Warum man article, report und book nicht unbedingt nutzen sollte -- die KOMA-Klassen
* Strukturierte Dokumente, ``\chapter``, ``\section`` & Co, Inhaltverzeichnisse
* Referenzen mit ``\label`` und ``\ref``
* Float-Objekte in LaTeX
* Einfache Bilder einbetten, Bilderverzeichnisse
* Einfacher Tabellensatz und Tabellenverzeichnisse
* Mehr zum Bilder einbetten: ``subfigure`` und ``subcaption`` 


### Tag 2 - Tabellen, Mathematik, und mehr

* Vorstellung von DANTE e.V.
* Wiederholung vom 1. Tag, Fragen beantworten
* Wir bauen eine Vorlage für Seminar- und Abschlussarbeiten: ``titlepage``, ``scrpage``
* Präsentationen mit ``Beamer``
* LaTeX automatisieren mit ``Arara``
* Schneller TeX mit Autohotkey & Co
* Briefe setzen mit ``scrlttr2``
* Mehr zu Mathematiksatz (mit ``amsmath``)


### Tag 3 - Bibliografien und Präsentationen

* Zusammenfassung vom 2. Termin, Wiederholung
* Quellcode-Listings einfügen mit dem ``Listings`` Paket
* Einfache Bibliografien -- die ``thebibliography`` Umgebung
* Bitte Jabref von www.jabref.org installieren, kostet nichts und ist sehr gut. 
  Alternativ kann man die entsprechenden Dateien auch mit dem Texteditor bearbeiten.
* Komplexe Bibliografien mit ``biblatex``, ``biber`` und ``jabref``
* ``nicefrac`` und ``nicematrix``
* Einheitensatz mit ``siunitx``

* Grafiken erstellen mit LaTeX-Paketen, Kurze Einführung ``TikZ``
* Fonts für ``pdflatex``, der LaTeX Font Katalog (https://tug.org/FontCatalogue/)
* Liste wichtiger Pakete: https://ctan.mc1.root.project-creative.net/info/first-packages/first-packages.html
* Von ``pdflatex`` zu ``lualatex``, Systemschriften nutzen


### Tag 4 - Erweiterungen

* Grundlagen der Satzautomatisierung von Textsatz mit Python (Ein Weg, Serienbriefe zu erzeugen...)
* Lebensläufe im Detail
* Lebende Kolumnentitel in KOMAscript
* Syntaxhighlighting mit pygments
* Umrahmte (farbige) Boxen mit ``tcolorbox`` (``texdoc tcolorbox``), alternativ siehe das ``mdframed`` Paket
* Editoren: ``TeXworks`` versus ``Visual Studio Code`` 
* Großer Frage-und-Antwort-Teil: was fehlt euch noch, was wolltet ihr schon immer mal TeXen?
* biblatex-apa
* Logik-Symbole gemäß https://de.wikipedia.org/wiki/Formelsammlung_Logik

## Literaturempfehlungen

Empfohlen werden:

* Alle Bücher von Herbert Voß (https://www.lehmanns.de/search/quick?PHPSESSID=mi28bh61dhv2nu8keg4hjnkunumgi5ah&mediatype_id=&q=herbert+vo%C3%9F), insbesondere die Einführung
* Der LaTeX Begleiter in der 2. Auflage (ist auch nicht mehr brandaktuell, bietet aber einen guten Überblick über LaTeX). Ist auch beispielsweise über Medimops extrem günstig zu bekommen.
* Die 3. Auflage vom Begleiter erscheint im Mai 2023

## Weitere Links

* https://open.hpi.de/courses/git2020 Git Kurs beim HPI
* Meine Briefvorlage https://www.uweziegenhagen.de/?p=3290
* Biblatex Cheat Sheet, https://www.ctan.org/tex-archive/info/biblatex-cheatsheet

