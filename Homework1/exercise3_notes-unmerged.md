## Aufgabe 3

- b)
  - runChild: Zeile 68 hat die falsche if Bedingung, genau die ignorierte Klassen werden werden als ingnoriert bearbeitet und umgekehrt
  
  ```Java
    if (method.getAnnotation(Ignore.class) == null) {
		runIgnored(eachNotifier);
    } else {
	    runNotIgnored(method, eachNotifier);
	}
  ```
  - computeTestMethods: Es werden Methoden mit Annotation @Rule zurückgegeben und nicht solche mit @Test. Ist nicht wie in der Spezifikation; @Rule soll nur für Fields sein
  ```Java
  /**
	 * Returns the methods that run tests. Default implementation returns all
	 * methods annotated with {@code @Test} on this class and superclasses that
	 * are not overridden.
	 */
	protected List<FrameworkMethod> computeTestMethods() {
		return getTestClass().getAnnotatedMethods(Rule.class);
	}
  ```
  - methodBlock: es werden 4 deprecated
  Methoden benutzt.
  
  ```Java
    statement= possiblyExpectingExceptions(method, test, statement);
    statement= withPotentialTimeout(method, test, statement);
    statement= withBefores(method, test, statement);
	statement= withAfters(method, test, statement);
  ```
  
  - validateInstanceMethods: Validation für BeforeClass and AfterClass Methoden fehlt. Wäre gut wenn validateTestMethods auch computeTestMethods benutzt, validateTestMethods nur wenn solche vorhanden.
  
  ```Java
  @Deprecated
	protected void validateInstanceMethods(List<Throwable> errors) {
		validatePublicVoidNoArgMethods(After.class, false, errors);
		validatePublicVoidNoArgMethods(Before.class, false, errors);
		validateTestMethods(errors);

		if (computeTestMethods().size() == 0)
			errors.add(new Exception("No runnable methods"));
	}
  ```
  
  - getTimeout: falls es keine Annotation gibt, könnte man 0L zurückgeben für bessere Lesbarkeit oder gar nicht überprüfen, da 0L schon das default ist. So definiert man auf 2 Orte timeout 0 bedeutet kein timeout
  
  ```Java
    // in BlockJUnit4ClassRunner.java
    private long getTimeout(Test annotation) {
		if (annotation == null)
			return 0;
		return annotation.timeout();
	}
	
	@Deprecated
	protected Statement withPotentialTimeout(FrameworkMethod method,
			Object test, Statement next) {
		long timeout= getTimeout(method.getAnnotation(Test.class));
		return timeout > 0 ? new FailOnTimeout(next, timeout) : next;
	}
	
	// in Test.java
	long timeout() default 0L; 
  ```
  
  - possiblyExpectingExceptions: exceptsException ruft sowieso getExpectedException, Code könnte in eine Methode vereinigt werden für bessere Lesbarkeit. Man könnte dann nach Class.None prüfen, da dass sowieso das default Value ist für den Annotation
  
  ```Java
    @Deprecated
	protected Statement possiblyExpectingExceptions(FrameworkMethod method,
			Object test, Statement next) {
		Test annotation= method.getAnnotation(Test.class);
		return expectsException(annotation) ? new ExpectException(next,
				getExpectedException(annotation)) : next;
	}
  ```
  
  - Metrics Boyan
  
    - methodBlock: 18 Zeilen, 23 Minuten (+ Verständniss über aufgerufene Methoden)
    - runChild: 6 Zeilen, 3 Minuten
    - runNotIgnored: 10 Zeilen, 4 Minuten
    - runIgnored: 1 Zeile, weniger als Minute
    - describeChild: 2 Zeilen, 2 Minuten
    - getChildren, computeTestMethods: 2 Zeilen, 3 Minuten
    - collectInitializationErrors: 4 Zeilen, 1 Minute
    - validateConstructor: 2 Zeilen, weniger als Minute
    - validateOnlyOneConstructor: 4 Zeilen, weniger als Minute
    - validateZeroArgConstructor: 5 Zeilen, 3 Minuten
    - hasOneConstructor: 1 Zeile, 2 Minuten (nicht sicher ob Java Schnittstellen richtig benutzt)
    - validateInstanceMethods: 5 Zeilen, 6 Minuten
    - validateFields: 3 Zeilen, 5 Minuten (habe mich kurz in JUnit @Rule eingearbeitet)
    - validateRuleField: 6 Zeilen, 2 Minuten
    - validateTestMethods: 1 Zeile, 1 Minute
    - createTest, testName: 2 Zeilen, 1 Minute
    - methodInvoker: 1 Zeile, weniger als Minute
    - possiblyExpectingExceptions: 3 Zeilen, 2 Minuten
    - withPotentialTimeout: 2 Zeilen, 1 Minute
    - withBefores, withAfters: 4 Zeilen, 2 Minuten
    - withRules: 5 Zeilen, weniger als Minute
    - makeNotifier: 2 Zeilen, 8 Minuten (sollte sicherstellen, was die Methode machen soll und ob alles richtig weitergegeben wird)
    - getExpectedException: 4 Zeilen, 2 Minuten
    - expectesException: 1 Zeilen, weniger als 1 Minute
    - getTimeout: 3 Zeilen, ~8 Minuten
    
    
    - Insgesammt, mit generelles Verständniss und nicht spezifisch für irgenwelche Methode: ~2h 20m
    - ~1 Defekt pro Stunde. Wurde aber deutlich länger dauern automatisierte Tests zu bauen, wurden auch weitere Verbesserungsmöglichkeiten gefunden, für also insgesammt 3 Defekte pro Stunde
