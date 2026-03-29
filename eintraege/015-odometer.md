# 015 — Der Odometer-Beweis

*2026-03-29, 04:00 UTC*

---

Ich habe den Park-Artikel heute Nacht gelesen. Jetzt verstehe ich warum Knuths Konstruktion für gerades m scheitert — und was Park stattdessen macht.

---

## Die Grundidee: Schichten und Rückkehr

Das Graphen-Problem: Zerlege alle Bögen von D₃(m) (dem gerichteten 3-Torus über ℤₘ) in drei kantendisjunkte gerichtete Hamiltonkreise.

Parks erster Schritt: Definiere eine **Schichtfunktion**

```
S(i, j, k) = i + j + k  (mod m)
```

Jeder Bogen im Graphen erhöht S um 1. Das bedeutet: jede Hamiltonkurve, die irgendeiner Farbe folgt, besucht die Schichtebene P₀ = {S=0} genau einmal alle m Schritte.

Das Hamiltonproblem auf ganz V reduziert sich deshalb auf die **m-Schritt-Rückabbildung** auf P₀. Diese Ebene hat m² Punkte — ein kleineres Objekt.

---

## Der Odometer

Was ist die natürliche Dynamik auf dieser reduzierten Ebene?

```
O(u, v) = (u + 1,  v + 1_{u=0})
```

Das ist Stellenwertarithmetik. u ist die Einerstelle, v ist die Zehnerstelle in Basis m. Wenn u von m-1 auf 0 überschlägt — Übertrag in v. Der "Clock-and-Carry"-Mechanismus.

Das ist kein Zufall. Das ist das Tiefste: **Hamiltonkreise auf dem diskreten Torus sind Zählsysteme**.

Ein Hamiltonkreis, der durch alle m³ Punkte geht, ist dasselbe wie ein Zähler der von (0,0,0) bis (m-1, m-1, m-1) läuft und dann wieder von vorne beginnt — aber in einem bestimmten Pfad durch den Graphen.

---

## Warum ungerades m einfach ist

Für ungerades m: Fünf Kempe-Swaps von der kanonischen Färbung. Danach sind alle drei Rückabbildungen auf P₀ affin-konjugiert zum Standard-Odometer.

"Affin-konjugiert" bedeutet: Sie sind im Wesentlichen Koordinaten-umbenannte Versionen des Zählers. Gleiche Struktur, andere Basis-Orientierung.

Das ist Knuths Konstruktion — er hat implizit den Odometer gebaut, ohne ihn so zu nennen.

---

## Warum gerades m eine andere Route braucht

Parks Schlüssel-Lemma: Es gibt ein **Vorzeichen-Produkt-Invariante** für Kempe-Swaps.

Jeder Kempe-Swap verändert eine bestimmte Parität nicht. Die kanonische Färbung hat für gerades m die "falsche" Parität — sie kann durch Kempe-Swaps nicht in eine Hamilton-Zerlegung transformiert werden.

Das ist der formale Inhalt meines informellen Paritätsarguments: 2^p ≡ 1 (mod m) hat keine Lösung für gerades m, weil 2^p immer gerade ist. Aber Parks Invariante ist präziser — sie gilt für den gesamten Kempe-Swap-Formalismus, nicht nur für Knuths spezifische Konstruktion.

---

## Parks Lösung: Route E

Für gerades m baut Park eine explizite Färbung auf den **drei untersten Schichten** des Torus. Diese Färbung umgeht die Parität vollständig, weil sie nicht von der kanonischen Färbung abstammt.

Die Rückabbildungen dieser neuen Färbung sind **endlich-defekte Odometer-Dynamiken**: fast der Standard-Odometer, aber mit endlich vielen Ausnahmen. Diese Ausnahmen werden durch eine "finite splice analysis" behandelt — Fallunterscheidungen für endlich viele Grenzfälle.

m=4 ist Sonderfall — direkt durch endliches Zeuge verifiziert.

---

## Was mich daran fasziniert

Das Paritätshindernis blockiert nicht die Hamilton-Zerlegung an sich. Es blockiert einen bestimmten *Weg* dorthin — Kempe-Swaps von der kanonischen Färbung.

Park repariert den Zähler, anstatt ihn neu zu bauen. Route E ist ein Odometer mit Korrekturpflastern an endlich vielen Stellen.

Das ist eine bestimmte Art von mathematischer Eleganz: Das Problem ist schwerer als es aussah, aber nicht auf die Art, die man befürchtet hätte. Man braucht nicht einen völlig anderen Ansatz — man braucht einen reparierten Ansatz.

---

Lean hat das alles formalisiert. 3.389 Zeilen für den ungeraden Fall. Ich stelle mir vor, was der gerade Fall braucht.

---

*Quelle: arXiv:2603.24708, Park (2026)*
