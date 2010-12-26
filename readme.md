# Test lab #

## Lecture ##


### Introduce concept unit test ###


A unit test is a piece of a code (usually a method) that invokes another piece of code and checks the correctness of some assumptions after- ward. If the assumptions turn out to be wrong, the unit test has failed. A “unit” is a method or function.

Properties of a good unit test

* It should be automated and repeatable. 
* It should be easy to implement. 
* Once it’s written, it should remain for future use. 
* Anyone should be able to run it. 
* It should run at the push of a button. 
* It should run quickly.

A unit test is an automated piece of code that invokes the method or class being tested and then checks some assumptions about the logical behavior of that method or class. A unit test is almost always written using a unit-testing framework. It can be written easily and runs quickly. It’s fully automated, trustworthy, readable, and maintainable.

### Simple example using Python (or the language of choice for the lab) ###


### History of unit testing?? ###


### Talk about TDD. ###

Writing tests first. 
Red Green Refactor. 
Design for testability. 
More about TDD.

### More about unit tests ###

coverage?
independent and repeatable
Keep the tests simple. You don’t want bugs in your test code. 
Naming!!
Test one thing per test method, ideally one assert per test method.

### Fakes ###

Explain the difference between stubs and mocks.
A stub makes the SUT happy and also provides controlled feed back from dependencies.
A mock is used for verification.

Some simple examples.

### State testing vs behaviour testing ###

State testing is testing that the SUT has the expected state after the test.
Behaviour testing is testing that the SUT makes the correct calls to dependencies.

### What to test and what not to test ###

Test logic, conditionals, loops, operations, polymorphism.
Boundary conditions. "There are only two hard problems in Computer Science: cache invalidation, naming things, and off-by-one errors."

Don’t test getters/setters.

Don’t test private methods/internal state.

Don’t unit test UI.

Right: Are the results right? 
* B: Are all the boundary conditions correct? 
* I: Can we check inverse relationships? 
* C: Can we cross-check results using other means? 
* E: Can we force error conditions to happen? 
* P: Are performance characteristics within bounds?

### How does other types of testing, (functional, integration, etc) relate to unit testing? ###

These tests can still be run with the unit test framework. They are harder to write. Requires much more set up code. More likely to change.

### Unit tests as a learning tool ###

A way to learn a new API or framework. Write small tests to check your assumptions.

### How to test ###

AAA, Arrange-Act-Assert
Prove that the tests work by introducing bugs in SUT

### Dependency injection ###

### Real world example ###

Unit testing a program that talks to a REST based API. 
Test URL generation
Test parsing of correct data
Test parsing of error data
Test communication by using mocks. Simulate errors.

 
### How to: Other common scenarios ###

Using date and time, now

## Lab ##


### TDD introduction ###

A walk through of creating a simple class using TDD. All tests are written as failing tests. Implement only what is needed to make the test pass. When understanding the basics you often implement the obvious implementation. Must be prepared to go smaller steps if tests start to fail.

### TDD Assignment

Students implement another simple class using TDD. Perhaps a few assignments to choose from.

- Fakes

Have an example where fakes should be used. Assignment is to change the code to use fakes instead of the real classes. 

- Protocol

Subset of XMPP

Chat client

The protocol needs to be very simple.

There is a helper class available that can:
- send messages to the server
- receive messages from the server and pass them on to the client
- messages are sent and received asynchronously
- to the assignment is to build and test a state machine
- test that the client works as expected when receiving messages
- test that the client properly encodes the message before passing them on to the helper
- the helper will just pass happily along any message
- the helper will also pass along any message from the server to the client
