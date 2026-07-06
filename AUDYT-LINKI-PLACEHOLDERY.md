# Audyt linkow i placeholderow

## Zakres

Sprawdzone pliki TXT w katalogu `txt/` pod katem:
- placeholderow daty publikacji;
- placeholderow do uzupelnienia;
- odnosnikow zapisanych jako nazwy plikow PDF;
- zgodnosci z briefem wdrozeniowym.

## Wyniki

### 1. Daty obowiazywania

W dokumentach wystepuje placeholder `Data obowiazywania: [data publikacji]`.

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
ustalic jedna date publikacji i wpisac ja we wszystkich dokumentach.

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

W samej tresci `txt/reklamacje-aj-printers.txt` warto dodac krotka wzmianke o formularzu reklamacyjnym jako pomocniczym formularzu do pobrania.

### 5. Placeholdery THI

W pliku `txt/warunki-gwarancji-produktow-thi-aj-printers.txt` zostaly dwa placeholdery:
- linia 33: link do instrukcji skladania reklamacji w systemie THI;
- linia 34: link do instrukcji prawidlowego pakowania zwrotow/reklamacji.

Rekomendacja:
albo uzupelnic linki, albo usunac te punkty z wersji publikowanej, jezeli linki nie sa gotowe.

### 6. README-linkowanie

Plik `txt/README-linkowanie.txt` zawiera starszy adres `/zwroty/`.

Rekomendacja:
zaktualizowac go do `https://ajprinters.pl/content/12-zwroty` albo uznac, ze nadrzedna checklista `WDROZENIE-CHECKLISTA.md` zastępuje ten plik.

## Proponowana kolejnosc poprawek

1. Ustalic date publikacji dokumentow.
2. Zdecydowac, czy placeholdery THI usuwamy czy uzupelniamy linkami.
3. Zaktualizowac linki w TXT pod CMS.
4. Dodac wzmianke o formularzu reklamacyjnym w `txt/reklamacje-aj-printers.txt`.
5. Po zatwierdzeniu zmian wygenerowac albo podmienic finalne PDF-y, jezeli PDF-y maja odzwierciedlac poprawione TXT.

