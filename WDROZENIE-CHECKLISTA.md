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
| `/regulamin/` | `txt/regulamin-aj-printers.txt` | `/pliki/dokumenty/regulamin-aj-printers.pdf` |
| `/polityka-prywatnosci/` | `txt/polityka-prywatnosci-aj-printers.txt` | `/pliki/dokumenty/polityka-prywatnosci-aj-printers.pdf` |
| `/obowiazek-informacyjny/` | `txt/obowiazek-informacyjny-aj-printers.txt` | `/pliki/dokumenty/obowiazek-informacyjny-aj-printers.pdf` |
| `/reklamacje/` | `txt/reklamacje-aj-printers.txt` | `/pliki/dokumenty/reklamacje-aj-printers.pdf` |
| `https://ajprinters.pl/content/17-zwroty-regulamin-zwrotow` | `txt/regulamin-zwrotow-aj-printers.txt` | `/pliki/dokumenty/regulamin-zwrotow-aj-printers.pdf` |
| `/odstapienie-od-umowy/` | `txt/odstapienie-od-umowy-aj-printers.txt` | `/pliki/dokumenty/odstapienie-od-umowy-aj-printers.pdf` |
| `/informacja-o-zagrozeniach/` | `txt/informacja-o-zagrozeniach-aj-printers.txt` | `/pliki/dokumenty/informacja-o-zagrozeniach-aj-printers.pdf` |
| `/warunki-gwarancji-produktow-thi/` | `txt/warunki-gwarancji-produktow-thi-aj-printers.txt` | `/pliki/dokumenty/warunki-gwarancji-produktow-thi-aj-printers.pdf` |

Decyzja URL: strona zwrotow ma dzialac pod adresem `https://ajprinters.pl/content/17-zwroty-regulamin-zwrotow`.

## Pliki PDF do publikacji

Gotowa paczka plikow publicznych znajduje sie w:
- `wdrozenie/pliki/dokumenty/`
- `wdrozenie/pliki/protokoly-szkody/`

Gotowe archiwum do przekazania:
- `wdrozenie-aj-printers-2026-07-06.zip`

Do `/pliki/dokumenty/`:
- `pdf/regulamin-aj-printers.pdf`
- `pdf/polityka-prywatnosci-aj-printers.pdf`
- `pdf/obowiazek-informacyjny-aj-printers.pdf`
- `pdf/reklamacje-aj-printers.pdf`
- `pdf/regulamin-zwrotow-aj-printers.pdf`
- `pdf/odstapienie-od-umowy-aj-printers.pdf`
- `pdf/informacja-o-zagrozeniach-aj-printers.pdf`
- `pdf/warunki-gwarancji-produktow-thi-aj-printers.pdf`
- `pdf/formularz-odstapienia-aj-printers.pdf`
- `pdf/formularz-reklamacyjny-aj-printers.pdf`

Do `/pliki/protokoly-szkody/`:
- `zalaczniki/protokol-szkody-dhl.pdf`
- `zalaczniki/protokol-szkody-dpd.pdf`
- `zalaczniki/protokol-szkody-fedex.pdf`
- `zalaczniki/protokol-szkody-geodis.pdf`
- `zalaczniki/protokol-szkody-gls.pdf`
- `zalaczniki/protokol-szkody-inpost.pdf`
- `zalaczniki/protokol-szkody-raben.pdf`
- `zalaczniki/protokol-szkody-ups.pdf`

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
`cms-html/wazne-informacje-przed-zakupem.html`

Blok boczny:
`cms-html/komunikat-produkt-footer-pionowy.html`

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
przygotowany jako plik `cms-html/komunikat-koszyk-dostawa.html`, ale wdrozenie komunikatu w koszyku / przy dostawie zostaje przeniesione do osobnego projektu.

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
