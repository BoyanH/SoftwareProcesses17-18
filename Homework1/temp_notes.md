# Notes

## Cool stuff about JUnit

No need to list them all here, they are actually the stuff from the *Usage and Idioms* section on
the JUnit website.

#### Running Multiple Tests
- a test Suite can include multiple test classes
- *Right Click* -> `Run As` -> `JUnit Test`

#### Expecting Exceptions
- try/catch idiom to evaluate Exception message
- need to define a Rule for expected exception

#### Fixtures
- a fixed state of a set of object to ensure that there is a well known and fixed
environment for running test, so that the test results are repeatable.
- Examples:
  - prepare input data, create fake objects
  - load a database with specific data
  - copy a specific set of files
- @BeforeClass, @Before, @After, @AfterClass

#### Theory
- a theory captures some aspect of the inteded behaviour in possibly infinite numbers of
potential scenarios
- what to do in case a username has a '/' in it

#### Assumptions
- tests with failed assumptions are ignored

#### Rules
- addition or redefinition of the behaviour of each test method
- TemporaryFolder, ExternalResource, ErrorCollector, Verifier

## Writing good tests

*TODO: Actually have examples and counter-examples written with the JUnit notation*

Unit test should test only a specific component, so that when other parts of the system change, the
tests are still working. On the other end of the scale, integration tests make assumptions how the 
whole system behaves. Anything in between is bad, because refractoring might break the tests.

- **keep testing code compact and readable** - this makes it easier to maintain the testing code
- **don't mock third party objects** - after the library has been updated, the object logic might 
chagne, but because the object was mocked, the test will still pass. It can also be a sign 
that your project and the third party library are not decoupled enough.
- **test names** - good test names can help the tester understand their purpose

#### Useful Links
- https://github.com/mockito/mockito/wiki/How-to-write-good-tests
- http://blog.stevensanderson.com/2009/08/24/writing-great-unit-tests-best-and-worst-practises/
- https://www.javaworld.com/article/2076265/testing-debugging/junit-best-practices.html

#### Bonus
- mock = vortäuschen
