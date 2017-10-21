## 1. Hausaufgabe - JUnit & Code Reviews

### Aufgabe 1

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
  1. `@Suite.SuiteClasses({TestFeatureLogin.class, TestFeatureLogout.class, ...})`. Damit kann man eine Liste von Klassen eingeben, womit man eine Test Suite erstellt.
  1. Alternativ kann man `org.junit.runner.JUnitCore.runClasses(TestClass1.class, ...);` in eine Java Datei ausführen.
  1. Von der Konsole `java org.junit.runner.JUnitCore TestClass1 [...other test classes...]` ausführen. Dabei soll JUnitCore und alle Klassen mit den als Argumenten zu JUnit gegeben Namen in dem Classpath sein.
  1. Es gibt viele IDEs, die es erlauben, mehrere Tests als einem TestSuite auszuführen. Z.B in Eclipse `new -> Java -> JUnit -> JUnit Test Suite` Wizard.

- c) Wenn das getestete Programm eine Fehlermeldung wirft und diese nicht erwartet wurde in dem Test (try/catch, expectToThrow) dann meldet JUnit ein Error. Wenn eine Assumption nicht erfüllt wird, dann meldet JUnit ein Failure (kann z.B. sein wenn eine Fehlermeldung erwartet aber nicht geworfen wurde).

- d) Ein Fixture dient dafür, dass die Umgebung aller Tests in einer Klasse gleich ist. Man kann da also Variablen definieren und Objekten von Klassen erstellen, die für alle Tests in der Gruppe benötigt sind. So kann man sicherstellen, dass die Vorbedingungen für die Tests klar und reproduzierbar sind, als auch wiederholbares Code sparen.

### Aufgabe 2

- a)
  Softwaretechnik
  
  1. Grenzfälle abdecken. Also mit alle Äquivalenzklassen von Eingaben testen, ohne Wiederholungen.
  
  ...Beispiel:
  ...```Java
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
  1. Nie Tests so schreiben, dass sie nur dann erfolgreich sind, wenn diese in der richtigen Reihenfolge laufen. Wenn Funktionalität mehrere Schritte testen soll, dann mit Fixtures bevor jedem Test die notwendige Umgebung erstellen und Tests gekapselt und unabhängig lassen.
  
  ...```Java
  
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
  
  ...Sonst ist man nicht sicher, wo das Problem liegt, wenn ein Test unerfolgreich war. Gilt natürlich nicht, wenn wir  z.B. die DB Verbindung testen wollen.
  1. So wenig Vorbedingungen wie möglich. Vorbedingungen sind nur dafür da, um sicher zu stellen, dass das Test in der richtigen Umgebung ausgeführt wird.
  
  ...Leben ist nicht immer so wie wir denken. Tests sollen das auch zeigen.
  
  ...Beispiel:
  ...```Java
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
  
  ...So müssen wir uns weniger einarbeiten, um ein unerfolgreiches Test zu reparieren oder überhaupt zu verstehen, wieso es unerfolgreich war.
  
  ...```Java
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
  
  ...Quelle: Blogpost von Steve Sanderson -> http://blog.stevensanderson.com/2009/08/24/writing-great-unit-tests-best-and-worst-practises/ + eigene Interpretation
  
- b)

