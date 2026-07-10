# Wytyczne do kolejnego projektu na stronie aj printers

## Kontekst

Projekt dokumentow prawnych i komunikatow informacyjnych jest przygotowany, ale nie jest jeszcze finalnie uruchomiony publicznie.

W kolejnym projekcie beda robione inne prace na stronie aj printers. Trzeba uwazac, zeby nie zepsuc wdrozonych lub przygotowanych elementow prawnych.

## Czego nie zmieniac bez potrzeby

- Nie usuwac podstron CMS od `content/13` do `content/21`.
- Nie zmieniac slugow/adresow tych podstron bez aktualizacji linkow w dokumentach.
- Nie usuwac folderow publicznych:
  - `/pliki/dokumenty/`
  - `/pliki/protokoly-szkody/`
- Nie zmieniac nazw PDF-ow, jezeli nie zostana potem podmienione linki w CMS.
- Nie usuwac bloku informacyjnego w lewej kolumnie bez decyzji.
- Nie dodawac czerwonych ostrzezen ani naglowkow typu `UWAGA!` do komunikatow prawnych.

## Aktualne adresy CMS

- Reklamacje: `https://ajprinters.pl/content/13-reklamacje`
- Polityka prywatnosci: `https://ajprinters.pl/content/14-polityka-prywatnosci`
- Regulamin: `https://ajprinters.pl/content/15-regulamin`
- Obowiazek informacyjny: `https://ajprinters.pl/content/16-obowiazek-informacyjny`
- Zwroty: `https://ajprinters.pl/content/17-zwroty-regulamin-zwrotow`
- Odstapienie od umowy: `https://ajprinters.pl/content/18-odstapienie-od-umowy`
- Informacja o zagrozeniach: `https://ajprinters.pl/content/19-informacja-o-zagrozeniach`
- Warunki gwarancji produktow THI: `https://ajprinters.pl/content/20-warunki-gwarancji-produktow-thi`
- Przed zakupem: `https://ajprinters.pl/content/21-przed-zakupem`

## Komunikat "Przed zakupem"

Nie ma osobnego bloku na stronie glownej.

Informacje przed zakupem sa realizowane przez:

- podstrone CMS `content/21-przed-zakupem`;
- pionowy blok HTML w hookach `leftColumn` i `leftColumnProduct`.

Plik z blokiem:

`content/cms/components/komunikat-produkt-footer-pionowy.html`

## Koszyk / dostawa

Komunikat koszyka/dostawy jest przygotowany, ale jego wdrozenie zostalo przeniesione do osobnego projektu.

Plik:

`content/cms/components/komunikat-koszyk-dostawa.html`

Tresc:

`Termin realizacji moze zalezec od dostepnosci produktu u dostawcy oraz pracy przewoznika. W razie zmian skontaktujemy sie z Toba przed realizacja zamowienia.`

Najlepsze miejsce wdrozenia w Presta: okolice wyboru dostawy / przewoznika, nie strona glowna.

## Zasady stylistyczne dla dalszych prac

- Komunikaty neutralne, spokojne i informacyjne.
- Tlo jasnoszare albo jasnoniebieskie.
- Typografia 13-15 px.
- Zaokraglone rogi.
- Bez czerwonego alarmowego stylu.
- Bez naglowkow typu `UWAGA!`.
- Linki do PDF otwierac w nowej karcie.
- Nie zaslaniac ceny, przycisku koszyka, wyboru wariantow ani informacji o dostawie.

## Zasady tresci

- Marka w tresci: `aj printers`.
- Kontakt sklepu: `sklep@ajprinters.pl`.
- Nie pisac, ze zdjecia sa tylko pogladowe.
- Poprawne brzmienie: zdjecia przedstawiaja oferowany produkt, ale kolorystyka, detale, etykieta lub opakowanie moga sie roznic.
- Jezeli zdjecie pokazuje opakowanie zbiorcze, karton lub zestaw, nie oznacza to sprzedazy calego opakowania.
- Podstawowa jednostka sprzedazy to 1 sztuka, chyba ze opis produktu wskazuje inaczej.

## Przed finalnym uruchomieniem

Przed finalna publikacja trzeba:

1. Wpisac date obowiazywania w dokumentach CMS.
2. Sprawdzic wszystkie publiczne podstrony CMS.
3. Kliknac linki miedzy dokumentami.
4. Kliknac przyciski PDF.
5. Sprawdzic protokoly szkody.
6. Sprawdzic widok mobilny.
7. Sprawdzic, czy blok w lewej kolumnie nie spycha waznych elementow strony.
