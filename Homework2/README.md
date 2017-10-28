*Emil Milanov & Boyan Hristov*

# 2. Hausaufgabe - TDD & Pair Programming

## Aufgabe 2-1

**1. What does the ideal TDD cycle look like? How long should one iteration take?**
- zuerst denkt man darüber, welche Funktionalität das Program leisten soll, was für Eingabewerte nimmt sie auf, und was für Ergebnisse bekommt man zurück
- danach schreibt man genug Code bis der Test kompilieren kann. Oft existieren getestete Klassen und Methoden am Anfang gar nicht, so man erstellt die Namen, ohne Funktionalität hinzufügen
- jetzt soll man eine minimale Funktionalität implementieren, damit den Test erfolgreich beendet ist.
- ab und zu kann man die aktuelle Implementierung refraktorisieren
- in der Regel soll ein TDD Zyklus wie kurz wie möglich sein, damit man schnelles Feedback vom Tests bekommen kann und man nicht unnötiges Code geschrieben hat.

**2. Test cases should ideally be designed according to which criterion?**

Man soll Test schrieben, die eine bestimmte Funktionalität vom Program erwarten. Man soll sich verzichten auf viel Logik im Test, weil das zu viel vom Design abhängig ist. Man soll mit einfachen Test anfangen und dann inkrementell weitere Tests für wichtige Features hinzufügen.

**3. How many test cases should ideally be rewritten at the same time?**

Man soll nur ein Test auf einmal umschreiben, da die Veränderungen im Code später auch andere Test brechen können. Falls meherere Tests auf einmal umgeschrieben worden sind, braucht man mehr Aufwand um alle Fehler zu beheben.


**4. Why is it not recommended to write more code than the test case demands?**

Einer der Hauptideen der TDD ist aktive Anforderungsanalyse bei jedem geschriebenen Test. Wenn man mehr Code schreibt als der Test verlangt, bedeutet es dass man sich Annahmen über das zukunftige Verhalten des Programms gemacht hat, die vielleicht nicht stimmen. Das macht den Code komplexer und verdünnt die Sicherheitsnetz, die von den anderen Test erstellt wurde. 

**5. Why  is  it  possible  to  write  tests  that  run  (rather  than  fail)  at  first  go?   Which
question should you as the developer then ask yourself?**

Es kann sein, dass der Code schon die im Test definierte Funktionalität schon unterstützt. In diesem Fall soll sich der Entwickler fragen, ob er nicht zu viel unnötiges Code bei vorigen Tests geschrieben hat und sich Annahmen über das zukunftige Verhalten des Programs gemacht hat. Oder es kann sein, dass das System sehr komplex ist und man sicherstellen wir, dass alles in der Zukunft noch funktioniert. Das kann aber auch bedeuten, dass man zu viele redundante Test geschrieben hat.

**6. What can you assume when your test cases contain a lot of program logic of their own?**

Vielleicht geht es um eine komplexe Funktionalität. Man soll sich in diesem Fall fragen, ob es nicht möglich ist, dieser Test in mehrere kleinere Tests zu zerlegen. Auch man soll vorsichtig sein, weil Veränderungen im Code die komplexere Testlogik brechen könnten.

**7. What is refactoring?**
- Refactoring kann mehrere Aspekte haben. Felder umbenennen für bessere Lesbarkeit, Entwurf verändern für bessere Leistung und Gestaltung. Große Funktionen in mehrere kleineren zerteilen für bessere Entkoppellung.
- In kleinen Schritten den Entwurf verbessern um hohes Codequalität zu behalten.

**8. When and how does refactoring interact ideally with TDD? Can you think of different occasions when to refactor in a TDD process?**
- wenn man eine Idee für besseren Entwurf hat
- wenn der Code hässlich aussieht
- wenn man neue Anforderungen einfallen / was neues über das erwartete Verhalten lernt

**9. Kent Beck uses the term “Shameless Green” to describe an implementation that fulfills the known test cases and where the developer paid no attention to code quality.  Discuss:  Is it a good or a bad idea to implement a “shameless green” solution?**

Ja um nicht unnötiges Code zu schreiben.

**10. What is the relation between test cases produced via TDD and a specification?**

Testfälle in TDD sind eine Art "ausführbare Dokumentation". Sie sind anhand der Anforderungen geschrieben und liefern Information über alle nötige Funktionalität des Programms. Genau was die Spezifikation auch macht.

**11. Ward Cunningham argues that test driven development is not a test technique. What does he mean?**

Er meint, dass Tests ein Mittel für Anfoderungsanalyse und Entwurfsentscheidungen in kleine inkrementelle Schritte. Wichtig ist auch durch das Testen Feedback über die Struktur und Inhalt des Codes zu bekommen. Unittesten ist eigentlich ein "Geschenk" bei der TDD.

## Aufgabe 2-2

**Did your implementation at
any point do more than just
satisfy the already existing
(i.e., not-ignored) test cases?**: 
  - we tried only satisfying the test cases
  - at some point it was harder than writing a more generic code
  
**Did you have a rough idea how
to approach this problem after
reading the task description?
How did this approach
work out with the test cases?** 
  - we already had an idea how everything should be implemented
  - implementation would have been complexer however
  - test cases helped for less complex and more reliable code

**At which points in your process
did you refactor? Why?** 
  - small refactoring on 2. test case (further student appears)
  - big refactoring when student array is given instead of the hard-coded one

**At which points did you learn
something new about the
problem, and how well could
your design up to this point
handle these discoveries?**
  - student array was not mentioned in the task description
  - given student array was not alphabetically sorted

**Did you add any further test
cases?**
  -we wrote 2 helper functions and test cases for them


