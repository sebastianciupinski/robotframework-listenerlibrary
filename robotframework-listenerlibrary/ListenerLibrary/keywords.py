from robot.libraries.BuiltIn import BuiltIn

def _end_keyword_implementation():
    pass

def _start_keyword_implementation():
    pass

def _start_test_implementation():
    pass

def _end_test_implementation():
    pass

def _start_suite_implementation():
    pass

def _end_suite_implementation():
    pass

class ListenerLibraryKeywords(object):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LISTENER_API_VERSION = 2



    def __init__(self):

        self.ROBOT_LIBRARY_LISTENER = self

    def _start_keyword(self, name, attrs):
        _start_keyword_implementation()


    def _end_keyword(self, name, attrs):
        _end_keyword_implementation()

    def _start_test(self, name, attrs):
        _start_test_implementation()


    def _end_test(self, name, attrs):
        _end_test_implementation()

    def _start_suite(self, name, attrs):
        _start_suite_implementation()

    def _end_suite(self, name, attrs):
        _end_suite_implementation()

    def _log_message(self, message):
        pass

    def _library_import(self, name, attrs):
        pass

    def _resource_import(self, name, attrs):
        pass

    def _output_file(self, path):
        pass

    def _report_file(self, path):
        pass

    def _xunit_file(self, path):
        pass

    def _debug_file(self, path):
        pass

    def _close(self):
        pass

    #keywords below


    def register_start_keyword_listener(self, kwname, *args):
        """Allows to register keyword as start keyword listener. After this keyword, keyword defined as _kwname_ will be executed before each keyword during test execution.
        Executing this keyword once again *does not* register new listener, but redefines existing one.

        Example:
        | Register Start Keyword Listener | Element Should Be Not Visible | id="error-message"
        """
        global _start_keyword_implementation
        def _start_keyword_implementation():
            BuiltIn().run_keyword(kwname, *args)

    def unregister_start_keyword_listener(self):
        """Allows to unregister keyword acting as start keyword listener. After this keyword, listener defined by `Register Start Keyword Listener` will not be executed anymore.
        """
        global _start_keyword_implementation
        def _start_keyword_implementation():
            pass

    def register_end_keyword_listener(self, kwname, *args):
        """Allows to register keyword as end keyword listener. After this keyword, keyword defined as _kwname_ will be executed after each keyword during test execution.
        Executing this keyword once again *does not* register new listener, but redefines existing one.

        Example:
        | Register End Keyword Listener | Element Should Be Not Visible | id="error-message"
        """
        global _end_keyword_implementation
        def _end_keyword_implementation():
            BuiltIn().run_keyword(kwname, *args)

    def unregister_end_keyword_listener(self):
        """Allows to unregister keyword acting as start keyword listener. After this keyword, listener defined by `Register End Keyword Listener` will not be executed anymore.
        """
        global _end_keyword_implementation
        def _end_keyword_implementation():
            pass







    def register_start_test_listener(self, kwname, *args):
        """Allows to register keyword as start test listener. After this keyword, keyword defined as _kwname_ will be executed before each test during test execution.
        Executing this keyword once again *does not* register new listener, but redefines existing one. *Note* - this does not override Test Setup setting.

        Example:
        | Register Start Test Listener | Element Should Be Not Visible | id="error-message"
        """
        global _start_test_implementation
        def _start_test_implementation():
            BuiltIn().run_keyword(kwname, *args)

    def unregister_start_test_listener(self):
        """Allows to unregister keyword acting as start test listener. After this keyword, listener defined by `Register Start Test Listener` will not be executed anymore.
        """
        global _start_test_implementation
        def _start_test_implementation():
            pass

    def register_end_test_listener(self, kwname, *args):
        """Allows to register keyword as end test listener. After this keyword, keyword defined as _kwname_ will be executed after each test during test execution.
        Executing this keyword once again *does not* register new listener, but redefines existing one. *Note* - this does not override Test Teardown setting.

        Example:
        | Register End Test Listener | Element Should Be Not Visible | id="error-message"
        """
        global _end_test_implementation
        def _end_test_implementation():
            BuiltIn().run_keyword(kwname, *args)

    def unregister_end_test_listener(self):
        """Allows to unregister keyword acting as end test listener. After this keyword, listener defined by `Register End Test Listener` will not be executed anymore.
        """
        global _end_test_implementation
        def _end_test_implementation():
            pass





    def register_start_suite_listener(self, kwname, *args):
        """Allows to register keyword as start suite listener. After this keyword, keyword defined as _kwname_ will be executed before each suite during test execution.
        Executing this keyword once again *does not* register new listener, but redefines existing one. *Note* - this does not override Suite Setup setting.

        Example:
        | Register Start Suite Listener | Element Should Be Not Visible | id="error-message"
        """
        global _start_suite_implementation
        def _start_suite_implementation():
            BuiltIn().run_keyword(kwname, *args)

    def unregister_start_suite_listener(self):
        """Allows to unregister keyword acting as start suite listener. After this keyword, listener defined by `Register Start Suite Listener` will not be executed anymore.
        """
        global _start_suite_implementation
        def _start_suite_implementation():
            pass

    def register_end_suite_listener(self, kwname, *args):
        """Allows to register keyword as end suite listener. After this keyword, keyword defined as _kwname_ will be executed after each suite during test execution.
        Executing this keyword once again *does not* register new listener, but redefines existing one. *Note* - this does not override Suite Teardown setting.

        Example:
        | Register End Suite Listener | Element Should Be Not Visible | id="error-message"
        """
        global _end_suite_implementation
        def _end_suite_implementation():
            BuiltIn().run_keyword(kwname, *args)

    def unregister_end_suite_listener(self):
        """Allows to unregister keyword acting as end suite listener. After this keyword, listener defined by `Register End Suite Listener` will not be executed anymore.
        """
        global _end_suite_implementation
        def _end_suite_implementation():
            pass