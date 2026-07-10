# Audyt linkow i placeholderow

## Zakres

Sprawdzone pliki TXT w katalogu `txt/` pod katem:
- placeholderow daty publikacji;
- placeholderow do uzupelnienia;
- odnosnikow zapisanych jako nazwy plikow PDF;
- zgodnosci z briefem wdrozeniowym.

## Wyniki

### 1. Daty obowiazywania

W dokumentach wystepuje placeholder `Data obowiązywania: [do uzupełnienia przed publikacją]`.

Pliki:
- `txt/regulamin-aj-printers.txt`
- `txt/polityka-prywatnosci-aj-printers.txt`
- `txt/obowiazek-informacyjny-aj-printers.txt`
- `txt/reklamacje-aj-printers.txt`
- `txt/regulamin-zwrotow-aj-printers.txt`
- `txt/odstapienie-od-umowy-aj-printers.txt`
- `txt/informacja-o-zagrozeniach-aj-printers.txt`
- `txt/warunki-gwarancji-produktow-thi-aj-printers.txt`

Rekomendacja:
pozostawic pole daty do recznego uzupelnienia przed publikacja albo wpisac jedna date publikacji we wszystkich dokumentach.

### 2. Linki miedzy dokumentami

W tresci dokumentow linki sa zapisane jako nazwy plikow PDF, np. `regulamin-aj-printers.pdf`, `reklamacje-aj-printers.pdf`, `regulamin-zwrotow-aj-printers.pdf`.

Rekomendacja:
w tresciach publikowanych w CMS zamienic nazwy plikow na docelowe adresy podstron albo publiczne URL-e PDF, zależnie od kontekstu:
- gdy dokument odsyla do tresci prawnej, preferowac podstrone CMS;
- gdy dokument odsyla do pobrania formularza, preferowac PDF w `/pliki/dokumenty/`;
- gdy dokument odsyla do protokolu szkody, preferowac PDF w `/pliki/protokoly-szkody/`.

### 3. Strona zwrotow

Docelowy adres strony zwrotow:
`https://ajprinters.pl/content/12-zwroty`

Rekomendacja:
wszystkie odnosniki do Regulaminu zwrotow w dokumentach i checklistach powinny prowadzic do tego adresu, chyba ze chodzi wprost o przycisk `Pobierz PDF`.

### 4. Formularz reklamacyjny

Plik `pdf/formularz-reklamacyjny-aj-printers.pdf` jest juz w paczce.

Rekomendacja:
na stronie `Reklamacje` dodac link:
`/pliki/dokumenty/formularz-reklamacyjny-aj-printers.pdf`

W tresci `txt/reklamacje-aj-printers.txt` dodano wzmianke o formularzu reklamacyjnym jako pomocniczym formularzu do pobrania.

### 5. Instrukcje THI

W pliku `txt/warunki-gwarancji-produktow-thi-aj-printers.txt` usunieto publiczne placeholdery odsyłające klienta do systemu THI i instrukcji THI.

Rekomendacja:
klient detaliczny sklada reklamacje do aj printers. aj printers informuje go o dalszym sposobie postepowania, a ogolna instrukcja pakowania pozostaje w sekcji wysylki reklamowanego produktu.

### 6. README-linkowanie

Plik `txt/README-linkowanie.txt` zostal zaktualizowany do docelowego adresu zwrotow `https://ajprinters.pl/content/12-zwroty`.

Rekomendacja:
zaktualizowac go do `https://ajprinters.pl/content/12-zwroty` albo uznac, ze nadrzedna checklista `WDROZENIE-CHECKLISTA.md` zastępuje ten plik.

## Proponowana kolejnosc poprawek

1. Ustalic date publikacji dokumentow.
2. Nie odsylac klienta detalicznego bezposrednio do systemu THI; reklamacja trafia do aj printers, a dalsze kroki wskazuje aj printers.
3. Zaktualizowac linki w TXT pod CMS.
4. Wzmianka o formularzu reklamacyjnym w `txt/reklamacje-aj-printers.txt` zostala dodana.
5. PDF-y w katalogu `pdf/` zostaly odswiezone po zmianach w TXT.
