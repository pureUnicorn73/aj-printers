# Paczka wdrożeniowa aj printers

## Co wrzucić na serwer

Zawartość folderu `pliki/` należy opublikować tak, aby była dostępna publicznie jako:

- `/pliki/dokumenty/`
- `/pliki/protokoly-szkody/`

Przykład:

- `wdrozenie/pliki/dokumenty/regulamin-aj-printers.pdf`
  powinien być dostępny jako
  `/pliki/dokumenty/regulamin-aj-printers.pdf`

- `wdrozenie/pliki/protokoly-szkody/protokol-szkody-dhl.pdf`
  powinien być dostępny jako
  `/pliki/protokoly-szkody/protokol-szkody-dhl.pdf`

## Treści CMS

Treści podstron CMS należy wkleić z plików `txt/` w katalogu głównym paczki:

- `/regulamin/` -> `txt/regulamin-aj-printers.txt`
- `/polityka-prywatnosci/` -> `txt/polityka-prywatnosci-aj-printers.txt`
- `/obowiazek-informacyjny/` -> `txt/obowiazek-informacyjny-aj-printers.txt`
- `/reklamacje/` -> `txt/reklamacje-aj-printers.txt`
- `https://ajprinters.pl/content/12-zwroty` -> `txt/regulamin-zwrotow-aj-printers.txt`
- `/odstapienie-od-umowy/` -> `txt/odstapienie-od-umowy-aj-printers.txt`
- `/informacja-o-zagrozeniach/` -> `txt/informacja-o-zagrozeniach-aj-printers.txt`
- `/warunki-gwarancji-produktow-thi/` -> `txt/warunki-gwarancji-produktow-thi-aj-printers.txt`

Na każdej podstronie należy dodać przycisk `Pobierz PDF` prowadzący do właściwego pliku w `/pliki/dokumenty/`.

## Dodatkowe sekcje

Na stronie `Reklamacje` należy dodać sekcję:

`Formularze i protokoły do pobrania`

Linki:

- `/pliki/dokumenty/formularz-reklamacyjny-aj-printers.pdf`
- `/pliki/protokoly-szkody/protokol-szkody-dhl.pdf`
- `/pliki/protokoly-szkody/protokol-szkody-dpd.pdf`
- `/pliki/protokoly-szkody/protokol-szkody-fedex.pdf`
- `/pliki/protokoly-szkody/protokol-szkody-geodis.pdf`
- `/pliki/protokoly-szkody/protokol-szkody-gls.pdf`
- `/pliki/protokoly-szkody/protokol-szkody-inpost.pdf`
- `/pliki/protokoly-szkody/protokol-szkody-raben.pdf`
- `/pliki/protokoly-szkody/protokol-szkody-ups.pdf`

Na stronie `Odstąpienie od umowy` należy dodać przycisk:

`Pobierz formularz odstąpienia od umowy PDF`

Link:

`/pliki/dokumenty/formularz-odstapienia-aj-printers.pdf`

## Komunikaty CMS

Gotowe komunikaty na stronę główną, kartę produktu i koszyk są w pliku:

`KOMUNIKATY-CMS.md`

## Kontrola po wdrożeniu

- sprawdzić, czy wszystkie podstrony CMS działają;
- sprawdzić, czy każdy przycisk `Pobierz PDF` otwiera PDF w nowej karcie;
- sprawdzić, czy pliki w `/pliki/dokumenty/` i `/pliki/protokoly-szkody/` są dostępne publicznie;
- sprawdzić, czy linki między dokumentami prowadzą do właściwych adresów;
- sprawdzić widok mobilny karty produktu po dodaniu komunikatów.
