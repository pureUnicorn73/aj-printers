# Komunikaty CMS aj printers

## Gotowe pliki do CMS

Najbezpieczniej wklejac wersje HTML z encjami z folderu `cms-html`, bo nie zalezy od kodowania edytora CMS:

- `cms-html/komunikat-strona-glowna.html`
- `cms-html/komunikat-produkt-footer-pionowy.html` - aktualny blok pionowy do `leftColumn` i `leftColumnProduct`
- `cms-html/wazne-informacje-przed-zakupem.html` - tresc podstrony `https://ajprinters.pl/content/21-przed-zakupem`
- `cms-html/komunikat-produkt.html`
- `cms-html/komunikat-materialy-eksploatacyjne.html`
- `cms-html/komunikat-koszyk-dostawa.html`
- `cms-html/komunikaty-cms.html` - caly zestaw razem z przykladowym CSS
- `cms-html/komunikaty-cms.css` - sam CSS, jezeli motyw sklepu ma osobne miejsce na style

## Zasady stylistyczne

- Komunikaty maja byc neutralne i przyjazne.
- Nie uzywac czerwonych ostrzezen.
- Nie uzywac naglowkow typu `UWAGA!`.
- Zalecane tlo: jasnoszare albo jasnoniebieskie.
- Zalecana typografia: 13-15 px.
- Zalecane rogi: delikatnie zaokraglone.
- Komunikaty nie powinny zaslaniac ceny, przycisku zakupu ani informacji o dostawie.

## Aktualna decyzja wdrozeniowa

Nie publikujemy osobnego bloku na stronie glownej.

Informacje przed zakupem sa wdrazane jako:

- podstrona CMS: `https://ajprinters.pl/content/21-przed-zakupem`;
- pionowy blok HTML w hookach Presta: `leftColumn` oraz `leftColumnProduct`;
- plik do wklejenia w blok boczny: `cms-html/komunikat-produkt-footer-pionowy.html`.

## Podstrona "Przed zakupem"

Plik HTML:
`cms-html/wazne-informacje-przed-zakupem.html`

Naglowek:
`Wazne informacje przed zakupem`

### Wersja tekstowa

Wazne informacje przed zakupem

Dokladamy wszelkich staran, aby opisy, zdjecia, ceny i parametry produktow w sklepie aj printers byly aktualne i prawidlowe. Zdjecia przedstawiaja oferowany produkt, jednak kolorystyka, detale graficzne, etykieta lub wyglad opakowania moga roznic sie od prezentowanych na stronie.

Jezeli na zdjeciu widoczne jest opakowanie zbiorcze, karton, paczka lub zestaw, nie oznacza to sprzedazy calego opakowania. Podstawowa jednostka sprzedazy jest 1 sztuka produktu, chyba ze nazwa, opis lub parametry wyraznie wskazuja inaczej.

Przed zakupem prosimy o sprawdzenie zgodnosci produktu z modelem urzadzenia. W razie watpliwosci zachecamy do kontaktu - pomozemy dobrac wlasciwy produkt.

Informacje o dostepnosci i terminach realizacji aktualizujemy na biezaco, jednak w wyjatkowych przypadkach moga one zalezec od dostawcy lub przewoznika. W przypadku zauwazenia bledu lub niescislosci prosimy o kontakt przed zlozeniem zamowienia.

## Starszy wariant HTML na strone glowna

Pliki `cms-html/komunikat-strona-glowna.html`, `cms-html/komunikat-strona-glowna-benefits-bar.html` i `cms-html/komunikat-strona-glowna-krotki-inline.html` zostaja jako warianty robocze, ale aktualnie nie sa wdrazane.

## Karta produktu - komunikat podstawowy

Miejsce:
w poblizu ceny, opisu albo przycisku zakupu, ale bez zaburzania ukladu mobilnego.

### Wersja tekstowa

Zdjecia przedstawiaja oferowany produkt, jednak kolorystyka, detale, etykieta lub wyglad opakowania moga roznic sie od prezentowanych. Cena dotyczy 1 sztuki, chyba ze nazwa, opis lub parametry produktu wskazuja inaczej.

Jezeli zdjecie pokazuje opakowanie zbiorcze, karton lub zestaw, nie oznacza to sprzedazy calego opakowania. Masz watpliwosci? Skontaktuj sie z nami przed zakupem.

### Wersja HTML

```html
<div class="aj-info-box aj-info-box--product">
  <p>Zdjecia przedstawiaja oferowany produkt, jednak kolorystyka, detale, etykieta lub wyglad opakowania moga roznic sie od prezentowanych. Cena dotyczy 1 sztuki, chyba ze nazwa, opis lub parametry produktu wskazuja inaczej.</p>
  <p>Jezeli zdjecie pokazuje opakowanie zbiorcze, karton lub zestaw, nie oznacza to sprzedazy calego opakowania. Masz watpliwosci? Skontaktuj sie z nami przed zakupem.</p>
</div>
```

## Karta produktu - materialy eksploatacyjne

Miejsce:
na kartach produktow, gdzie istotna jest zgodnosc z modelem urzadzenia.

### Wersja tekstowa

Przed zakupem sprawdz zgodnosc produktu z modelem urzadzenia. W razie watpliwosci skontaktuj sie z nami - pomozemy dobrac odpowiedni produkt.

### Wersja HTML

```html
<div class="aj-info-box aj-info-box--compatibility">
  <p>Przed zakupem sprawdz zgodnosc produktu z modelem urzadzenia. W razie watpliwosci skontaktuj sie z nami - pomozemy dobrac odpowiedni produkt.</p>
</div>
```

## Koszyk albo dostawa

Miejsce:
w koszyku, przy wyborze dostawy albo przy podsumowaniu zamowienia.

Status:
plik jest przygotowany, ale wdrozenie w Presta zostaje przeniesione do osobnego projektu.

### Wersja tekstowa

Termin realizacji moze zalezec od dostepnosci produktu u dostawcy oraz pracy przewoznika. W razie zmian skontaktujemy sie z Toba przed realizacja zamowienia.

### Wersja HTML

```html
<div class="aj-info-box aj-info-box--checkout">
  <p>Termin realizacji moze zalezec od dostepnosci produktu u dostawcy oraz pracy przewoznika. W razie zmian skontaktujemy sie z Toba przed realizacja zamowienia.</p>
</div>
```

## Przykladowy CSS

Kod orientacyjny. Nalezy dopasowac do stylow motywu sklepu.

```css
.aj-info-box {
  background: #f5f8fb;
  border: 1px solid #dce7f2;
  border-radius: 8px;
  color: #243447;
  font-size: 14px;
  line-height: 1.5;
  padding: 14px 16px;
  margin: 16px 0;
}

.aj-info-box h2 {
  font-size: 18px;
  line-height: 1.3;
  margin: 0 0 10px;
}

.aj-info-box p {
  margin: 0 0 8px;
}

.aj-info-box p:last-child {
  margin-bottom: 0;
}

@media (max-width: 767px) {
  .aj-info-box {
    font-size: 13px;
    padding: 12px 14px;
  }
}
```

## Kontrola po wdrozeniu

- Komunikaty nie sa czerwone i nie wygladaja jak alarm.
- Tekst jest czytelny na telefonie.
- Box na karcie produktu nie zaslania ceny ani przycisku zakupu.
- Komunikat w koszyku nie utrudnia przejscia do platnosci.
- Nazwa firmy wystepuje jako `aj printers`.
- Kontakt sklepu prowadzi na `sklep@ajprinters.pl`, jezeli komunikat zawiera dane kontaktowe.
