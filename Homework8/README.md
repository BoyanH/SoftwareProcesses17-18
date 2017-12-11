## Aufgabe 1

### Why is it reasonable to proceed top-down and not bottom-up when using goal question metric approach?

* top-down = data analysis before having any data. Thinks of data usage before actually having any
* when gathering data without knowing why you gather it for, often wrong data is extracted
* when taken out of the context (after a long time) data can easily be misunderstood
* missing data can never be added, as the context is already lost; programmers don't remember all the details anymore
* defining schema at the beginning leads to more accurate data and better statistics

### Why is measuring important in the software engineering process?

* error detection and error correction are considered the major cost factors in SE
* measuring reason for (type of) error can provide good statistics
* good statistics can help design a better process, which leads to less errors or easier changes
* less errors and easier changes lead to lower costs

### Which information sources may help to develop the goals element?

* goals are defined in order to achieve something (greater goals)
* people, who have knowledge in the area of the greater goal must be asked, they can define the goals for GQM better
* one must also consider what data can be gathered succesffuly and define goals which can be satisfied

### Which pitfalls remain for the data analysis despite the goal question metric approach?

* misunderstading by those filling out the forms
* misunderstanding by analyst
* too much effort to fill out forms
* no feedback to those filling out the forms (they cannot improve their data gathering)
* interpreting results without understanding the factors which lead to them
* sensitivity of data
  * people, who fill out the forms, must be assured that the data won't be used against them
* monitoring one's behavior often lead to this person changing his/hers behavior
* isolating single factors that lead to a certain case (behavior / situation) is hard in complex systems
* lost data (something that should have been gathered, but wasn't) is impossible to acquire afterwards. context is lost

### Notes on GQM paper

#### Untitled / General

* data usually wrongly classified into an incorrect scheme, analysed from 3. party or misunderstood
* when using goals one can gather relevant and precise data
  * otherwise too much, hardly interpretable and incorrect data is gathered
* define schema with the help of people who will find the data useful
  * e.g. software engineers when gathering methodology data (information hiding)
* Have goals
  * generate metrics
  * e.g. Goal -> Characterize changes in SW
  * Question -> Distribution of changes relevant to reason for change
* Have questions -> define schema
* consider how data analysis must be done before you have any data
* schema must be complete and consistent
  * each case fits in only one categorization in the schema
* often "Other", "Not Applicable" etc. used to ensure schema completeness
* Data validation is a must
  * e.g. two different reasons lead to change in one routine
  * must be entered in 2 separate forms
  * auto-generation of forms
* Data analysis while gathering data
* For data validation
  * data analyst reviews data
  * interviews with the ones filling out the forms
* Problem -> Data analyst can not know which changes were not submitted or wrongly classified
  * add validation by the team leader
* classify data according to probability for accuracy
* inaccuracy of 50% can be introduced when skipping the validation process
* data analysis shows which data can be reliably collected
  * goals and questions may need to be revised

#### Pitfalls for GQM

* misunderstanding by those filling out the forms -> training might help
* misunderstanding by analyst -> pick analyst who is already familiar with the environment
* no feedback to those filling out the forms (timely)
* too much effort to fill out forms
* no consistency / accuracy checks in DB prior to analysis
* interpreting results without understainding the factors which lead to them
* not understanding reports while doing interviews
* sensitivity of data -> convice people who fill out the forms that the data won't be used against them
* changing behavior when knowing it is being monitored

#### Avoiding data collection pitfalls

* analysts who are familiar with the environment
* GQM before data collection
* small goals, effort grows exponentially
* project specific data collection forms
* integrate data collection and validation process into the configuration process

#### Limitations

* isolating single factors
* lost data connot be accurately recaptured
  * if data is missing in schema and is useful, it cannot be added later

## Aufgabe 2

**Assessing the Process of an Eastern European Software SME using Systemic Analysis, GQM, and Reliability Growth Models** - 2016 - Vladimir Ivanov, Manuel Mazzara, Witold Pedrycz, Alberto Sillitti, Giancarlo Succi

[https://csdl.computer.org/csdl/proceedings/icse-c/2016/4205/00/4205a251.pdf](https://csdl.computer.org/csdl/proceedings/icse-c/2016/4205/00/4205a251.pdf)

- **Core Issue and Objective** - 
  - To see if GQM and Systemic Analysis gute Methoden für Analyse und Prozessverbesserung sind.
  - To be applicable also in small contexts, not requiring a
major investment;
  - to go to the root causes of the problems,  and rather
than prescribing practices and disciplines that would
be  hard,  if  not  impossible,  to  follow,  to  present  how
changing some of the dynamics inside the existing pro-
cess of a company, such problems would almost auto-
matically dissolve.

- **Motivation** - Es geht um eine mittelgroße osteuropäische Softwarefirma, die keinen festen Softwareprozess hat. Das Team wurde angeheuert, um Einsichten und "Silber Kugeln" zu liefert.

- **Research Strategy** -
  1. Ausführliche GQM Session mit höherem Management um technischen und Geschäftsziele zu definieren, und Fragen und Metriken festzulegen
  2. Persönliche Gespräche mit Mitarbeiter, wobeei sie über die Firma, ihre Prozesse, Ziele und persönliche Aspekte und Herausforderungen reden.
  3. Beziehungen, Metapher, Ambitionen und Probleme aus den Interviews extrahieren
  4. Aktuelle Dokumentation über die Softwareprozesse lesen (die entspricht die Realität nicht)
  5. Analyse über Öffnen- und Schließzeiten von Bugs um Muster in der tatsächliche Organisation der Entwicklung zu finden.
  6. Prozess so rekonstruiren, damit auch nicht-Techies es verstehen können, und Unterschiede mit Realität deutlich markieren.

- **Results and conclusions** -
Diese Unternehmung war laut der Forscher erfolgreich. GQM war entscheidend bei Zieldefinition und Datenanalyse. Am ende gab es leichte Verbesserung des Prozesses der Firma, das war aber keine Langfirstige Studie. Außerdem wenn man Schismogenesis behebt, verbessert sich das Prozess auch von sich selbst.

- **Who benefits** - Management von kleinen und mittelgroßen Firmas, die Interesse daran haben, ihre Prozess quantitativ zu verbessern.

- **Interesting and/or surprising** 
  - *It  is  ironical  to  notice  that  just  convincing
him  of  the  infeasibility  of  his  request  required  more  effort
than  what  he  originally  foresaw  for  the  entire  assessment.*
  - *these approaches are still perceived
by SMEs as complicated approaches intended for large com-
panies and may scare the management away due to uncer-
tainty during the implementation of changes*
  - *Testing was not liked among the Developers, so a specific Testing group was created with lower salaries and not particularry appreciated people*

- **Formulated goall** - A single product line with merged codebases, and establish sounder testing practices.
  - **Object of measurement** - 
  - **goal** - 
  - **quality focus** - 
  - **perspective** - 
  - **context** - 

- **Concerning the activities during the six GQM steps** - nicht viele Infos. Das GQM Vorgehen hat dabei geholfen, messbare techische und Geschäftsziele zu definieren und Vertrauen mit hohem Management zu bauen.

- **Unsolved questions to be answered through data analysis** - Keine explizite Infos. Wann tauchen Bugs auf, wie schnell und unter welchen Umständen werden die behebt? Welche Variablen (wie Priorität und Schwere) sind entscheidend für die Beschreibung des Entwichlungprozesses.

- **What kind of data was collected and how?** - 
  - arriving and closing time of Issues, auch mit Daten wie Schwere und Priorität
