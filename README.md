# Prosta tekstowa gra RPG

## Autor:
Aleksander Szczepura s24454

## Opis:
Gra powinna pozwalać na rozwój postaci, odwiedzanie różnych lokacji i pojedynkowanie się z przeciwnikami. Wymagana jest trwałość stanu rozgrywki pomiędzy sesjami.

## Wymagania:
1.	Postać gracza powinna mieć statystki: punkty zdrowia, punkty ataku, punkty obrony, szansę na trafienie krytyczne
2.	Postać powinna móc gromadzić punkty doświadczenia. Punkty te są przeliczalne na poziom doświadczenia. Każdy poziom doświadczenia powinien zwiększać bazowe statystyki, oraz przydzielać postaci jeden punkt umiejętności.
3.	Gracz powinien móc wydać punkt umiejętności na rozwój wybranej statystyki.
4.	Statystyki bazowe jak i ich przyrosty powinny być wstępnie dostosowane tak aby umożliwiać poprawne działanie gry.
5.	Gracz może wyruszyć w podróż do wybranej lokacji. Każda podróż skutkuje napotkaniem losowego przeciwnika przypisanego do danej lokacji.
6.	Walka przebiega w systemie turowym i zaczyna się od tury gracza.
7.	Podczas jednej tury gracz wybiera w kierunku jakiej części ciała przeciwnika chce wyprowadzić atak. Po ataku punkty życia przeciwnika są obniżane o przeliczone punkty zadanych obrażeń. Przeciwnik odpowiada atakiem na losową część ciała gracza.
8.	Jeżeli punkty życia przeciwnika spadną do zera, gracz uzyskuje nagrodę w postaci punktów doświadczenia. Jeżeli to punkty życia gracza spadną do zera, ponosi on porażkę i wraca do menu głównego bez nagrody.
9.	Postęp gry powinien być zapisywany w pliku po każdej zakończonej walce oraz zmianie statystyk, a wczytywany przy każdym uruchomieniu aplikacji.
10.	Nawigowanie po interfejsie aplikacji powinno być możliwie szybkie i wygodne, aby zapewnić płynność rozgrywki.
11.	Wszelkie dane powinny być prezentowane w czytelnej formie.

## Wymagania systemowe:
1.	python (aplikacja była testowania z użyciem wersji 3.10.7).
2.	pip
3.	odpowiedni wybór i ustawienie terminala:

  	- terminal – testowane z użyciem systemu Windows i terminali: cmd, powershell, git bash – system operacyjny i jego wersja, jak i program przez który uruchamiany jest terminal (np. PyCharm) mogą mieć wpływ na poprawność działania, jest to ograniczenie wynikające z użycia biblioteki https://docs.python.org/3/library/curses.html - nie jest również gwarantowane działanie na systemach innych niż Windows
    - rozmiar okna – minimalnie 20 wierszy i 70 kolumn – najbezpieczniej jest użyć okna w trybie pełnoekranowym


## Uruchamianie:
Wszystkie poniższe komendy muszą być wykonywane z poziomu głównego katalogu projektu.

Instalacja zależności:
`pip install -r requirements.txt`

Uruchomienie aplikacji:
`python main.py`

## Użytkowanie:
Do poruszania się po aplikacji używana jest jedynie klawiatura:
-	zatwierdzanie operacji – enter
-	wybór opcji w menu – strzałka w górę i strzałka w dół
-	wydawanie punktów umiejętności – strzałka w prawo i strzałka w lewo
-	wybór ataku podczas walki - strzałki

