# Wdrozenie dokumentow aj printers

## Cel

Uzupelnic strone aj printers o dokumenty regulaminowe, reklamacyjne, zwrotowe, RODO oraz komunikaty informacyjne w podstronach CMS, lewej kolumnie, kartach produktu i docelowo w koszyku.

## Struktura publiczna plikow

Rekomendowane katalogi publiczne:
- `/pliki/dokumenty/`
- `/pliki/protokoly-szkody/`

Linki do PDF powinny otwierac sie w nowej karcie.

## Podstrony CMS

| Podstrona | Tresc z pliku TXT | Przycisk "Pobierz PDF" |
| --- | --- | --- |
| `/regulamin/` | `content/cms/pages/regulamin.html` | `/pliki/dokumenty/regulamin-aj-printers.pdf` |
| `/polityka-prywatnosci/` | `content/cms/pages/polityka-prywatnosci.html` | `/pliki/dokumenty/polityka-prywatnosci-aj-printers.pdf` |
| `/obowiazek-informacyjny/` | `content/cms/pages/obowiazek-informacyjny.html` | `/pliki/dokumenty/obowiazek-informacyjny-aj-printers.pdf` |
| `/reklamacje/` | `content/cms/pages/reklamacje.html` | `/pliki/dokumenty/reklamacje-aj-printers.pdf` |
| `https://ajprinters.pl/content/17-zwroty-regulamin-zwrotow` | `content/cms/pages/zwroty-regulamin-zwrotow.html` | `/pliki/dokumenty/regulamin-zwrotow-aj-printers.pdf` |
| `/odstapienie-od-umowy/` | `content/cms/pages/odstapienie-od-umowy.html` | `/pliki/dokumenty/odstapienie-od-umowy-aj-printers.pdf` |
| `/informacja-o-zagrozeniach/` | `content/cms/pages/informacja-o-zagrozeniach.html` | `/pliki/dokumenty/informacja-o-zagrozeniach-aj-printers.pdf` |
| `/warunki-gwarancji-produktow-thi/` | `content/cms/pages/warunki-gwarancji-produktow-thi.html` | `/pliki/dokumenty/warunki-gwarancji-produktow-thi-aj-printers.pdf` |

Decyzja URL: strona zwrotow ma dzialac pod adresem `https://ajprinters.pl/content/17-zwroty-regulamin-zwrotow`.

## Pliki PDF do publikacji

Aktualną paczkę tworzy polecenie
`powershell -NoProfile -ExecutionPolicy Bypass -File scripts/build-release.ps1`.
Wynik pojawia się w `dist/aj-printers-wdrozenie.zip`.

Poprzednia paczka z 6 lipca 2026 r. znajduje się wyłącznie w `archive/releases/`.

Do `/pliki/dokumenty/`:
- pliki z `public/documents/`

Do `/pliki/protokoly-szkody/`:
- pliki z `public/damage-reports/`

## Sekcja na stronie Reklamacje

Naglowek:
`Formularze i protokoly do pobrania`

Linki:
- Formularz reklamacyjny aj printers: `/pliki/dokumenty/formularz-reklamacyjny-aj-printers.pdf`
- Protokol szkody DHL: `/pliki/protokoly-szkody/protokol-szkody-dhl.pdf`
- Protokol szkody DPD: `/pliki/protokoly-szkody/protokol-szkody-dpd.pdf`
- Protokol szkody FedEx: `/pliki/protokoly-szkody/protokol-szkody-fedex.pdf`
- Protokol szkody GEODIS: `/pliki/protokoly-szkody/protokol-szkody-geodis.pdf`
- Protokol szkody GLS: `/pliki/protokoly-szkody/protokol-szkody-gls.pdf`
- Protokol szkody InPost: `/pliki/protokoly-szkody/protokol-szkody-inpost.pdf`
- Protokol szkody Raben: `/pliki/protokoly-szkody/protokol-szkody-raben.pdf`
- Protokol szkody UPS: `/pliki/protokoly-szkody/protokol-szkody-ups.pdf`

## Sekcja na stronie Odstapienie od umowy

Dodatkowy przycisk:
`Pobierz formularz odstapienia od umowy PDF`

Link:
`/pliki/dokumenty/formularz-odstapienia-aj-printers.pdf`

## Informacje przed zakupem

Decyzja wdrozeniowa:
nie publikujemy osobnego bloku na stronie glownej. Informacje przed zakupem sa wdrazane jako podstrona CMS oraz pionowy blok w lewej kolumnie.

Podstrona CMS:
`https://ajprinters.pl/content/21-przed-zakupem`

Tresc podstrony:
`content/cms/pages/przed-zakupem.html`

Blok boczny:
`content/cms/components/komunikat-produkt-footer-pionowy.html`

Hooki Presta:
- `leftColumn`
- `leftColumnProduct`

Naglowek:
`Wazne informacje przed zakupem`

Tresc:
`Dokladamy wszelkich staran, aby opisy, zdjecia, ceny i parametry produktow w sklepie aj printers byly aktualne i prawidlowe. Zdjecia przedstawiaja oferowany produkt, jednak kolorystyka, detale graficzne, etykieta lub wyglad opakowania moga roznic sie od prezentowanych na stronie.`

`Jezeli na zdjeciu widoczne jest opakowanie zbiorcze, karton, paczka lub zestaw, nie oznacza to sprzedazy calego opakowania. Podstawowa jednostka sprzedazy jest 1 sztuka produktu, chyba ze nazwa, opis lub parametry wyraznie wskazuja inaczej.`

`Przed zakupem prosimy o sprawdzenie zgodnosci produktu z modelem urzadzenia. W razie watpliwosci zachecamy do kontaktu - pomozemy dobrac wlasciwy produkt.`

`Informacje o dostepnosci i terminach realizacji aktualizujemy na biezaco, jednak w wyjatkowych przypadkach moga one zalezec od dostawcy lub przewoznika. W przypadku zauwazenia bledu lub niescislosci prosimy o kontakt przed zlozeniem zamowienia.`

## Komunikaty na karcie produktu

Podstawowy box:
`Zdjecia przedstawiaja oferowany produkt, jednak kolorystyka, detale, etykieta lub wyglad opakowania moga roznic sie od prezentowanych. Cena dotyczy 1 sztuki, chyba ze nazwa, opis lub parametry produktu wskazuja inaczej.`

Dla materialow eksploatacyjnych:
`Przed zakupem sprawdz zgodnosc produktu z modelem urzadzenia. W razie watpliwosci skontaktuj sie z nami - pomozemy dobrac odpowiedni produkt.`

Dodatkowa informacja:
`Jezeli zdjecie pokazuje opakowanie zbiorcze, karton lub zestaw, nie oznacza to sprzedazy calego opakowania. Masz watpliwosci? Skontaktuj sie z nami przed zakupem.`

## Komunikat w koszyku lub przy dostawie

`Termin realizacji moze zalezec od dostepnosci produktu u dostawcy oraz pracy przewoznika. W razie zmian skontaktujemy sie z Toba przed realizacja zamowienia.`

Status:
przygotowany jako plik `content/cms/components/komunikat-koszyk-dostawa.html`, ale wdrozenie komunikatu w koszyku / przy dostawie zostaje przeniesione do osobnego projektu.

## Wskazowki stylistyczne

- Komunikaty neutralne i przyjazne.
- Bez czerwonych ostrzezen.
- Bez naglowkow typu `UWAGA!`.
- Jasnoszare lub jasnoniebieskie tlo.
- Zaokraglone rogi.
- Mala typografia: 13-15 px.
- Linki PDF otwierane w nowej karcie.

## Kontrola po wdrozeniu

- Wszystkie podstrony dzialaja.
- Linki do PDF dzialaja.
- PDF-y sa dostepne publicznie.
- Linki miedzy dokumentami nie prowadza do blednych sciezek.
- Komunikaty na produkcie nie zaburzaja ukladu mobilnego.

## Decyzje wdrozeniowe

- Strona zwrotow: `https://ajprinters.pl/content/17-zwroty-regulamin-zwrotow`.
- Formularz reklamacyjny linkujemy na stronie `Reklamacje` w sekcji formularzy i protokolow do pobrania; jezeli CMS pozwala, dodajemy tez przycisk lub box w tresci procedury reklamacyjnej.
- Publikujemy wszystkie protokoly przewoznikow dostepne w paczce: DHL, DPD, FedEx, GEODIS, GLS, InPost, Raben, UPS.
- W tresciach publikowanych w CMS uzywamy polskich znakow.
