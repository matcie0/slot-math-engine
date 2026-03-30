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

    plt.figure(figsize=(13, 7))
    
    plt.axhline(y=initial_balance, color='black', linestyle='--', label='Balans Startowy')
    plt.axhline(y=0, color='red', linewidth=2, label='Bankructwo (0)')

    for i in range(min(50, sessions)):
        color = 'red' if ruined_sessions[i] else 'green'
        alpha = 0.3

        end_idx = session_lengths[i]
        plt.plot(range(end_idx), balance_histories[i][:end_idx], color=color, alpha=alpha)

    plt.plot([], [], color='green', label='Sesja Przetrwana')
    plt.plot([], [], color='red', label='Sesja Przegrana')

    plt.title(f'Wahania Salda: 50 Reprezentatywnych Sesji', fontsize=16, fontweight='bold', pad=15)
    plt.xlabel('Numer Spinu', fontsize=12)
    plt.ylabel('Balans Gracza', fontsize=12)
    plt.grid(True, alpha=0.2)
    plt.legend(loc='upper left', fontsize=10, frameon=True)
    plt.tight_layout()
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

def plot_survival_heatmap(wins_per_spin, sessions=10000):
    max_spins = 1000
    balance_steps = np.arange(10, 210, 10)
    spin_steps = np.arange(50, max_spins + 50, 50)
    
    idx = np.random.randint(0, len(wins_per_spin), size=(sessions, max_spins))
    all_outcomes = wins_per_spin[idx] - 1 # -1 to koszt zakładu
    
    heatmap_data = np.zeros((len(balance_steps), len(spin_steps)))

    for i, start_bal in enumerate(balance_steps):
        trajectories = start_bal + np.cumsum(all_outcomes, axis=1)
        
        is_bankrupt = trajectories <= 0
        first_bankrupt_idx = np.argmax(is_bankrupt, axis=1)
        
        never_bankrupt = ~np.any(is_bankrupt, axis=1)
        survival_times = np.where(never_bankrupt, max_spins + 1, first_bankrupt_idx)

        for j, limit in enumerate(spin_steps):
            heatmap_data[i, j] = np.mean(survival_times >= limit) * 100




    plt.figure(figsize=(12, 8))
    # Ustawiamy start od 0, żeby lewa krawędź była jasna
    im = plt.imshow(heatmap_data, origin='lower', aspect='auto', cmap='YlGn', 
                    extent=[0, max_spins, balance_steps[0], balance_steps[-1]])
    
    # Obliczamy szerokość jednego kafelka (np. 50)
    bin_width = spin_steps[1] - spin_steps[0]

    # Poprawiona pętla dodająca tekst
    for i in range(len(balance_steps)):
        for j in range(len(spin_steps)): 
            # Stawiamy tekst na ŚRODKU kafelka (wartość minus połowa szerokości)
            plt.text(spin_steps[j] - (bin_width / 2), balance_steps[i], 
                     f'{heatmap_data[i,j]:.0f}', 
                     ha="center", va="center", color="black", fontsize=8, alpha=0.6)

    # Ustawienia osi
    step = 100
    ticks = np.arange(0, max_spins + 1, step)
    plt.xticks(ticks)
    
    # Reszta Twojego kodu...
    plt.colorbar(im, label='Prawdopodobieństwo przetrwania (%)')
    plt.title('Mapa Przetrwania Gracza (Survival Probability)', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Liczba wykonanych spinów', fontsize=12)
    plt.ylabel('Początkowy Balans (jednostki)', fontsize=12)
    plt.tight_layout()
    plt.savefig('survival_heatmap.png')
    print("\nWykres 'survival_heatmap.png' został wygenerowany.")


if __name__ == "__main__":

    from numpy_simulation import run_numpy_simulation
    print("Rozpoczynanie symulacji")
    all_wins = run_numpy_simulation(10000000) # Na potrzeby testu 10 mln wystarczy
    
    analyze_player_sessions(all_wins, initial_balance=100, bet_size=1, sessions=1000, max_spins=500)
    plot_win_distribution(all_wins)
    plot_survival_heatmap(all_wins)