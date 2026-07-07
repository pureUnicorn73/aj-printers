# Linki CMS do potwierdzenia w Presta

## Cel

Sprawdzic, czy linki wewnetrzne w dokumentach CMS prowadza do faktycznych podstron sklepu aj printers, a nie do przypadkowych stron albo adresow 404.

## Potwierdzone

- Zwroty: `https://ajprinters.pl/content/12-zwroty`
- Przed zakupem: `https://ajprinters.pl/content/21-przed-zakupem`

## Do potwierdzenia

Potrzebne sa docelowe adresy URL tych podstron:

- Regulamin
- Polityka prywatnosci
- Reklamacje
- Odstapienie od umowy
- Informacja o zagrozeniach
- Warunki gwarancji produktow THI

## Obecne adresy uzyte roboczo w plikach HTML

- `https://ajprinters.pl/regulamin/`
- `https://ajprinters.pl/polityka-prywatnosci/`
- `https://ajprinters.pl/reklamacje/`
- `https://ajprinters.pl/odstapienie-od-umowy/`
- `https://ajprinters.pl/informacja-o-zagrozeniach/`
- `https://ajprinters.pl/warunki-gwarancji-produktow-thi/`

## Co zrobic po potwierdzeniu

Po otrzymaniu prawidlowych adresow z Presta podmienic linki w plikach:

- `cms-html/regulamin-aj-printers.html`
- `cms-html/polityka-prywatnosci-aj-printers.html`
- `cms-html/obowiazek-informacyjny-aj-printers.html`
- `cms-html/regulamin-zwrotow-aj-printers.html`
- `cms-html/reklamacje-aj-printers.html`

Nie zmieniac linkow PDF w `/pliki/dokumenty/` i `/pliki/protokoly-szkody/`, jezeli dzialaja publicznie.
