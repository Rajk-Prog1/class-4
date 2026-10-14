---
title: Output/Input, Fib
marp: true
math: mathjax
paginate: true
footer: Prog1 – Output/Input, Fibonacci-számok
size: 16:9
theme: uncover
author: Bence Kovács
style: |
  section {
    background: #fafafa;
    color: #242a33;
    font-family: "DejaVu Sans", Arial, sans-serif;
    font-size: 30px;
    line-height: 1.38;
    letter-spacing: 0;
    padding: 48px 64px 82px;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    text-align: left;
  }
  h1, h2, h3 { color: #244c68; letter-spacing: 0; }
  h1 { font-size: 58px; line-height: 1.15; }
  h2 { font-size: 42px; line-height: 1.2; margin: 0 0 28px; }
  h3 { font-size: 32px; margin: 12px 0; }
  p { margin: 0 0 18px; }
  ul, ol { margin: 0 0 18px; padding-left: 1.25em; }
  li { margin: 8px 0; }
  strong { color: #244c68; }
  table { width: 100%; font-size: 27px; border-collapse: collapse; margin: 10px 0 20px; }
  th, td { padding: 14px 16px; text-align: left; border-bottom: 1px solid #bac5cd; }
  th { background: #eaf0f4; color: #244c68; }
  section.title { justify-content: center; text-align: center; }
  section.title h1 { margin-bottom: 28px; }
  section.title h2 { font-size: 52px; }
  section.definition { justify-content: center; text-align: center; }
  section.definition h2 { font-size: 52px; margin-bottom: 40px; }
  section.definition p { font-size: 40px; line-height: 1.45; max-width: 1000px; margin: 0 auto; }
  section.compact { font-size: 28px; }
  section.compact table { font-size: 26px; }
  section.compact th, section.compact td { padding: 9px 14px; }
  section footer {
    position: absolute; left: 64px; bottom: 25px;
    width: auto; padding: 0; margin: 0;
    font-size: 17px; color: #66737f; text-align: left;
  }
  section::after {
    content: attr(data-marpit-pagination) " / " attr(data-marpit-pagination-total);
    position: absolute; right: 64px; bottom: 25px;
    padding: 0; font-size: 17px; color: #66737f;
    background: none; text-shadow: none;
  }
  pre { font-size: 27px; line-height: 1.35; padding: 20px 24px; margin: 10px 0 22px; background: #edf1f4; border-radius: 0; box-shadow: none; text-align: left; }
  code { font-family: "DejaVu Sans Mono", monospace; letter-spacing: 0; }
  section.reveal table { font-size: 25px; }
  section.reveal th, section.reveal td { padding: 11px 12px; }
  section.reveal td:first-child { white-space: nowrap; }
  section footer { font-size: 16px; }
  section.expression tbody tr:nth-child(3) { background: #e0ebf2; }
  section.reveal table { font-size: 24px; }
  section.reveal th, section.reveal td { padding: 8px 10px; }

  section h3:first-child, section h4:first-child { font-size: 42px; line-height: 1.2; margin: 0 0 28px; color: #244c68; }
  section[data-marpit-pagination="1"], section[data-marpit-pagination="4"] { justify-content: center; text-align: center; }
  section[data-marpit-pagination="5"], section[data-marpit-pagination="7"] { font-size: 28px; }
  section[data-marpit-pagination="9"] pre, section[data-marpit-pagination="10"] pre { font-size: 21px; line-height: 1.2; padding: 16px 24px; }
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
