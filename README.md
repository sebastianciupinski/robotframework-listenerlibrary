ListenerLibrary for Robot Framework
==================================================


Introduction
------------

RobotFramework library relaying on [listener interface](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#listener-interface).
Allows to run defined RF keyword before other keywords are executed, after keywords are executet, before test, after test, etc.

- Information about keywords can be found on the [Keyword Documentation](https://raw.githack.com/sebastianciupinski/robotframework-listenerlibrary/master/docs/ListenerLibrary.html) page.


Requirements
------------
* Robot Framework


Installation
------------
#### Using pip ####

The recommended installation tool is [pip](http://pip-installer.org).

Install pip.
Enter the following:

    pip install robotframework-listenerlibrary

Usage
------------
BasicListener.robot

    *** Settings ***
    Documentation     This example demonstrates how to use current library
    Library      ListenerLibrary

    *** Test Cases ***
    Example Test
        Should Be Equal As Numbers    2    2
        Register Start Keyword Listener    Log   message from start keyword listener
        Should Be Equal As Numbers    2    2
        Register End Keyword listener      Log   message form end keyword listener    level=WARN
        Should Be Equal As Numbers    2    2
        Custom Keyword    You will see keyword above this and bellow this
        Unregister End Keyword Listener
        Should Be Equal As Numbers    2    2
        Unregister Start Keyword Listener
        Should Be Equal As Numbers    2    2

    *** Keywords ***
    Custom Keyword
        [Arguments]     ${argument}
        Log       ${argument}


MultipleListeners.robot

    *** Settings ***
    Documentation     This example demonstrates how to use current library
    Library      ListenerLibrary    WITH NAMR   FirstListener
    Library      ListenerLibrary    WITH NAME    AnotherListener

    *** Test Cases ***
    Example Test
        Should Be Equal As Numbers    2    2
        FirstListener.Register Start Keyword Listener    Log   message from start keyword listener
        Should Be Equal As Numbers    2    2
        FirstListener.Register End Keyword listener      Log   message form end keyword listener    level=WARN
        Should Be Equal As Numbers    2    2
        Should Be Equal As Numbers    2    2
        AnotherListener.Register Start Keyword Listener    Log   start kw message from AnotherListener
        FirstListener.Unregister End Keyword Listener
        Should Be Equal As Numbers    2    2
        FirstListener.Unregister Start Keyword Listener
        AnotherListener.Unregister Start Keyword Listener
        Should Be Equal As Numbers    2    2



