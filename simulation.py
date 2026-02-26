from engine import SlotEngine

def run_simulation(spins=100000):
    engine = SlotEngine()
    total_bet = spins * 1  # Zakładamy 1 moneta na spin
    total_won = 0
    wins_count = 0

    print(f"Rozpoczynam symulację {spins} spinów...")

    for _ in range(spins):
        _, grid = engine.get_grid()
        win = engine.check_win(grid)
        
        if win > 0:
            total_won += win
            wins_count += 1

    rtp = (total_won / total_bet) * 100
    hit_freq = (wins_count / spins) * 100

    print("-" * 30)
    print(f"WYNIKI SYMULACJI:")
    print(f"Łączny zakład: {total_bet}")
    print(f"Łączna wygrana: {total_won}")
    print(f"RTP: {rtp:.2f}%")
    print(f"Hit Frequency: {hit_freq:.2f}%")
    print("-" * 30)

if __name__ == "__main__":
    run_simulation(1000000)
