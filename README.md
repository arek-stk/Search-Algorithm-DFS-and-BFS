# 🧩 Maze Pathfinder – StackGrenze / QueueGrenze

Dieses Projekt verwendet ein ASCII-Labyrinth (`labyrinth2.txt`), um Suchalgorithmen mit einer **Stack-basierten** bzw. **Queue-basierten Frontier** zu demonstrieren.

- **DFS (Depth-First Search)** → StackGrenze  
- **BFS (Breadth-First Search)** → QueueGrenze  

Das Labyrinth wird aus einer Textdatei geladen und vom Algorithmus Schritt für Schritt durchsucht, bis das Ziel gefunden wird.  
Am Ende wird ausgegeben, **wie viele Zustände (States)** benötigt wurden, um das Ziel zu erreichen.

---

## 🔄 BFS aktivieren

Um **Breadth-First Search (BFS)** zu verwenden, setze in der Methode:

```python
def solve(self, bfs=True):
den Parameter bfs=True.

bfs=True → BFS (QueueGrenze)

bfs=False → DFS (StackGrenze)

(Standardmäßig ist DFS aktiviert.)

## 📁 Projektstruktur
├── labyrinth2.txt # ASCII-Labyrinth
├── labyrinth.py #Suchalgorithmen BFS/DFS
├── README.md

---
🧱 Maze-Format (labyrinth2.txt)

Das Labyrinth besteht aus einfachen ASCII-Zeichen:

Symbol	Bedeutung
#	Wand (nicht begehbar)
.	Freier Weg
A	Startposition
B	Ziel
Beispiel:
#######
###..B#
#####.#
#.#####
#A#####

🧠 Suchalgorithmen
Depth-First Search (DFS)

Verwendet eine StackGrenze

Sucht tief in eine Richtung

Kein garantierter kürzester Weg

Breadth-First Search (BFS)

Verwendet eine QueueGrenze

Durchsucht das Labyrinth Ebene für Ebene

Garantiert den kürzesten Weg

Beim Auführen im Terminal:
python labyrinth.py labyrinth2.txt



