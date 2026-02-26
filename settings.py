SYMBOLS = {
    "H1": {"value": 20, "name": "Seven"},
    "M1": {"value": 5, "name": "Bar"},
    "L1": {"value": 0.5, "name": "Cherry"},
    "L2": {"value": 0.5, "name": "Lemon"},
    "W":  {"value": 500, "name": "Wild"}
}

REELS = [
    ["H1", "L1", "L2", "M1", "L2", "W", "L2", "L1", "M1", "H1", "L2", "L1", "L2", "M1", "L1", "W", "H1", "L2", "L2", "M1", "L2", "L2", "L2", "L1", "L2", "M1", "L2", "L2", "W", "L2", "L2", "L1", "L2"],

    ["L1", "L1", "L1", "W", "L1", "L1",  "L1", "H1", "L2", "L1", "L1", "L1", "H1", "L1",  "W", "L1", "M1", "L1", "L2", "L1", "H1", "L1", "H1", "L1", "L1", "L1", "L1"],
    
    ["L2", "L1", "M1", "L2", "L2", "L2", "M1", "L2", "L2", "H1", "M1", "W", "L2", "L2", "L2", "M1", "L2", "L1", "L2", "L2", "L2", "L2", "L2", "M1", "L2", "M1", "L2", "M1", "L2", "L2", "L2", "L2", "L2", "M1", "L2", "L2", "L2", "L2", "M1"]
]

PAYLINES = [
    [0, 0, 0],  # Linia 1: górny rząd
    [1, 1, 1],  # Linia 2: środkowy rząd
    [2, 2, 2],  # Linia 3: dolny rząd
    [0, 1, 2],  # Linia 4: ukośna z lewej do prawej (góra-środek-dół)
    [2, 1, 0]   # Linia 5: ukośna z lewej do prawej (dół-środek-góra)
]