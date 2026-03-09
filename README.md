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
