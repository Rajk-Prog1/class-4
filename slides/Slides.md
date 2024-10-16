---
title: Output/Input, Fib
marp: true
math: mathjax
class: lead
paginate: false
footer: Prog1 - Prelogika
size: 16:9
theme: uncover
author: Bence Kovács
---

# Output/Input, Fibonacci-számok

---

## Input/Output

- input: Az az objektum, amely belép a program állapotába (pl. a felhasználótól kapott adat).
- output: Az az objektum, amely a program állapotából kilép, és máshol kerül felhasználásra (pl. egy számítás eredménye, ami megjelenik a képernyőn).

---

### Függvény

- PARAMÉTER – INPUT
  A függvény meghívásakor megadott paraméterek a függvény lokális keretébe kerülnek.

- VISSZATÉRÉSI ÉRTÉK – OUTPUT
  A függvény végrehajtása során a return utasítással egy eredmény (visszatérési érték) kerül ki a függvény lokális keretéből. Ez az eredmény átlép a függvényt meghívó környezetbe, ahol az eredményt fel lehet használni további műveletekhez.

---

## Fibonacci-számok: Egy matematikai sorozat költői gyökerekkel

---

A Fibonacci-sorozat az egyik legismertebb számsorozat a matematikában. Az első két elem 1, majd minden további szám az előző két szám összegéből adódik.

$F(1)=1$
$F(2)=1$
$F(n)=F(n−1)+F(n−2)$ ha $n>2$

A sorozat így néz ki: $1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...$

Ezek a számok lenyűgöző alkalmazásokkal rendelkeznek a természetben, az építészetben és a művészetben. Megjelennek a növények növekedési mintázataiban, a levelek elrendezésében, sőt a tengeri kagylók spiráljaiban is.

---

### Fibonacci-sorozat eredete és a nyulak példája

A **Fibonacci-sorozat** Leonardo Fibonacci nevéhez fűződik, aki a 13. században publikálta az „**Liber Abaci**” című könyvében.
Fibonacci a sorozatot egy nyulakkal kapcsolatos probléma megoldására használta.

- **Probléma**: Ha egy pár nyúl minden hónapban egy újabb pár nyulat hoz világra, és a nyulak soha nem halnak meg, hány pár nyúl lesz egy év alatt?

---

### Fibonacci és a szanszkrit költészet

Érdekes módon a Fibonacci-sorozat gyökerei az indiai kultúrában, különösen a szanszkrit költészetben is megtalálhatók. A szanszkrit verselésben a költők hosszú és rövid szótagok alapján szerkesztették verseiket, és bizonyos szótagminták a Fibonacci-sorozatot követik.

Ezt a felfedezést az indiai matematikus Pingala (Kr. e. 200 körül) tette, aki a költészet szótagmintáit elemezte, és felfedezte, hogy az $n$ hosszúságú szótagminták száma az $n$-edik Fibonacci-szám.

---

### Mi az a Rekurzió?

A **rekurzió** olyan programozási technika, amelyben egy függvény önmagát hívja meg a probléma megoldása során.

### Hogyan működik a rekurzió?

1. **Alapeset**: Minden rekurzív függvénynek tartalmaznia kell egy alapesetet, amely megállítja a további önhívásokat. Ez a "kilépési feltétel".
2. **Rekurzív eset**: Amíg az alapeset nem teljesül, a függvény önmagát hívja meg kisebb részfeladatokkal.

---

### Fibonacci-sorozat Pythonban

```python
def fib(n: int) -> int:
    """
    A n-edik Fibonacci-szám rekurzív kiszámítása.

    Paraméterek:
    n (int): A Fibonacci-sorozatban lévő pozíció.

    Visszatérés:
    int: A n-edik Fibonacci-szám.
    """
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
```

---

```python
def print_some_fib(start: int = 1, end: int = 40) -> None:
    """
    Fibonacci-számok nyomtatása a start és end tartományban (beleértve).

    Paraméterek:
    start (int): A Fibonacci-sorozat kezdő pozíciója.
    end (int): A Fibonacci-sorozat záró pozíciója.

    Visszatérés:
    None
    """
    for f in range(start, end + 1):
        print(f"{f}. Fibonacci: {fib(f)}")

# Példakód futtatása
print_some_fib()
```

---

### Mi az a Rekurzió?

Előnyök:

- Egyszerű és tiszta megoldás bizonyos problémákra (pl. matematikai sorozatok, fa-struktúrák).

Hátrányok:

- Mély rekurzió esetén memóriafogyasztás és lassúság léphet fel.

---

## Melyik programnyelven a leggyorsabb?

Versenyzőink:

- Python
- C++
- Java
- PHP

---

### Python

- Magas szintű, általános célú programozási nyelv.
- Dinamikus típusú, ami azt jelenti, hogy nem kell a változókat előre deklarálni.
- Könnyen olvasható, egyszerű szintaxis, amely közel áll a természetes nyelvhez.

---

#### Erősségek:

- **Egyszerű és olvasható**: Kód írása és olvasása egyszerű.
- **Széleskörű könyvtárak**: Sok beépített könyvtár, amelyek egyszerűvé teszik az adatelemzést, gépi tanulást, webfejlesztést stb.
- **Platformfüggetlen**: A Python kód különböző platformokon futtatható.

---

#### Gyengeségek:

- **Sebesség**: A Python lassabb lehet más nyelveknél, mivel interpreter nyelv, nem compiler.
- **Memóriahasználat**: Magas memóriaigényű lehet nagyobb projektek esetén.

---

### C++

- Magas szintű, statikusan típusos programozási nyelv.
- Közvetlen hozzáférést biztosít a memóriához, ezért gyakran használják rendszerszintű programozásra.
- Támogatja az objektum-orientált, procedurális és funkcionális programozási paradigmákat.
- ***

---

### Erősségek:

- **Gyors és hatékony**: Kiváló teljesítmény, mivel compiler nyelv. Alacsony szintű hozzáférést biztosít a hardverhez.
- **Kontroll a memóriakezelés felett**: Pontos memóriakezelés, amit más nyelvek, mint Python, nem biztosítanak.
- **Hordozhatóság**: Nagyon hordozható nyelv, különböző platformokon futtatható.

---

### Gyengeségek:

- **Komplex szintaxis**: A bonyolult szintaxis nehezebbé teszi a tanulást és a hibakeresést.
- **Memóriakezelési hibák**: Ha nem jól kezelik, könnyen memóriakezelési hibákat eredményezhet (pl. memória szivárgás).

---

### Java

- Magas szintű, statikusan típusos programozási nyelv, amely platformfüggetlen („írj meg egyszer, futtasd bárhol”).
- Objektum-orientált programozási nyelv, de támogatja az egyéb paradigmákat is.
- Java bytecode formátumban fut a Java Virtuális Gépen (JVM), ami lehetővé teszi a hordozhatóságot.

---

### Erősségek:

- **Platformfüggetlen**: A Java kód mindenhol ugyanúgy futtatható, ahol elérhető a JVM.
- **Stabilitás és skálázhatóság**: Nagyméretű, vállalati szintű alkalmazásokhoz tökéletes.
- **Biztonság**: Beépített biztonsági mechanizmusok a memóriakezeléshez és a JVM futtatási környezethez.

---

### Gyengeségek:

- **Sebesség**: A Java lassabb lehet más compiler nyelveknél, mint a C++, mivel a JVM-en fut.
- **Bonyolult memóriahasználat**: Bár automatikusan kezeli a memóriát (garbage collection), ez néha lassabb lehet.

---

### PHP

- Dinamikusan típusos, szkriptnyelv, amelyet leginkább webszerverek oldali fejlesztésre használnak.
- Könnyen integrálható HTML-be és adatbázisokkal, mint a MySQL.
- Széles körben használják webfejlesztésben, különösen dinamikus weboldalak készítéséhez.

---

### Erősségek:

- **Webfejlesztésre optimalizálva**: Kiválóan használható webszerverek oldali programozásra, sok webszerver támogatja natívan.
- **Egyszerű tanulni**: A szintaxis egyszerű, ideális kezdőknek webfejlesztésre.
- **Nagyon jól integrálható**: Könnyen kapcsolódik adatbázisokhoz és HTML-hez.

---

### Gyengeségek:

- **Biztonsági problémák**: Ha nem megfelelően használják, a PHP kódok könnyen támadhatók.
- **Sebesség**: Dinamikusan értelmezett, ami miatt lassabb lehet, mint a compiler nyelvek.
- **Nagyobb projektek nehézkes kezelése**: Nagyobb projektek esetén a PHP kódok nehezen karbantarthatóvá válhatnak.

---
