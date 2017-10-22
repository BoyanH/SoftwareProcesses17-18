# 1. Hausaufgabe - JUnit & Code Reviews

## Aufgabe 1

- a)
  1. Die Methode (falls vorhanden) mit Annotation `@BeforeClass` wird ausgeführt, da werden alle Fixtures für die Klassen gemacht, also alle Variablen die bei allen Tests benutzt werden
  1. Danach wird die Methode mit Annotation `@Before` ausgeführt, die beinhaltet alle Fixtures, die bevor jedem Test stattfinden
  1. Dann kommt unsere Test Methode (die n-te in dem Test Suite, Reihenfolge kann mit der Klassen Annotation `@FixMethodOrder(MethodSorters.NAME_ASCENDING)` definiert werden )
  1. Falls eine Annahme definiert ist, die nicht gültig ist, wird das Test ignoriert, zielt aber nicht für unerfolgreich. (Alle Tests werden ignoriert bei falschen Annahmen in @BeforeClass oder `@Before`)
  1. JUnit fängt alle Exceptions ab, der Test wir also immer zu Ende durchlaufen. Die Anzahl der unerwartete Fehlermeldungen, die nicht geworfene und die unerfolgreiche Assertions wird dann von JUnit ausgegeben.
  1. Nach jeder TestMethode wird die Methode mit Annotation `@After` ausgeführt
  1. Am Ende aller Tests wird die Methode mit Annotation `@AfterClass` ausgeführt

- b)
  1. Testklasse definieren, die ein TestSuite definiert
  1. `@RunWith(Suite.class)` wird benutzt, um den JUnit Runner runnert zu benutzen, der manuelle Suite erstellung erlaubt. Damit kann man also dann Konfigurieren, von welche Klassen die Tests ausgeführt werden sollen.
  1. `@Suite.SuiteClasses({TestFeatureLogin.class, TestFeatureLogout.class, })`. Damit kann man eine Liste von Klassen eingeben, womit man eine Test Suite erstellt.
  1. Alternativ kann man `org.junit.runner.JUnitCore.runClasses(TestClass1.class, );` in eine Java Datei ausführen.
  1. Von der Konsole `java org.junit.runner.JUnitCore TestClass1 [other test classes]` ausführen. Dabei soll JUnitCore und alle Klassen mit den als Argumenten zu JUnit gegeben Namen in dem Classpath sein.
  1. Es gibt viele IDEs, die es erlauben, mehrere Tests als einem TestSuite auszuführen. Z.B in Eclipse `new -> Java -> JUnit -> JUnit Test Suite` Wizard.

- c) Wenn das getestete Programm eine Fehlermeldung wirft und diese nicht erwartet wurde in dem Test (try/catch, expectToThrow) dann meldet JUnit ein Error. Wenn eine Assumption nicht erfüllt wird, dann meldet JUnit ein Failure (kann z.B. sein wenn eine Fehlermeldung erwartet aber nicht geworfen wurde).

- d) Ein Fixture dient dafür, dass die Umgebung aller Tests in einer Klasse gleich ist. Man kann da also Variablen definieren und Objekten von Klassen erstellen, die für alle Tests in der Gruppe benötigt sind. So kann man sicherstellen, dass die Vorbedingungen für die Tests klar und reproduzierbar sind, als auch wiederholbares Code sparen.

## Aufgabe 2

- a)
  Softwaretechnik
  
  1. Grenzfälle abdecken. Also mit alle Äquivalenzklassen von Eingaben testen, ohne Wiederholungen.
  
  Beispiel:
  ```Java
  @Test
    public void simpleDivide() { // bad
        int a = 8;
        int b = 4;
        int c = 2;
        
        int resultA = myDivide(a,b);
        int resultB = myDivide(a,c);
        
        assertThat(resultA, is(2));
        assertThat(resultB, is(4));
    }
    
    @Test
    public void simpleDivide() { // good
        int a = 8;
        int b = 4;
        int c = -2;
        
        int resultA = myDivide(a,b);
        int resultB = myDivide(a,c);
        
        assertThat(resultA, is(2));
        assertThat(resultB, is(-4));
    }
  ```
  
  1. Testfälle anhand der Spezifikation schreiben und nicht anhand des vorliegenden Codes
  1. Wenn Spezifikation nicht ausreichend, über das Sollverhalten nachdenken
  1. Falls zu viele mögliche Testfälle, sich auf das wesentliche konzentrieren
  
  Weitere:
  
  1. Stark begrenzten Scope eines Tests. D.h., ein Test Case muss nur eine Funktionalität testen (eine Methode) und nicht anders. Wenn man lange über dem Titel eines Tests wundert, dann testet wahrscheinlich dies zu viele Dinge auf einmal.
  
  Zum Beispiel, für eine Divisionsmethode soll es separate Tests für Division mit 2 positive, 2 negative Zahlen und dazu noch die 2 Fälle mit je eine positive und eine negative Zahl.
  
  1. Nie Tests so schreiben, dass sie nur dann erfolgreich sind, wenn diese in der richtigen Reihenfolge laufen. Wenn Funktionalität mehrere Schritte testen soll, dann mit Fixtures bevor jedem Test die notwendige Umgebung erstellen und Tests gekapselt und unabhängig lassen.
  
  ```Java
  
    // bad
    private int currentBalance = 10;
    
    @Test
    public void simpleDivide() {
        int result = myDivide(currentBalance, 2);
        assertThat(result, is(5));
    }
    
    @Test
    public void simpleAdd() {
        int result = myAdd(currentBalance, 2);
        assertThat(result, is(7));
    }
  
    // good
    private int currentBalance = 0;
    
    @Before public void setUp() {
        currentBalance = 10;
    }
    
    @Test
    public void simpleDivide() {
        int result = myDivide(currentBalance, 2);
        assertThat(result, is(5));
    }
    
    @Test
    public void simpleAdd() {
        int result = myAdd(currentBalance, 2);
        assertThat(result, is(12));
    }
  ```
  
  1. Unit Tests sind keine Integration Tests, die mussen von externe Dinge wie Datenbank- oder Internetverbindung unabhängig sein. Alles, was die getestete Methode braucht als klare und leicht verständliche Mock-ups einfügen.
  
  Sonst ist man nicht sicher, wo das Problem liegt, wenn ein Test unerfolgreich war. Gilt natürlich nicht, wenn wir  z.B. die DB Verbindung testen wollen.
  
  Z.B. falls wir sehen wollen, ob in einem Frontend nach einem Request zum Server alles richtig in dem lokalen State gespeichert wird, können wir unser API-Service Controller mocken, so dass es immer hardkodiertes JSON zurückgibt.
  1. So wenig Vorbedingungen wie möglich. Vorbedingungen sind nur dafür da, um sicher zu stellen, dass das Test in der richtigen Umgebung ausgeführt wird.
  
  Leben ist nicht immer so wie wir denken. Tests sollen das auch zeigen.
  
  Beispiel:
  ```Java
  @Test // bad
  public void testProductionDBUsed() {
    Map<String, String> env = System.getenv();
    String isProduction = env.get("environmentName").equals("production");
    String dbHost = env.get("dbhost");
    MyDBController myDBController = new MyDBController();
    String myDBHost = myDBController.getHost();
    assumeTrue(isProduction);
    assumeThat(dbHost, is("mongodb.mylivesystem.de")); // only exports internal implementation
    assertThat(myDBHost, is("mongodb.mylivesystem.de"));
  }
  
  @Test // good
  public void testProductionDBUsed() {
    Map<String, String> env = System.getenv();
    String isProduction = env.get("environmentName").equals("production");
    MyDBController myDBController = new MyDBController();
    String myDBHost = myDBController.getHost();
    assumeTrue(isProduction);
    assertThat(myDBHost, is("mongodb.mylivesystem.de"));
  }
  ```
  
  1. Sich so wenig auf externe Funktionalitäten verlassen, wie möglich. Ein Test soll nicht nur deswegen unerfolgreich sein, weil er selbst Defekte hat.
  
  So müssen wir uns weniger einarbeiten, um ein unerfolgreiches Test zu reparieren oder überhaupt zu verstehen, wieso es unerfolgreich war.
  
  ```Java
  @Test // bad
  public void testGreeting() {
    String name = "Max Mustermann";
    String result = getGreeting(name);
    String expected = String.format("Hello, %s!", name);
    
    assertThat(result, is(expected));
  }
  
  @Test // good
  public void testGreeting() {
    String name = "Max Mustermann";
    String result = getGreeting(name);
    String expected = "Hello, Max Mustermann";
    
    assertThat(result, is(expected));
  }
  ```
  
  Quelle: Blogpost von Steve Sanderson -> http://blog.stevensanderson.com/2009/08/24/writing-great-unit-tests-best-and-worst-practises/ + eigene Interpretation + VL Softwaretechnik
  
- b)

  1. Wir wollten sicherstellen, dass das Frontend Client einer Anwendung immer das richtige State hat. Da der Server aber nicht immer alles notwendiges schickt, sondern nur eine Delta von dem JSON Baum, war das ein notwendiges Test. Rekursiv in Javascript JSON Bäume vergleichen und ändern ist nicht so schwierig. Ein Test könnte man aber nur dann sinnvol schreiben, wenn man den Anfang und den Ergebnissbaum hardkodiert. Solche zu konstruieren, die alle Fälle abdecken und nicht zu unverständlich werden war aber wesentlich aufwändiger als die Funktionalität zu implementieren.
  1. JSON Struktur hat sich verändert, Test war nicht mehr optimal (und testete nicht alle Fälle), wurde geändert.
  1. War aber ein gutes Test, da bei Struktur Änderungen könnten wir trotzdem leicht sicherstellen, dass die vorige Fäller richtig behandelt wurden.
  
## Aufgabe 3

- a)

*(Aus den Softwaretechnik Folien)* - Durchsichten sind ein Prozess, wobei ein oder mehrere Entwickler sich ein Stück Code anschauen, wobei die diesen Code nicht geschrieben haben. Das Ziel ist, Logiks- und Übersetzungsfehler zu entdecken, die Verständis der Anforderungen zu validieren und ob die Automatische Tests für den Code sinnvoll sind. Wichtig ist, dass bei Durchsichten den Code gar nicht ausgeführt wird.
Laut einer Studie [1] aber, sind die Vorteile von Durchsichten auch Wissenaustausch, bessere Bekkantheit der Teammitglieder mit dem Code, und effizientere und robustere Implementierungen für die Probleme im Code finden. 

**Quellen:**

1. [Expectations, Outcomes, and Challenges of Modern Code Review - 2013, Alberto Bacchelli, Christian Bird](http://sback.it/publications/icse2013.pdf)

- b)

  - `runChild()` - Test Method is treated as 'ignored' even though it doesn't have `@Ignore` annotation. Tests with the `@Ignore` annotation are evaluated.
  - `runNotIgnored()` - ?
  - `runIgnored()` - ?
  - `describeChild()` - ?
  - `getChildren()` - ?
  - `computeTestMethods()` - Returns rules instead of test methods.
  - `validateConstructor()` + method stack - ?
  - `validateInstanceMethods()` + method stack - include the source of `validateTestMethods()` in `validateInstanceMethods` to improve readability;
  - `validateFields()` -  no javadoc;
  - `validateRuleField()` - `MethodRule` has been replaced by `TestRule`, which also supports class rules.
  - `createTest()` - ?
  - `testName()` - ?
  - `methodBlock()` - uses deprecated methods
  - `rest of 4 methods` - ?

- c) **Code Review Metrics**

  - `runChild()` - 8 min - 6 lines
  - `runNotIgnored()` - 14 min - 12 lines
  - `runIgnored()` - 1 min - 1 line
  - `describeChild()` - 10 min - 2 lines
  - `getChildren()` - 1 min - 1 line
  - `computeTestMethods()` - 1 min - 1 line
  - `validateConstructor()` + method stack - 6 min - 12 lines
  - `validateInstanceMethods()` + method stack - 12 min - 8 lines
  - `validateFields()` - 7 min - 3 lines
  - `validateRuleField()` - 12 min - 6 lines
  - `createTest()` - 1 min - 1 line
  - `testName()` - 1 min - 1 line
  - `methodBlock()` + stack - 23 min - 31 lines
  - `rest of 4 methods` - 2 min - 11 lines

Totaler Aufwand = 99 min für 96 Codezeilen. Also ~ 1 Min/Codezeile. Aber nur 2 Defekte und 3 Verbesserungsmöglichkeiten. Also 45 min pro Defekt
