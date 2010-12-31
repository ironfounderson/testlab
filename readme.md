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

* send messages to the server
* receive messages from the server and pass them on to the client
* messages are sent and received asynchronously
* the assignment is to build and test a state machine
* test that the client works as expected when receiving messages
* test that the client properly encodes the message before passing them on to the helper
* the helper will just pass happily along any message
* the helper will also pass along any message from the server to the client


`def test_login_helper_gets_correct_command(self):`

### Chat use cases

Log on to server

Log off from server

Send message to existing user

Send message to non existing user

Receive message from user in friend list

Receive message from user not in friend list

Request friend list from server

Get rejected from server when logging on

Get disconnected from server

Receive notification that a user in friend list has changed status

Friend status = online, offline, (away)

Send friend request

Receive friend request

Sent friend request gets rejected

Sent friend request gets accepted

Accept incoming friend request

Reject incoming friend request

Send message to user of different status

Change your own status

Receive message when you are away

Messages received when away should be queued and displayed when becoming online? You have X messages.



The assignment is to write a `TalkClient` class using TDD. There are some helper classes available. All communication to and from the server is done via a `ClientService` class. The `ClientService` class has a `send` method and invokes a `receive` method on the `TalkClient` for all communication.

The assignment is to create a new class to facilitate the interaction with the chat service. Today the API is very sparse. It's one class that has one method `send` and uses a callback to report responses and incoming messages and requests. Actually, it is a bit more complex but for the purpose of this assignment that is what is important.

    class ChatService(object):
      def __init__(self, callback):
        super(ChatService, self).__init__()
        self.callback = callback
        
      def send(self, message):
        """sends a message to the server"""
        pass

    class SimplifiedChatClient(object):
      def __init__(self):
          super(SimplifiedChatClient, self).__init__()
          self.chat_service = ChatService(self)

      def response(self, message):
          """invoked from chat_service when there is a response or message 
              from the server"""
          print message

      def send(self, message):
          """passes on the message to the chat_service"""
          self.chat_service(message)

What is needed is a new `ChatClient` which has a better API and meets the following requirements:

...list of requirements...




# Tests

The first categories of tests that one can write is to make sure that the messages that will be sent to the server are encoded properly. This can be done in at least two ways. The `ChatClient` uses a `ChatService` that can be mocked and we can test against our mock to make sure that we get the correct message. See `test_login_using_mock`. Another way would be to have a helper method encode the command and have the test make sure that the helper method works as expected. That was an easy test to write since we are not doing very much. Depending on if we want to test that the user and password supplied to the method are valid, non-empty string, we can write more tests. The `ChatService` will return an error message if the supplied credentials are wrong so we will leave out further tests for now.

We need tests for the rest of our send commands so let's move on. `logout` is an easy test to write as well. And the implementation for the failing test is also easy to implement. Since I did basically copy-pasted my first test case to create the second I have a feeling that we can refactor the test case some. But I'm going to postpone that refactoring until we have written our next test, `send_message`. Again I did a copy-paste so let's refactor the test case a bit. I'm going to introduce two test classes, one for testing sending of messages using the mock and one for making sure `ChatClient` works as expected when receiving messages. Now the tests have been refactored to use `setUp` we can continue to `send_friend_request`. Another straight forward test. The last of these simple test is for `set_status` 

After these tests we can continue to handle responses according to the specification. Let's start by tackling an easy problem, the response to the login command. What we want to test is that the status is updated accordingly after receiving a response to login.

This is going to get messy but that is a good thing since with the tests you can actually refactor the code and make sure it still works. We are building a state machine and I'm not sure where we will end up.

Login

What do we need to do to be able to login? 

- login command, user, password
- we need to make sure that with send the correct command
to make is easy the commands are encoded as Python dictionaries
{'command':'login', 'args':['username','password']}

The responses we get from `ClientService` are also delivered as Python dictionaries. If a response contains a key exception with a non-nil value then there was a "serious" error trying to deliver the command. Serious as the server can't be reached. All commands are listed together with the possible responses. The `ClientService` handles the underlying stuff of appending the token/cookie for the session.

The communication is done asynchronously which means that responses can come at "unexpected times". This means that the first response that comes from a 'send-message' command could very well be a message from another user.

The responsibilities of the `TalkClient` class are:

    login(user, password)
    logout()
    send_message(user_id, message)
    send_friend_request(user_id)
    get_friend_list()
    get_messages()
    get_current_status()

The talk client does not need to update any "user" of status changes etc. The "user" will query `TalkClient` using the above API

# Commands

## Possible responses to all commands

connection error:
{'response-to-command':'command-name','exception':'connection error'}

client not logged on:
{'response-to-command':'command-name','exception':'unknown client'}

## Login
Sent when the client want to login to the chat server.

{'command':'login',...}

### Possible responses
login ok:
{'response-to-command':'login','value':'ok'}

login failed:
{'response-to-command':'login','value':'failed'}

## Logoff
{'command':'logoff'}

### Possible responses
logoff ok:
{'response-to-command':'logoff','value':'ok'}

logoff failed: (user has not previously logged in)
{'response-to-command':'logoff','value':'failed'}

## Request friend list

{'command':'friend-list'}

### Possible responses
{'response-to-command':'friend-list','response-code':'ok', 'value':[{'name':'','id':'','status':''},...]}

## Send message

{'command':'send-message','to':'user-id','message':'message-text'}

### Possible responses
Message sent successfully:
{'response-to-command':'send-message','response-code':'ok'}

Message failed to be delivered:
{'response-to-command':'send-message','response-code':'failed'}

## Set status
Sent when the user want's to change her status

{'command':'set-status', 'value':'new-status'}

value: 'online', 'away'

Other values return a response unknown value
{'response-to-command':'set-status', 'response-code':'unknown-value'}

# Responses that can come at any time

## Friend status change
A status change message is sent when a user has changed their status as well as their name
{'response':'friend-status-change','value':{'name':'current-name','id':'id','status':'new-status'}}

## Message from user
{'response':'message','from':{'name':'user-name','id':'user-id'},'message':'message-text'}

## Friend request from user
{'response':'friend-request','from':{'name':'user-name','id':'user-id'},'message':'message-text'}



