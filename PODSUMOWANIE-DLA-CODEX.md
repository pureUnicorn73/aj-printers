# Podsumowanie dla Codex - aj printers

## Status projektu

Projekt jest przygotowany do publikacji, ale nie traktujemy go jeszcze jako finalnie uruchomionego publicznie.

Nie wpisujemy jeszcze daty obowiazywania w dokumentach. Placeholder:

`Data obowiazywania: [do uzupelnienia przed publikacja]`

zostaje do pozniejszego recznego uzupelnienia.

## Repo i git

Repo: `C:\Users\DELL\Documents\prawne\aj-printers`

Ostatnie istotne commity:

- `6fae38e` - Oznacz koszyk do osobnego projektu
- `a43dde1` - Zamien gole URL-e CMS na linki HTML
- `aa13113` - Podmien docelowe linki CMS Presta
- `f995d74` - Dodaj liste linkow CMS do potwierdzenia
- `67f8e02` - Popraw link do warunkow THI w reklamacji
- `0a079b9` - Doprecyzuj pomocnicze linki producentow
- `75e1a9d` - Odnotuj wdrozenie informacji w lewej kolumnie
- `7f77117` - Podmien link do informacji przed zakupem

Przed zakonczeniem pracy repo bylo czyste.

## Wazne decyzje

- Koszyk / dostawa: przygotowane, ale wdrozenie przeniesione do osobnego projektu.
- Strona glowna: zrezygnowano z bloku na stronie glownej.
- Informacje przed zakupem: wdrozone jako podstrona CMS i pionowy blok w lewej kolumnie.
- Blok boczny jest uzywany w hookach Presta: `leftColumn` i `leftColumnProduct`.
- Data obowiazywania nie jest jeszcze wpisana.
- Koncowy audyt publiczny ma byc wykonany dopiero po faktycznym uruchomieniu publicznym.

## Potwierdzone adresy CMS

- Reklamacje: `https://ajprinters.pl/content/13-reklamacje`
- Polityka prywatnosci: `https://ajprinters.pl/content/14-polityka-prywatnosci`
- Regulamin: `https://ajprinters.pl/content/15-regulamin`
- Obowiazek informacyjny: `https://ajprinters.pl/content/16-obowiazek-informacyjny`
- Zwroty: `https://ajprinters.pl/content/17-zwroty-regulamin-zwrotow`
- Odstapienie od umowy: `https://ajprinters.pl/content/18-odstapienie-od-umowy`
- Informacja o zagrozeniach: `https://ajprinters.pl/content/19-informacja-o-zagrozeniach`
- Warunki gwarancji produktow THI: `https://ajprinters.pl/content/20-warunki-gwarancji-produktow-thi`
- Przed zakupem: `https://ajprinters.pl/content/21-przed-zakupem`

## Pliki CMS HTML

Glowne pliki do wklejania w CMS:

- `cms-html/regulamin-aj-printers.html`
- `cms-html/polityka-prywatnosci-aj-printers.html`
- `cms-html/obowiazek-informacyjny-aj-printers.html`
- `cms-html/reklamacje-aj-printers.html`
- `cms-html/regulamin-zwrotow-aj-printers.html`
- `cms-html/odstapienie-od-umowy-aj-printers.html`
- `cms-html/informacja-o-zagrozeniach-aj-printers.html`
- `cms-html/warunki-gwarancji-produktow-thi-aj-printers.html`
- `cms-html/wazne-informacje-przed-zakupem.html`
- `cms-html/komunikat-produkt-footer-pionowy.html`

Plik przygotowany, ale przeniesiony do osobnego projektu:

- `cms-html/komunikat-koszyk-dostawa.html`

## Najwazniejsze poprawki merytoryczne

- Zmieniono sformulowanie o zdjeciach: nie piszemy juz, ze zdjecia sa tylko pogladowe. Aktualne brzmienie wskazuje, ze zdjecia przedstawiaja oferowany produkt, ale kolorystyka, detale, etykieta lub opakowanie moga sie roznic.
- Doprecyzowano, ze zdjecie opakowania zbiorczego, kartonu lub zestawu nie oznacza sprzedazy calego opakowania.
- Pomocnicze linki producentow w reklamacji opisano jako strony wsparcia/kontaktu/serwisowe, a nie bezposrednie formularze reklamacyjne.
- Usunieto problem z golymi URL-ami w nawiasach. Linki CMS sa teraz normalnymi linkami HTML z tekstem linku.
- Poprawiono link do warunkow THI w reklamacji.

## Do zrobienia przed finalna publikacja

1. Wpisac date obowiazywania w dokumentach CMS.
2. Sprawdzic publiczne adresy CMS po publikacji.
3. Kliknac wszystkie linki miedzy dokumentami.
4. Sprawdzic przyciski PDF.
5. Sprawdzic protokoly szkody.
6. Sprawdzic widok mobilny, szczegolnie lewa kolumne i produkt.
7. Koszyk / dostawa zrobic w osobnym projekcie.
