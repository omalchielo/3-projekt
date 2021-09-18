# Engeto-pa-3-projekt
# POPIS PROJEKTU:

Tento projekt slouži k získání vstupů z parlamentních voleb z roku 2017. Odkaz na volby je [zde](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)


Spousteni projektu

Spuštění souboru election-scraper.py v rámci přík. řádku požaduje dva povinné argumenty.

```
python election-scrapper <odkaz-uzemniho-celku> <vysledny-soubor>
```
Potom se vám uloži výsledky jako soubor

## Ukázka projektu

Výsledky hlasování pro okres Prostějov:

1.argument ```https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103```

2.argument ``` *vysledky_prostejov.xlsx*```

## Spuštení programu:

```
python election-scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" "projekt"
```

## Průběh stahování:

```
BERU DATA Z: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
ZAPISUJI DO PROJEKT
UKONCUJI ELECTION-SCRAPER
```

## Částečný výstup:
KOD	JMENO	VOLICI	OBALKY

581291	Adamov	3 668	2 157

581313	Bedřichov	205	155

581330	Benešov	538	382





