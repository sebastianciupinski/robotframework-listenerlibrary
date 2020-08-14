import pkg_resources
from .keywords import ListenerLibraryKeywords


#__version__ = pkg_resources.get_distribution("robotframework-listenerlibrary").version


class ListenerLibrary(ListenerLibraryKeywords):
    """ListenerLibrary allows to register and unregister RobotFramework [http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#listener-interface|listeners].

    Listeners may be used for example to performing certain action after/before keywords
    Keywords executed by listeners are unable to FAIL tests - they are raising ERROR,
    so to fail TestCase when listener keywords fails, use --exitonerror command-line switch.

    To register more than one listener, import library many times with WITHNAME option
    
    Examples:    
    
    *SingleListener.robot*
    
    | ***** Settings ***** 
    | Documentation   This example demonstrates how to use current library 
    | Library      ListenerLibrary 
    |
    | ***** Test Cases ***** 
    | Example Test
    |    Should Be Equal As Numbers     2     2
    |    Register Start Keyword Listener    Log   message from start keyword listener
    |    Should Be Equal As Numbers    2    2
    |    Register End Keyword listener      Log   message form end keyword listener    level=WARN
    |    Should Be Equal As Numbers    2    2
    |    Custom Keyword    You will see keyword above this and bellow this
    |    Unregister End Keyword Listener
    |    Should Be Equal As Numbers    2    2
    |    Unregister Start Keyword Listener
    |    Should Be Equal As Numbers    2    2
    |
    | ***** Keywords *****
    | Custom Keyword
    |    [Arguments]     ${argument}
    |    Log       ${argument}
    
    *MultipleListeners.robot*
    
    | ***** Settings *****
    | Documentation     This example demonstrates how to use current library
    | Library      ListenerLibrary    WITH NAME   FirstListener
    | Library      ListenerLibrary    WITH NAME   AnotherListener
    |
    | ***** Test Cases *****
    | Example Test
    |     Should Be Equal As Numbers    2    2
    |     FirstListener.Register Start Keyword Listener    Log   message from start keyword listener
    |     Should Be Equal As Numbers    2    2
    |     FirstListener.Register End Keyword listener      Log   message form end keyword listener    level=WARN
    |     Should Be Equal As Numbers    2    2
    |     Should Be Equal As Numbers    2    2
    |     AnotherListener.Register Start Keyword Listener    Log   start kw message from AnotherListener
    |     FirstListener.Unregister End Keyword Listener
    |     Should Be Equal As Numbers    2    2
    |     FirstListener.Unregister Start Keyword Listener
    |     AnotherListener.Unregister Start Keyword Listener
    |     Should Be Equal As Numbers    2    2
    """ 

    ROBOT_LIBRARY_SCOPE = "GLOBAL"