import numpy as np
import matplotlib.pyplot as plt
from numpy_simulation import run_numpy_simulation 

def analyze_player_sessions(wins_per_spin, initial_balance=100, bet_size=1, sessions=1000, max_spins=500):
    """
    Simulates multiple player sessions to calculate Ruin Probability and visualize balance swings.
    """

    session_results = np.random.choice(wins_per_spin, size=(sessions, max_spins))

    net_outcomes = (session_results * bet_size) - bet_size
    
    balance_histories = initial_balance + np.cumsum(net_outcomes, axis=1)
    
    ruined_sessions = np.any(balance_histories <= 0, axis=1)
    ruin_probability = np.mean(ruined_sessions) * 100
    
    def get_session_end(history):
        ruin_points = np.where(history <= 0)[0]
        return ruin_points[0] + 1 if len(ruin_points) > 0 else max_spins
    
    session_lengths = [get_session_end(h) for h in balance_histories]
    avg_session_length = np.mean(session_lengths)
    median_length = np.median(session_lengths)

    print(f"--- ANALIZA SESJI GRACZA ({sessions} sesji po {max_spins} spinów) ---")
    print(f"Początkowy balans: {initial_balance} | Stawka: {bet_size}")
    print(f"Probability of Ruin: {ruin_probability:.2f}%")
    print(f"Średnia długość sesji: {avg_session_length:.1f} spinów")
    print(f"Mediana długości sesji: {median_length:} spinów")

    plt.figure(figsize=(12, 7))
    
    for i in range(min(50, sessions)):
        color = 'red' if ruined_sessions[i] else 'green'
        alpha = 0.3

        end_idx = session_lengths[i]
        plt.plot(range(end_idx), balance_histories[i][:end_idx], color=color, alpha=alpha)

    plt.axhline(y=initial_balance, color='black', linestyle='--', label='Start Balance')
    plt.axhline(y=0, color='red', linewidth=2, label='Ruin Line (0)')
    
    plt.title(f'Wahania kapitału: {sessions} sesji (Czerwony = Bankructwo, Zielony = Przetrwanie)')
    plt.xlabel('Numer spinu')
    plt.ylabel('Balans gracza (PLN)')
    plt.grid(True, alpha=0.2)
    plt.legend(['Start Balance', 'Ruin Line (0)', 'Sesje graczy'])  
    
    plt.savefig('balance_swings.png')
    print("\nWykres 'balance_swings.png' został wygenerowany.")
    
    return ruin_probability

def plot_win_distribution(wins_per_spin):
    # Filtrujemy tylko wygrane większe od 0
    winning_payouts = wins_per_spin[wins_per_spin > 0]
    
    plt.figure(figsize=(10, 6))
    plt.hist(winning_payouts, bins=50, color='skyblue', edgecolor='black', log=True)
    
    plt.title('Rozkład wielkości wygranych (Skala logarytmiczna)')
    plt.xlabel('Mnożnik wygranej (x Bet)')
    plt.ylabel('Częstotliwość występowania (Log)')
    plt.grid(axis='y', alpha=0.3)
    
    plt.savefig('win_distribution.png')
    print("\nWykres: 'win_distribution.png' został wygenerowany.")

if __name__ == "__main__":

    from numpy_simulation import run_numpy_simulation
    print("Rozpoczynanie symulacji")
    all_wins = run_numpy_simulation(10000000) # Na potrzeby testu 10 mln wystarczy
    
    analyze_player_sessions(all_wins, initial_balance=100, bet_size=1, sessions=1000, max_spins=500)
    plot_win_distribution(all_wins)