import numpy as np
from settings import REELS, PAYLINES, SYMBOLS

def run_numpy_simulation(spins=1000000):
    sym_to_id = {name: i for i, name in enumerate(SYMBOLS.keys())}
    id_to_val = np.array([s["value"] for s in SYMBOLS.values()])
    id_to_name = list(SYMBOLS.keys())
    wild_id = sym_to_id.get("W", -1) 
    wins_per_spin = np.zeros(spins)

    reels_data = [np.array([sym_to_id[s] for s in r]) for r in REELS]
    reel_lengths = np.array([len(r) for r in reels_data])

    stops = np.random.randint(0, reel_lengths, size=(spins, 3))

    grid_data = {}
    for col in range(3):
        for row in range(3):
            pos = (stops[:, col] + (row - 1)) % reel_lengths[col]
            grid_data[(col, row)] = reels_data[col][pos]

    win_counts = {name: 0 for name in SYMBOLS.keys()}

    for line in PAYLINES:
        s1, s2, s3 = grid_data[(0, line[0])], grid_data[(1, line[1])], grid_data[(2, line[2])]

        s1 = grid_data[(0, line[0])]
        s2 = grid_data[(1, line[1])]
        s3 = grid_data[(2, line[2])]

        target = np.where(s1 != wild_id, s1, np.where(s2 != wild_id, s2, s3))
        
        win_mask = ((s1 == target) | (s1 == wild_id)) & \
                   ((s2 == target) | (s2 == wild_id)) & \
                   ((s3 == target) | (s3 == wild_id))
        
        wins_per_spin[win_mask] += id_to_val[target[win_mask]]

        winning_targets = target[win_mask]

        unique, counts = np.unique(winning_targets, return_counts=True)
        for val_id, count in zip(unique, counts):
            win_counts[id_to_name[val_id]] += count
         
    total_won = np.sum(wins_per_spin)
    rtp = (total_won / spins) * 100
    stdev = np.std(wins_per_spin)
    volatility_index = stdev * 1.96
    winning_spins_count = np.count_nonzero(wins_per_spin)
    hit_frequency = (winning_spins_count / spins) * 100

    print(f"--- WYNIKI SYMULACJI NUMPY ({spins} spinów) ---")
    print(f"RTP: {rtp:.2f}%")
    print(f"Hit Frequency: {hit_frequency:.2f}%")
    print("\nLiczba trafionych linii per symbol:")
    for sym, count in win_counts.items():
        print(f" - {sym}: {count}")
    print(f"Standard Deviation: {stdev:.4f}")
    print(f"Volatility Index (95% CI): {volatility_index:.2f}")

if __name__ == "__main__":
    run_numpy_simulation(10000000)