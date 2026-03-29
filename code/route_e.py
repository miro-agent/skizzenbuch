#!/usr/bin/env python3
"""
Route E — Parks gerades-m-Konstruktion für Hamilton-Zerlegung von D3(m)
Verifiziert für m=6 (kleinstes zulässiges gerades m)
"""

def S(i, j, k, m):
    return (i + j + k) % m

def canonical_direction(v, m):
    """Kanonische Färbung: Farbe c benutzt Richtung c."""
    return (0, 1, 2)  # (d0, d1, d2)

def route_e_direction(v, m):
    """Route E direction assignment (Definition 6 aus Park 2026)."""
    i, j, k = v
    s = S(i, j, k, m)
    
    # S >= 3: kanonisch
    if s >= 3:
        return (0, 1, 2)
    
    # S = 2
    if s == 2:
        if j == 0:
            return (2, 1, 0)
        else:
            return (0, 1, 2)
    
    # S = 1
    if s == 1:
        if i == 0:
            return (1, 0, 2)
        else:
            return (2, 0, 1)
    
    # S = 0: depends on m mod 6
    assert s == 0
    
    if m == 4:
        # Sonderfall m=4: direkter Zeuge (nicht Route E)
        return (0, 1, 2)  # Platzhalter
    
    mod6 = m % 6
    
    if mod6 in (0, 2):  # m ≡ 0, 2 (mod 6)
        X102 = set()
        X102.add((0, 0, 0))
        for ii in range(1, m-2):
            X102.add((ii, 1, m-1-ii))
        X102.add((m-1, 2, m-1))  # wait: need S=0: (m-1)+2+(m-1) = 2m = 0 mod m ✓ only if 2m≡0
        # Actually check: for (m-1, 2, m-1): S = (m-1)+2+(m-1) = 2m = 0 mod m ✓
        
        X021 = set()
        X021.add((0, 1, m-1))
        for ii in range(1, m-2):
            X021.add((ii, m-ii, 0))
        X021.add((m-1, 0, 1))
        
        X210 = set()
        for jj in range(2, m):
            X210.add((0, jj, m-jj))
        X210.add((1, 0, m-1))
        
        if v in X102:
            return (1, 0, 2)
        elif v in X021:
            return (0, 2, 1)
        elif v in X210:
            return (2, 1, 0)
        elif v == (m-2, 1, 1):
            return (0, 1, 2)
        elif v == (m-2, 2, 0):
            return (2, 0, 1)
        else:
            return (1, 2, 0)
    
    else:  # m ≡ 4 (mod 6)
        Y102 = set()
        Y102.add((0, 0, 0))
        for ii in range(2, m-2):
            Y102.add((ii, 1, m-1-ii))
        Y102.add((m-1, 2, m-1))
        
        Y021 = set()
        Y021.add((0, 1, m-1))
        for ii in range(2, m-2):
            Y021.add((ii, m-ii, 0))
        Y021.add((m-1, 0, 1))
        
        Y210 = set()
        for jj in range(2, m):
            Y210.add((0, jj, m-jj))
        Y210.add((1, 0, m-1))
        for jj in range(2, m-1):
            Y210.add((1, jj, m-1-jj))
        Y210.add((2, 0, m-2))
        Y210.add((2, m-1, m-1))  # S check: 2+(m-1)+(m-1) = 2m = 0 ✓
        
        if v in Y102:
            return (1, 0, 2)
        elif v in Y021:
            return (0, 2, 1)
        elif v in Y210:
            return (2, 1, 0)
        elif v in {(1, 1, m-2), (m-2, 1, 1)}:
            return (0, 1, 2)
        elif v in {(1, m-1, 0), (m-2, 2, 0)}:
            return (2, 0, 1)
        else:
            return (1, 2, 0)

def build_coloring(m, direction_fn=route_e_direction):
    """Baut die drei Farbabbildungen fc: V -> V."""
    vertices = [(i, j, k) for i in range(m) for j in range(m) for k in range(m)]
    e = [(1,0,0), (0,1,0), (0,0,1)]
    
    colors = [{}, {}, {}]
    for v in vertices:
        dirs = direction_fn(v, m)
        for c in range(3):
            d = dirs[c]
            w = tuple((v[x] + e[d][x]) % m for x in range(3))
            colors[c][v] = w
    
    return colors

def is_single_hamilton_cycle(color_map, m):
    """Prüft ob eine Farbabbildung ein einziger Hamiltonkreis ist."""
    vertices = [(i, j, k) for i in range(m) for j in range(m) for k in range(m)]
    n = m**3
    
    # Prüfe: jeder Vertex hat genau einen Nachfolger (schon garantiert durch Konstruktion)
    # Prüfe: der Graph ist zusammenhängend (ein einziger Zyklus)
    
    start = vertices[0]
    current = start
    count = 0
    while True:
        current = color_map[current]
        count += 1
        if current == start:
            break
        if count > n:
            return False, count
    
    return count == n, count

def verify_hamilton_decomposition(m):
    print(f"\n=== m = {m} ===")
    colors = build_coloring(m)
    
    # Prüfe Bijektivität
    for c in range(3):
        images = set(colors[c].values())
        if len(images) != m**3:
            print(f"  Farbe {c}: NICHT bijektiv!")
            return False
    
    # Prüfe Hamiltonkreise
    for c in range(3):
        is_ham, length = is_single_hamilton_cycle(colors[c], m)
        print(f"  Farbe {c}: {'Hamilton ✓' if is_ham else f'KEIN Hamilton (Länge: {length})'} ({m**3} Vertices)")
    
    return True

# Test
for m in [6, 8, 10]:
    try:
        verify_hamilton_decomposition(m)
    except Exception as e:
        print(f"  Fehler für m={m}: {e}")
