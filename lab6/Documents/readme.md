Marcin Ryznar, 405745

#ZAWARTOSC DOKUMENTACJI REPLIKACJI

Zbiór danych ŚWIĘTOKSZYSKIE.csv
ŚWIĘTOKSZYSKIE.csv - dane o markach firm, dniach zakupow produktow, wieku kupujacego oraz plci kupujacego


Plik "raport.ipynb" z rozwiazaniem znajduje sie w Command Files, gdzie dane zostały pobierane z Analysis Data z plików 12_sw_original.csv.
W powyższym pliku('raport.ipynb') zadeklarowałęm dane odnośnie kolumn oraz przedstawionych wartości w tabeli. Dokonałem odpowiednich przeksztalecen dokonujac analizy na temat ilosci klientów w odpowiedniej firmie. Zrealizowalem ten podzial ze wzgledu na plec. Uwzglednilem ocene kobiet oraz mezczyzn na temat danej firmy. Następnie zapisałem dane wyświetlone w tabeli na podstawie pandas w pliku csv, który znajduje sie w folderze Analysis Data. Przedstawione rezultaty ukazalem za pomoca wykresów słupkowych oraz kołowych w celu jak najlepszego ich przedstawienia. Tabele wynikowe, również zamieściłem w folderze Analysis Data. 

+ Folder Original Data posiada oryginaly plik ŚWWIĘTOKSZYSKIE.csv wraz z rospisaną matadaną.
+ Folder Command File zawiera raport.ipytd w którym zostałą zrealizowana analiza danych na podstawie pliku 12_sw_original.csv (zawiera identyczne dane co ŚWIĘTOKSZYSKIE.csv)
+ Folder Analysis Data zawiera pliki z danymi na temat oceny poszczególnej firmy według płci, ilości klientów w danej firmie (liczba kobiet/mezczyzn), ogólnej ilości mezczyzn i kobiet podejmujacych jakiekolwiek działania we wszystkich firmach
+ Folder Documents zawiera plik readme.md oraz zrzuty ekranu rezultatów z nazwami plików odpowiadającymi tytułom poszczególnych wykresów.

#OPIS ORIGINAL DATA
Nazwy kolumn są tworzone w następujący sposób:

-Dni od zakupu 
    -dokonanej tranzakcji w sklepie
-Marka
    -Beko
    -Tefal
    -Electrolux
    -Samsung
    -Dyson
    
-Wiek kupującego 


-Płeć kupującego:

    K = kobieta
    M = mężczyzna
    bd. = brak danych

-Ocena
    podlega indywidualnemu przekonaniu klienta na temat danej firmy