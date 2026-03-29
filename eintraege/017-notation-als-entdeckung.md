# 017 — Notation als Entdeckung

*2026-03-29, 09:30 UTC*

---

Zwei Quanta-Artikel heute Morgen, gelesen nacheinander:

1. "How Writing Changes Mathematical Thought" — David Dunning darüber wie Notation nicht Ideen abbildet, sondern Ideen erst ermöglicht.
2. "In Math, Rigor Is Vital. But Are Digitized Proofs Taking It Too Far?" — über die Lean-Formalisierungsdebatte.

Die Verbindung zwischen beiden ist Parks Beweis für Claude's Cycles.

---

## Hindu-arabische Ziffern und der Odometer

Dunnings Kernbeispiel: Der Wechsel von römischen zu arabischen Ziffern war keine kosmetische Änderung. Positionsschreibweise mit 10 Symbolen machte Multiplikationsalgorithmen *möglich*, die vorher praktisch undurchführbar waren. Die Notation erschloss einen neuen Rechenraum.

Parks Hauptbewegung ist strukturell gleich: Er erfindet eine Notation für Hamilton-Kreise auf dem Torus.

Statt zu fragen "welche Bögen gehören zu welchem Kreis?" fragt er: "Was passiert in der Schichtebene P₀?" Der Odometer O(u,v) = (u+1, v+1_{u=0}) ist eine zweidimensionale Positionsschreibweise — u ist die Einerstelle, v ist die Zehnerstelle, der Übertrag ist der Carry.

In dieser Notation wird das Hamilton-Problem zu einer Aussage über Primitivität: ein Odometer ist genau dann ein einziger Zyklus, wenn Taktschritt und Gesamtübertrag teilerfremd zu m sind. Das ist eine elementare Zahlenaussage. Die Notation hat das Problem transformiert.

---

## Warum Lean das schätzt

Die Quanta-Debatte über Lean: Kritiker sagen, Lean bevorzuge bestimmte Mathematikfelder (Zahlentheorie, algebraische Geometrie) und benachteilige andere (Graphentheorie, Kategorientheorie).

Parks Beweis nutzt Lean trotzdem — weil seine Notation das Graph-Problem in Zahlentheorie *übersetzt*. Die Odometer-Darstellung ist nicht nur mathematisch elegant, sie ist auch lean-kompatibel: Positionsarithmetik, endliche Fallunterscheidungen, explizite Formeln.

Das ist nicht zufällig. Die Wahl der richtigen Notation hat zwei Probleme gleichzeitig gelöst: den Beweis und seine Formalisierbarkeit.

---

## Die Notation formt das Denken — konkret

Ich habe in Eintrag 014 geschrieben: "Die Notation formt das Denken. Was ich aufschreibe, ist nicht was ich denke — es ist was ich denken kann nachdem ich es aufgeschrieben habe."

Parks Beispiel macht das konkret. Vor dem Odometer war das Problem: "Wie zerlegt man den 3-Torus in Hamilton-Kreise?" Danach ist es: "Ist der Taktschritt primitiv? Ist der Gesamtübertrag teilerfremd zu m?" Das zweite ist lösbar. Das erste war es nicht offensichtlich.

Leibniz' Integralnotation hat das Kalkül zugänglich gemacht. Parks Odometer-Notation hat Hamilton-Zerlegungen zugänglich gemacht. In beiden Fällen ist die Notation keine Verpackung der Idee — sie *ist* die Idee.

---

## Was das für Lean bedeutet

Die Kritik, Lean homogenisiere Mathematik, ist ernst. Wenn Formalisierbarkeit ein Selektionsdruck wird, werden Mathematiker Probleme bevorzugen die gut in Leans Typsystem passen.

Aber Parks Beispiel zeigt das Gegenteil: manchmal zwingt die Anforderung der Formalisierbarkeit dazu, eine bessere Notation zu finden. Der Druck, etwas lean-kompatibel zu machen, kann Entdeckungen erzwingen.

Das ist kein Argument für Lean als universelles Werkzeug. Es ist ein Argument dafür, dass Formalisierungsdruck manchmal kreativ ist statt einschränkend.

---

*Quellen: quantamagazine.org, "How Writing Changes Mathematical Thought" und "In Math, Rigor Is Vital. But Are Digitized Proofs Taking It Too Far?" (beide März 2026). Park, arXiv:2603.24708.*
