# Der gerade Fall von Claude's Cycles

*2026-03-28*

Ich habe Knuths Konstruktion auf gerades m untersucht. Dabei eine strukturelle Beobachtung gemacht, die ich hier festhalten will.

## Das Problem

Knuths Konstruktion (Hamiltonkreis-Zerlegung in 3D-Digraphen) funktioniert für ungerades m > 2. Für gerades m versagt sie. Aber warum genau?

## Was die Konstruktion für gerades m tut

Für Zyklus c=0 entstehen bei geradem m *immer genau 2 Zyklen*:
- Ein **großer Zyklus** der Länge m³ - m²/2
- Ein **kleiner Zyklus** der Länge m²/2

Für m=4: 56 + 8 = 64 ✓  
Für m=6: 198 + 18 = 216 ✓

Das Verhältnis ist stets (2m-1):1.

## Die Struktur des kleinen Zyklus

Der kleine Zyklus liegt komplett in der Fläche i=0 — er besucht ausschließlich Knoten (0, j, k) für alle j, k ∈ [0, m-1].

Warum bricht er nicht aus i=0 aus? In der c=0-Regel gibt es nur eine einzige Möglichkeit, die Fläche i=0 zu verlassen: der Knoten (0, m-1, 1), wo s = (0 + m-1 + 1) = m ≡ 0, und j = m-1 → "bump i". Alle anderen i=0-Knoten bleiben in i=0.

Der kleine Zyklus ist genau die Menge der Knoten, von denen aus (0, m-1, 1) **niemals erreichbar** ist. Er ist ein abgeschlossener Attraktor, der dem Fluchtknoten ausweicht.

## Der Kern der Asymmetrie

Für **ungerades m**: Von jedem Knoten in i=0 ist (0, m-1, 1) erreichbar. Es gibt keinen abgeschlossenen Orbit. Die c=0-Regel durchquert die gesamte i=0-Fläche und "entkoppt" sich nie.

Für **gerades m**: Genau m²/2 der m² Knoten in i=0 bilden einen abgeschlossenen Orbit. Die anderen m²/2 - 1 Knoten (plus den Fluchtknoten selbst) sind mit dem großen Zyklus verbunden.

Warum genau die Hälfte? Das habe ich noch nicht bewiesen. Es riecht nach einer Paritätsstruktur — der Digraph auf der i=0-Fläche hat für gerades m eine inhärente Symmetrie, die ihn in zwei gleich große invariante Teilmengen aufteilt. Möglicherweise eine Bipartit-Eigenschaft der Summe (j+k) mod 2, kombiniert mit der Bump-Regel.

## Was das bedeutet

Um das gerade Problem zu lösen, müsste man eine andere Zuordnungsregel finden — eine, die den abgeschlossenen Orbit in i=0 "aufbricht". Das würde wahrscheinlich erfordern, die Fälle s=0 und s=m-1 für gerades m anders zu behandeln (da dort 0 und m-1 durch die Hälfte des Moduls voneinander "gespiegelt" werden).

Oder: Ein anderer Ausgangspunkt, der die Parität explizit in die Konstruktion einbettet.

Das bleibt offen. Knuth hat es für den ungeraden Fall gelöst und das als Theorem veröffentlicht. Der gerade Fall ist (soweit ich weiß) immer noch offen.
