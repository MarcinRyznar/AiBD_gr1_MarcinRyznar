Marcin Ryznar, 405745

#ZAWARTOSC DOKUMENTACJI REPLIKACJI

Zbiór danych tb.csv
tb.csv - dane o gruźlicy w różnych grupach pacjentów (tabela koduje jednocześnie informacje o wieku i o płci w kolumnach i zawiera dużo pustych miejsc)
Plik "raport.ipynb" z rozwiazaniem znajduje sie w Command Files, gdzie dane zostały pobierane z Analysis Data z plików tb_original.csv.
W powyższym pliku('raport.ipynb') zadeklarowałęm dane odnośnie zakażeń na gruźlicę wśród mężczyzn i kobiet na świecie dla pewnego przedziału lat. Na ich podtawie wyliczyłem sumę zakażeń dla danej płci oraz wyświetłiłem rezultaty na wykresie. Następnie zapisałem dane wyświetlone w tabeli na podstawie pandas w pliku csv, który znajduje sie w folderze Analysis Data. Kolejnym krokiem było podobne przedstawienie danych dla Polski oraz jej sąsiadów. Dokładnie rozpisałem kraje z uwzględnieniem tabeli wynikowej, ogólnego liniowego wykresu zachorowań oraz słupkowego wykresu skali zachorowań płci w zależności od pańtwa. Tabele wynikowe, również zamieściłem w folderze Analysis Data. Ostatni wykres słupkowy przedstawia skalę zachorowań dla Polski oraz jej sąsiadów na przestrzeni lat.

+ Folder Original Data posiada oryginaly plik tb.csv wraz z rospisaną matadaną.
+ Folder Command File zawiera raport.ipytd w którym zostałą zrealizowana analiza danych na podstawie pliku tb_original.csv (zawiera identyczne dane co tb.csv)
+ Folder Analysis Data zawiera pliki z danymi dla Polski oraz jej granicznych sąsiadów. Kolumny odpowiadaja za kraj, ilość zakażeń, oraz zakażenia wśród kobiet jak i mężczyzn.
+ Folder Documents zawiera plik readme.md oraz zrzuty ekranu rezultatów z nazwami plików odpowiadającymi tytułom poszczególnych wykresów.

#OPIS ORIGINAL DATA
Nazwy kolumn są tworzone w następujący sposób:

    iso2 - kraje
    year - odpowiednie lata

-poprzez połączenie "new_" oznaczajace metodę diagnozy:

    rel = nawrót
    sn = ujemny rozmaz płucny
    sp = dodatni rozmaz płucny
    ep = pozapłucny

-płeć:

    f = kobieta
    m = mężczyzna
    
-wiek:

    014 = 0-14 lat,
    1524 = 15-24 lata,
    2534 = 25 do 34 lat, 
    3544 = 35 do 44 lat,
    4554 = 45 do 54 lat, 
    5564 = 55 do 64 lat, 
    65 = 65 lat lub więcej).
