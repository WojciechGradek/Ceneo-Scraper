#CeneoScraperN11
## Etap 1 Pobranie składowych pojedyńczej opinii o konkretnym produkcie z serwisu [ceneo.pl] (https://www.ceneo.pl/)
1. Pobranie kodu pojedyńczej strony z opiniami o produkcie
2. Analiza struktury kodu pojedyńczej opinii

|Składowa|Selektor CSS|Nazwa zmiennej|Typ danych|
|:------|:----------|:------------|:--------|
|Opinia|`div.js_product-review`|review||
|Identyfikator opinii|`[data-entry-id]`|review_id||
|Autor opinji|`span.user-post__author-name`|author|| 
|Rekomendacja|`span.user-post__author-recomendation`|recommendation||
|Liczba gwiazdek|`span.user-post__score-count`|stars|| 
|Treść opinii|`div.user-post__text`|content||
|Lista zalet|`div.review-feature__col:has(> div.review-feature__title--positives) > div.review-feature__item`<br>`div.review-feature__col:has(> div[class*="positives"]) > div.review-feature__item`<br>`div.review-feature__title--positives ~ div.review-feature__item`|pros||
|Lista wad|``div.review-feature__col:has(> div.review-feature__title--negatives) > div.review-feature__item`<br>`div.review-feature__col:has(> div[class*="negatives"]) > div.review-feature__item`<br>`div.review-feature__title--negatives ~ div.review-feature__item``|cons||
|Dla ilu osób przydatna|`span[id^="votes-yes"]`<br>`button.vote-yes["data-total-vote"]`<br>`button.vote-yes > span`|useful||
|Dla ilu osób nieprzydatna|`span[id^="votes-no"]`<br>`button.vote-no["data-total-vote"]`<br>`button.vote-no > span`|useless|| 
|Czy potwierdzona zakupem|`div.review-pz`|purchased|| 
|Data wystawienia opinii|`span.user-post__published > time:nth-child(1)["datetime"]`|review_date||
|Data zakupu produktu|`span.user-post__published > time:nth-child(2)["datetime"]`|purchase_date||

div.review-feature__col:has(> div.review-feature__title--positives) > div.review-feature__item
div.review-feature__col:has(> div[class*="positives"]) > div.review-feature__item
div.review-feature__title--positives ~ div.review-feature__item

`span[id^="votes-yes"]`<br>`button.vote-yes["data-total-vote]`<br>`button.vote-yes > span`

`span[id^="votes-no"]`
`button.vote-no["data-total-vote]`
`button.vote-no > span`

3. Pobranie składowych opinii do pojedyńczych zmiennych

## Etap 2 - Pobranie wszystkich opinii z pojedyńczej strony
1. Zdefiniowanie słownika do przechowywania składowych
2. Zdefiniowanie listy do przechowywania słowników z opiniami
3. Dodanie pętli wykonującej operację ekstrakcji na wszystkich opiniach z pojedyńczej strony

## Etap 3 - Pobranie wszystkich opinii o produkcie
1. Dodanie pętli wykonującej operację ekstrakcji opinii z wszystkich stron z opiniami dla danego produktu
2. Wczytywanie kodu produktu z standardowego wejścia
3. Parametryzacja adresy strony z opiniami
4. Eksport opinii o produkcjie do pliku .json

## Etap 4 - Analiza pobranych opinii




