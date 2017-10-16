### Homework 1

## Exercise 1

- a)
  1. Die Methode (falls vorhanden) mit Annotation `@BeforeClass` wird ausgeführt, da werden alle Fixtures für die Klassen gemacht, also alle Variablen die bei allen Tests benutzt werden
  1. Danach wird die Methode mit Annotation `@Before` ausgeführt, die beinhaltet alle Fixtures, die bevor jedem Test stattfinden
  1. Dann kommt unsere Test Methode (die n-te in dem Test Suite, Reihenfolge kann mit der Klassen Annotation `@FixMethodOrder(MethodSorters.NAME_ASCENDING)` definiert werden )
  1. Falls eine Annahme definiert ist, die nicht gültig ist, wird das Test ignoriert, zielt aber nicht für unerfolgreich. (Alle Tests werden ignoriert bei falschen Annahmen in @BeforeClass oder `@Before`)
  1. Die Test Methode wird ausgeführt, bis diese zu Ende ist, eine Fehler geworfen wurde und nicht abgefangen, oder ein Assertion nicht erfüllt wurde (`assertTrue`, `assertEquals`, `assertThat(x, is(5))`) (Da in JUnit bei nicht erfülltem Assertion ein AssertionError geworfen wird, alles wird in JVM ausgeführt)
  1. Nach jeder TestMethode wird die Methode mit Annotation `@After` ausgeführt
  1. Am Ende aller Tests wird die Methode mit Annotation `@AfterClass` ausgeführt

- b)
  1. Testklasse definieren, die ein TestSuite definiert
  1. `@RunWith(Suite.class)` wird benutzt, um den JUnit Runner runnert zu benutzen, der manuelle Suite erstellung erlaubt. Damit kann man also dann Konfigurieren, von welche Klassen die Tests ausgeführt werden sollen.
  1. `@Suite.SuiteClasses({TestFeatureLogin.class, TestFeatureLogout.class, ...})`. Damit kann man eine Liste von Klassen eingeben, womit man eine Test Suite erstellt.
  1. Alternativ kann man `org.junit.runner.JUnitCore.runClasses(TestClass1.class, ...);` in eine Java Datei ausführen.
  1. Von der Konsole `java org.junit.runner.JUnitCore TestClass1 [...other test classes...]` ausführen. Dabei soll JUnitCore und alle Klassen mit den als Argumenten zu JUnit gegeben Namen in dem Classpath sein.
  1. Es gibt viele IDEs, die es erlauben, mehrere Tests als einem TestSuite auszuführen. Z.B in Eclipse `new -> Java -> JUnit -> JUnit Test Suite` Wizard.

- c) Wenn das getestete Programm eine Fehlermeldung wirft und diese nicht erwartet wurde in dem Test (try/catch, exceptToThrow) dann meldet JUnit ein Error. Wenn eine Assumption nicht erfüllt wird, dann meldet JUnit ein Failure (kann z.B. sein wenn eine Fehlermeldung erwartet aber nicht geworfen wurde).

- d) Ein Fixture dient dafür, dass die Umgebung aller Tests in einer Klasse gleich ist. Man kann da also Variablen definieren und Objekten von Klassen erstellen, die für alle Tests in der Gruppe benötigt sind. So kann man sicherstellen, dass die Vorbedingungen für die Tests klar und reproduzierbar sind, als auch wiederholbares Code sparen.

