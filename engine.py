import numpy as np
from settings import REELS, SYMBOLS, PAYLINES

class SlotEngine:
    def __init__(self):
        self.reels = REELS
        self.cols = len(REELS)
        self.rows = 3 
    
    def get_grid(self):
            grid = []
            stop_positions = []

            for reel in self.reels:
                reel_length = len(reel)
                # 1. Losujemy punkt startowy
                stop_pos = np.random.randint(0, reel_length)
                stop_positions.append(stop_pos)

                # 2. Wycinamy 3 symbole (z obsługą zawijania - modulo)
                column = []
                for i in range(self.rows):
                    index = (stop_pos + i) % reel_length
                    column.append(reel[index])
                
                grid.append(column)
            
            return stop_positions, grid
    
    def check_win(self, grid):
        total_payout = 0
        for line in PAYLINES:
            symbols = [grid[0][line[0]], grid[1][line[1]], grid[2][line[2]]]
            
            # 1. Znajdź pierwszy symbol, który NIE JEST Wildem
            target = next((s for s in symbols if s != "W"), "W")
            
            # 2. Sprawdź czy każdy symbol na linii to nasz 'target' ALBO 'W'
            is_winner = all(s == target or s == "W" for s in symbols)
            
            if is_winner:
                # Jeśli wygrały same Wildy, wypłać za najwyższy symbol (np. H1)
                payout_key = "H1" if target == "W" else target
                total_payout += SYMBOLS[payout_key]["value"]
                
        return total_payout
            

    def print_grid(self, grid):
            """Pomocnicza funkcja do ładnego wyświetlania w terminalu."""
            print("------------")
            for row in range(self.rows):
                display_row = []
                for col in range(self.cols):
                    display_row.append(grid[col][row].ljust(2))
                print(f"| {' '.join(display_row)} |")
            print("------------")

if __name__ == "__main__":
    engine = SlotEngine()
    pos, grid = engine.get_grid()
    win = engine.check_win(grid)
    print(f"Pozycje zatrzymania: {pos}")
    engine.print_grid(grid)
    if win:
        print(f"Twoje wygrane: {win}") 
    else:
        print("Spróbój jeszcze raz")