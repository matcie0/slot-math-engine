# High-Performance Slot Math Engine & Monte Carlo Simulator

Profesjonalny silnik matematyczny dla gry typu slot (3x3), zoptymalizowany pod kątem wydajności przy użyciu biblioteki **NumPy**. Projekt zawiera pełny symulator statystyczny metodą Monte Carlo, pozwalający na walidację parametrów gry na dużych próbach danych.

## Kluczowe cechy
- **Wektoryzacja Obliczeń:** Wykorzystanie NumPy do przetwarzania milionów spinów.
- **Analiza Statystyczna:** Automatyczne wyliczanie kluczowych wskaźników KPI (RTP, Hit Frequency, Volatility Index).
- **Wizualizacja Danych:** Generowanie wykresów zbieżności statystycznej przy użyciu Matplotlib.
- **Logika Wilda:** Pełna obsługa symbolu Wild zastępującego inne symbole na liniach wygrywających.

## Wyniki Symulacji (Próba: 100 000 000 spinów)

Poniższa tabela przedstawia uśrednione wyniki uzyskane podczas walidacji silnika.

| Parametr | Wartość | Opis |
| :--- | :--- | :--- |
| **RTP (Return to Player)** | **97.58%** | Teoretyczny zwrot dla gracza |
| **Hit Frequency** | **32.75%** | Częstotliwość występowania jakiejkolwiek wygranej |
| **Standard Deviation** | **14.8451** | Odchylenie standardowe pojedynczego spinu |
| **Volatility Index** | **29.10** | Wskaźnik zmienności (95% Confidence Interval) |

### Zbieżność RTP (Monte Carlo)
Wykres poniżej udowadnia stabilność modelu matematycznego. Wraz ze wzrostem liczby spinów, wynik symulacji zbiega się do teoretycznego poziomu RTP, co potwierdza poprawność implementacji Prawa Wielkich Liczb.

![RTP Convergence](rtp_convergence.png)

### Symulacja sesji gracza (Analiza Monte Carlo)

W celu oceny gry z perspektywy użytkownika, przeprowadzono analizę sesji metodą Monte Carlo. Podczas gdy teoretyczne wskaźniki RTP i Volatility Index opisują zachowanie automatu w nieskończonym horyzoncie czasowym, analiza sesji pozwala zrozumieć realne ryzyko utraty kapitału (prawdopodobieństwo bankructwa).

#### Parametry symulacji:
- **Liczba sesji:** 1 000
- **Limit spinów w sesji:** 500
- **Balans początkowy:** 100 jednostek
- **Stawka (Bet):** 1 jednostka
- **Profil matematyczny:** Wysoka zmienność (VI ≈ 29.05)

#### Kluczowe wnioski:
- **Prawdopodobieństwo bankructwa:** 82,90% – taki odsetek graczy traci cały budżet przed wykonaniem 500 spinów.
- **Średnia długość sesji:** 259,4 spinów.
- **Mediana długości sesji:** 213 spinów. 
- **Interpretacja:** Różnica między medianą a średnią wskazuje na silną asymetrię rozkładu. Większość graczy kończy sesję stosunkowo szybko, natomiast średnia jest zawyżana przez nieliczne sesje o wyjątkowo długim czasie trwania, wynikającym z trafienia wysokich wygranych.

#### Wizualizacja wahań kapitału (Balance Swings):
![Balance Swings](balance_swings.png)

Powyższy wykres prezentuje 50 reprezentatywnych sesji:
- **Czerwone linie** oznaczają sesje zakończone bankructwem.
- **Zielone linie** reprezentują sesje, w których gracz przetrwał 500 spinów.
- **Gwałtowne skoki** na trajektoriach zielonych linii obrazują trafienia wysokopłatnych kombinacji (np. H1 lub symbole Wild). 
- **Systematyczny spadek** większości linii dokumentuje wpływ "House Edge" oraz kosztu gry, który przy braku trafienia wysokiej wygranej szybko pochłania pieniądze z konta przy tak wysokiej zmienności.

Analiza potwierdza, że model matematyczny poprawnie implementuje profil "High Volatility", oferując rzadkie, ale znaczące wygrane kosztem krótszego średniego czasu rozgrywki dla większości użytkowników.

## Technologia
- **Python 3.x**
- **NumPy** - macierzowe operacje na danych
- **Matplotlib** - generowanie wykresów analitycznych

## Struktura Projektu
- `numpy_simulation.py` - Główny silnik symulacji i moduł wizualizacji.
- `settings.py` - Definicja bębnów (Reel Strips), linii płatnych (Paylines) oraz tabeli wypłat (Paytable).
- `rtp_convergence.png` - Wygenerowany wykres stabilności statystycznej.

## Jak uruchomić
1. Sklonuj repozytorium:
   ```bash
   git clone [https://github.com/TwojUser/slot-math-engine.git](https://github.com/TwojUser/slot-math-engine.git)
