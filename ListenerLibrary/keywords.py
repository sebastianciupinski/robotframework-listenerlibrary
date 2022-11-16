from robot.libraries.BuiltIn import BuiltIn

def _end_keyword_registered_implementation():
    pass

def _end_keyword_import_implementation():
    pass

def _start_keyword_registered_implementation():
    pass

def _start_keyword_import_implementation():
    pass

def _start_test_registered_implementation():
    pass

def _start_test_import_implementation():
    pass

def _end_test_registered_implementation():
    pass

def _end_test_import_implementation():
    pass

def _start_suite_registered_implementation():
    pass

def _start_suite_import_implementation():
    pass

def _end_suite_registered_implementation():
    pass

def _end_suite_import_implementation():
    pass

def _passed_keyword_import_implementation():
    pass

def _passed_keyword_registered_implementatnion():
    pass

def _skipped_keyword_import_implementation():
    pass

def _failed_keyword_import_implementation():
    pass

def _passed_keyword_registered_implementation():
    pass

def _skipped_keyword_registered_implementatnion():
    pass

def _failed_keyword_registered_implementatnion():
    pass



class ListenerLibraryKeywords(object):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LISTENER_API_VERSION = 2



    def __init__(self,
        start_keyword_listener = None, end_keyword_listener = None,
        start_test_listener = None, end_test_listener = None,
        start_suite_listener = None, end_suite_listener = None,
        passed_end_keyword_listener = None, failed_end_keyword_listener = None, skipped_end_keyword_listener = None,
        passed_end_test_listener = None, failed_end_test_listener = None, skipped_end_test_listener = None,
        passed_end_suite_listener = None, failed_end_suite_listener = None, skipped_end_suite_listener = None,

        included_keyword_tags = None, excluded_keyword_tags = None,
        included_test_tags = None, excluded_test_tags = None,

        token_separator="|"):

        self.start_keyword_listener = start_keyword_listener
        self.end_keyword_listener = end_keyword_listener
        self.start_test_listener = start_test_listener
        self.end_test_listener = end_test_listener
        self.start_suite_listener = start_suite_listener
        self.end_suite_listener = end_suite_listener
        self.passed_end_keyword_listener = passed_end_keyword_listener
        self.failed_end_keyword_listener = failed_end_keyword_listener
        self.skipped_end_keyword_listener = skipped_end_keyword_listener
        self.passed_end_test_listener = passed_end_test_listener
        self.failed_end_test_listener = failed_end_test_listener
        self.skipped_end_test_listener = skipped_end_test_listener
        self.passed_end_suite_listener = passed_end_suite_listener
        self.failed_end_suite_listener = failed_end_suite_listener
        self.skipped_end_suite_listener = skipped_end_suite_listener


        self.token_separator = token_separator

        self.ROBOT_LIBRARY_LISTENER = self

        if self.start_keyword_listener is not None:
            self._start_keyword_import_implementation = lambda: BuiltIn().run_keyword(*self._tokenize_listener(self.start_keyword_listener))

        if end_keyword_listener is not None:
            self._end_keyword_import_implementation = lambda: BuiltIn().run_keyword(*self._tokenize_listener(self.end_keyword_listener))
            

        if self.start_test_listener is not None:
            self._start_test_import_implementation = lambda: BuiltIn().run_test(*self._tokenize_listener(self.start_test_listener))


        if self.end_test_listener is not None:
            self._end_test_import_implementation = lambda :BuiltIn().run_test(*self._tokenize_listener(self.end_test_listener))


        if self.start_suite_listener is not None:
            self._start_suite_import_implementation = lambda: BuiltIn().run_suite(*self._tokenize_listener(self.start_suite_listener))                

        if self.end_suite_listener is not None:
            self._end_suite_import_implementation = lambda: BuiltIn().run_suite(*self._tokenize_listener(self.end_suite_listener))

        if self.passed_end_keyword_listener is not None:
            self._passed_end_keyword_import_implementation = lambda: BuiltIn().run_keyword(*self._tokenize_listener(self.passed_end_keyword_listener))

        if self.failed_end_keyword_listener is not None:
            self._failed_end_keyword_import_implementation = lambda: BuiltIn().run_keyword(*self._tokenize_listener(self.failed_end_keyword_listener))

        if self.skipped_end_keyword_listener is not None:
            self._skipped_end_keyword_import_implementation = lambda: BuiltIn().run_keyword(*self._tokenize_listener(self.skipped_end_keyword_listener))

        if self.passed_end_test_listener is not None:
            self._passed_end_test_import_implementation = lambda: BuiltIn().run_test(*self._tokenize_listener(self.passed_end_test_listener))

        if self.failed_end_test_listener is not None:
            self._failed_end_test_import_implementation = lambda: BuiltIn().run_test(*self._tokenize_listener(self.failed_end_test_listener))

        if self.skipped_end_test_listener is not None:
            self._skipped_end_test_import_implementation = lambda: BuiltIn().run_test(*self.__tokenize_listener(self.skipped_end_test_listener))

        if self.passed_end_suite_listener is not None:
            self._passed_end_suite_import_implementation = lambda: BuiltIn().run_suite(*self.__tokenize_listener(self.passed_end_suite_listener))

        if self.failed_end_suite_listener is not None:
            self._failed_end_suite_import_implementation = lambda: BuiltIn().run_suite(*self._tokenize_listener(self.failed_end_suite_listener))

        if self.skipped_end_suite_listener is not None:
            self._skipped_end_suite_import_implementation = lambda: BuiltIn().run_suite(*self._tokenize_listener(self.skipped_end_suite_listener))

    def _start_keyword_import_implementation(self):
        pass

    def _end_keyword_import_implementation(self):
        pass
        
    def _passed_end_keyword_import_implementation(self):
        pass    

    def _failed_end_keyword_import_implementation(self):
        pass  
        
    def _skipped_end_keyword_import_implementation(self):
        pass 
        
    def _start_keyword_registered_implementation(self):
        pass

    def _end_keyword_registered_implementation(self):
        pass

    def _passed_end_keyword_registered_implementation(self):
        pass    

    def _failed_end_keyword_registered_implementation(self):
        pass  
        
    def _skipped_end_keyword_registered_implementation(self):
        pass    

    ### test listeners definitions

    def _start_test_import_implementation(self):
        pass

    def _end_test_import_implementation(self):
        pass
        
    def _passed_end_test_import_implementation(self):
        pass    

    def _failed_end_test_import_implementation(self):
        pass  
        
    def _skipped_end_test_import_implementation(self):
        pass 
        
    def _start_test_registered_implementation(self):
        pass

    def _end_test_registered_implementation(self):
        pass

    def _passed_end_test_registered_implementation(self):
        pass    

    def _failed_end_test_registered_implementation(self):
        pass  
        
    def _skipped_end_test_registered_implementation(self):
        pass    

    ### suite listeners definitions

    def _start_suite_import_implementation(self):
        pass

    def _end_suite_import_implementation(self):
        pass
        
    def _passed_end_suite_import_implementation(self):
        pass    

    def _failed_end_suite_import_implementation(self):
        pass  
        
    def _skipped_end_suite_import_implementation(self):
        pass 
        
    def _start_suite_registered_implementation(self):
        pass

    def _end_suite_registered_implementation(self):
        pass

    def _passed_end_suite_registered_implementation(self):
        pass    

    def _failed_end_suite_registered_implementation(self):
        pass  
        
    def _skipped_end_suite_registered_implementation(self):
        pass              

    def _tokenize_listener(self, command):
        arrayed = [token.strip() for token in command.split(self.token_separator)]
        return arrayed

       

    def _start_keyword(self, name, attrs):
        self._start_keyword_import_implementation()
        self._start_keyword_registered_implementation()


    def _end_keyword(self, name, attrs):
        self._end_keyword_import_implementation()
        self._end_keyword_registered_implementation()
        if attrs["status"] == "FAIL":
            self._failed_end_keyword_import_implementation()
            self._failed_end_keyword_registered_implementation()
        if attrs["status"] == "PASS":
            self._passed_end_keyword_import_implementation()
            self._passed_end_keyword_registered_implementation()
        if attrs["status"] == "SKIP":
            self._skipped_end_keyword_import_implementation()
            self._skipped_end_keyword_registered_implementation()

    def _start_test(self, name, attrs):
        self._start_test_import_implementation()
        self._start_test_registered_implementation()


    def _end_test(self, name, attrs):
        self._end_test_import_implementation()
        self._end_test_registered_implementation()
        if attrs["status"] == "FAIL":
            self._failed_end_test_import_implementation()
            self._failed_end_test_registered_implementation()
        if attrs["status"] == "PASS":
            self._passed_end_test_import_implementation()
            self._passed_end_test_registered_implementation()
        if attrs["status"] == "SKIP":
            self._skipped_end_test_import_implementation()
            self._skipped_end_test_registered_implementation()


    def _start_suite(self, name, attrs):
        self._start_suite_import_implementation()
        self._start_suite_registered_implementation()

    def _end_suite(self, name, attrs):
        self._end_suite_import_implementation()
        self._end_suite_registered_implementation()
        if attrs["status"] == "FAIL":
            self._failed_end_suite_import_implementation()
            self._failed_end_suite_registered_implementation()
        if attrs["status"] == "PASS":
            self._passed_end_suite_import_implementation()
            self._passed_end_suite_registered_implementation()
        if attrs["status"] == "SKIP":
            self._skipped_end_suite_import_implementation()
            self._skipped_end_suite_registered_implementation()

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
        | Register Start Keyword Listener  Element Should Be Not Visible  id="error-message"
        """
        global _start_keyword_registered_implementation
        def _start_keyword_registered_implementation():
            BuiltIn().run_keyword(kwname, *args)

    def unregister_start_keyword_listener(self):
        """Allows to unregister keyword acting as start keyword listener. After this keyword, listener defined by `Register Start Keyword Listener` will not be executed anymore.
        """
        global _start_keyword_registered_implementation
        def _start_keyword_registered_implementation():
            pass

    def register_end_keyword_listener(self, kwname, *args):
        """Allows to register keyword as end keyword listener. After this keyword, keyword defined as _kwname_ will be executed after each keyword during test execution.
        Executing this keyword once again *does not* register new listener, but redefines existing one.

        Example:
        | Register End Keyword Listener  Element Should Be Not Visible  id="error-message"
        """
        global _end_keyword_registered_implementation
        def _end_keyword_registered_implementation():
            BuiltIn().run_keyword(kwname, *args)

    def unregister_end_keyword_listener(self):
        """Allows to unregister keyword acting as start keyword listener. After this keyword, listener defined by `Register End Keyword Listener` will not be executed anymore.
        """
        global _end_keyword_registered_implementation
        def _end_keyword_registered_implementation():
            pass







    def register_start_test_listener(self, kwname, *args):
        """Allows to register keyword as start test listener. After this keyword, keyword defined as _kwname_ will be executed before each test during test execution.
        Executing this keyword once again *does not* register new listener, but redefines existing one. *Note* - this does not override Test Setup setting.

        Example:
        | Register Start Test Listener  Element Should Be Not Visible  id="error-message"
        """
        global _start_test_registered_implementation
        def _start_test_registered_implementation():
            BuiltIn().run_keyword(kwname, *args)

    def unregister_start_test_listener(self):
        """Allows to unregister keyword acting as start test listener. After this keyword, listener defined by `Register Start Test Listener` will not be executed anymore.
        """
        global _start_test_registered_implementation
        def _start_test_registered_implementation():
            pass

    def register_end_test_listener(self, kwname, *args):
        """Allows to register keyword as end test listener. After this keyword, keyword defined as _kwname_ will be executed after each test during test execution.
        Executing this keyword once again *does not* register new listener, but redefines existing one. *Note* - this does not override Test Teardown setting.

        Example:
        | Register End Test Listener  Element Should Be Not Visible  id="error-message"
        """
        global _end_test_registered_implementation
        def _end_test_registered_implementation():
            BuiltIn().run_keyword(kwname, *args)

    def unregister_end_test_listener(self):
        """Allows to unregister keyword acting as end test listener. After this keyword, listener defined by `Register End Test Listener` will not be executed anymore.
        """
        global _end_test_registered_implementation
        def _end_test_registered_implementation():
            pass





    def register_start_suite_listener(self, kwname, *args):
        """Allows to register keyword as start suite listener. After this keyword, keyword defined as _kwname_ will be executed before each suite during test execution.
        Executing this keyword once again *does not* register new listener, but redefines existing one. *Note* - this does not override Suite Setup setting.

        Example:
        | Register Start Suite Listener  Element Should Be Not Visible  id="error-message"
        """
        global _start_suite_registered_implementation
        def _start_suite_registered_implementation():
            BuiltIn().run_keyword(kwname, *args)

    def unregister_start_suite_listener(self):
        """Allows to unregister keyword acting as start suite listener. After this keyword, listener defined by `Register Start Suite Listener` will not be executed anymore.
        """
        global _start_suite_registered_implementation
        def _start_suite_registered_implementation():
            pass

    def register_end_suite_listener(self, kwname, *args):
        """Allows to register keyword as end suite listener. After this keyword, keyword defined as _kwname_ will be executed after each suite during test execution.
        Executing this keyword once again *does not* register new listener, but redefines existing one. *Note* - this does not override Suite Teardown setting.

        Example:
        | Register End Suite Listener  Element Should Be Not Visible  id="error-message"
        """
        global _end_suite_registered_implementation
        def _end_suite_registered_implementation():
            BuiltIn().run_keyword(kwname, *args)

    def unregister_end_suite_listener(self):
        """Allows to unregister keyword acting as end suite listener. After this keyword, listener defined by `Register End Suite Listener` will not be executed anymore.
        """
        global _end_suite_registered_implementation
        def _end_suite_registered_implementation():
            pass
