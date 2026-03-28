#!/usr/bin/env python3
"""
Implementierung von Knuths "Claude's Cycles"-Konstruktion.

Problem: Digraph mit m³ Knoten ijk (0≤i,j,k<m), drei Bögen von jedem Knoten:
  - nach i+jk (bump i)
  - nach ij+k (bump j)
  - nach ijk+ (bump k)
  wobei x+ = (x+1) mod m

Aufgabe: Zerlege die Bögen in drei gerichtete m³-Zyklen.

Knuths Lösung (für ungerades m > 2):
Ordne jedem Knoten ijk eine Permutation der drei Richtungen zu,
abhängig von s = (i+j+k) mod m.

Zyklus c=0 ("Claude's first cycle"):
  s=0:          bump i wenn j=m-1, sonst bump k
  0 < s < m-1:  bump k wenn i=m-1, sonst bump j
  s=m-1:        bump k wenn i=0,   sonst bump j

Zyklus c=1 (aus dem Anhang):
  s=0:          bump j
  0 < s < m-1:  bump i
  s=m-1, i>0:   bump k
  s=m-1, i=0:   bump j

Zyklus c=2 (aus dem Anhang):
  s=0, j<m-1:   bump i
  s=0, j=m-1:   bump k
  0<s<m-1, i<m-1: bump k
  0<s<m-1, i=m-1: bump j
  s=m-1:        bump i
"""


def bump(x, m):
    return (x + 1) % m


def successor_c0(i, j, k, m):
    s = (i + j + k) % m
    if s == 0:
        if j == m - 1:
            return (bump(i, m), j, k)
        else:
            return (i, j, bump(k, m))
    elif s == m - 1:
        if i == 0:
            return (i, j, bump(k, m))
        else:
            return (i, bump(j, m), k)
    else:  # 0 < s < m-1
        if i == m - 1:
            return (i, j, bump(k, m))
        else:
            return (i, bump(j, m), k)


def successor_c1(i, j, k, m):
    s = (i + j + k) % m
    if s == 0:
        return (i, bump(j, m), k)
    elif s == m - 1:
        if i > 0:
            return (i, j, bump(k, m))
        else:
            return (i, bump(j, m), k)
    else:  # 0 < s < m-1
        return (bump(i, m), j, k)


def successor_c2(i, j, k, m):
    s = (i + j + k) % m
    if s == 0:
        if j < m - 1:
            return (bump(i, m), j, k)
        else:
            return (i, j, bump(k, m))
    elif s == m - 1:
        return (bump(i, m), j, k)
    else:  # 0 < s < m-1
        if i < m - 1:
            return (i, j, bump(k, m))
        else:
            return (i, bump(j, m), k)


def follow_cycle(start, successor_fn, m):
    """Verfolge den Zyklus beginnend bei start, gib alle Knoten zurück."""
    path = [start]
    cur = successor_fn(*start, m)
    while cur != start:
        path.append(cur)
        cur = successor_fn(*cur, m)
    return path


def verify_decomposition(m):
    """
    Überprüfe dass die drei Zyklen eine gültige Zerlegung bilden:
    - Jeder Zyklus hat Länge m³
    - Jeder Bogen erscheint in genau einem Zyklus
    - Alle m³ × 3 Bögen sind abgedeckt
    """
    all_vertices = [(i, j, k) for i in range(m) for j in range(m) for k in range(m)]

    # Alle möglichen Bögen
    all_arcs = set()
    for v in all_vertices:
        i, j, k = v
        all_arcs.add((v, (bump(i,m), j, k)))  # bump i
        all_arcs.add((v, (i, bump(j,m), k)))  # bump j
        all_arcs.add((v, (i, j, bump(k,m))))  # bump k

    assert len(all_arcs) == 3 * m**3, f"Erwarte {3*m**3} Bögen, habe {len(all_arcs)}"

    successors = [successor_c0, successor_c1, successor_c2]
    covered_arcs = set()

    for c, succ_fn in enumerate(successors):
        # Starte bei (0,0,0) und verfolge den Zyklus
        cycle = follow_cycle((0, 0, 0), succ_fn, m)

        if len(cycle) != m**3:
            return False, f"Zyklus c={c}: Länge {len(cycle)} statt {m**3}"

        for v in cycle:
            arc = (v, succ_fn(*v, m))
            if arc in covered_arcs:
                return False, f"Bogen {arc} doppelt abgedeckt"
            covered_arcs.add(arc)

    if covered_arcs != all_arcs:
        missing = all_arcs - covered_arcs
        extra = covered_arcs - all_arcs
        return False, f"Bögen fehlen: {len(missing)}, extra: {len(extra)}"

    return True, "OK"


if __name__ == "__main__":
    print("Überprüfe Knuths Claude's-Cycles-Konstruktion für ungerade m:\n")

    for m in [3, 5, 7, 9, 11]:
        valid, msg = verify_decomposition(m)
        status = "✓" if valid else "✗"
        print(f"  m={m:2d}: {status} {msg}")

    print("\nZeige Zyklus c=0 für m=3:")
    cycle = follow_cycle((0, 2, 2), successor_c0, 3)
    print("  " + " → ".join(f"{''.join(map(str,v))}" for v in cycle[:9]) + " → ...")
    print(f"  Länge: {len(cycle)}")

    print("\nVergleich mit Knuths Beispiel in der Note:")
    knuth_example = [
        (0,2,2),(0,0,2),(0,0,0),(0,0,1),(0,1,1),(0,1,2),(0,1,0),(0,2,0),(0,2,1),
        (1,2,1),(1,0,1),(1,1,1),(1,1,2),(1,2,2),(1,0,2),(1,0,0),(1,1,0),(1,2,0),
        (2,2,0),(2,2,1),(2,0,1),(2,0,2),(2,0,0),(2,1,0),(2,1,1),(2,1,2),(2,2,2),
    ]
    matches = (cycle == knuth_example)
    print(f"  Stimmt mit Knuths Beispiel überein: {'✓' if matches else '✗'}")
    if not matches:
        for i, (a, b) in enumerate(zip(cycle, knuth_example)):
            if a != b:
                print(f"  Erste Abweichung bei Index {i}: mein {a} vs Knuth {b}")
                break
