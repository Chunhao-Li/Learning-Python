
## This module is used by the testing programs.

## Do NOT open, run, modify, move or delete this file.

import sys
import os.path
import importlib
import importlib.machinery
import ast
import io

class ModuleTestBase (object):
    STAGE_READ = 1
    STAGE_PARSE = 2
    STAGE_CHECK = 3
    STAGE_LOAD = 4
    STAGE_TEST = 5

    allowed = (ast.Import, ast.ImportFrom, ast.FunctionDef)

    allowed_modules = None
    forbidden_modules = None

    def __init__(self, arg1, verbose = 0, raise_exceptions = True):
        self.raise_exceptions = raise_exceptions
        self.verbose = verbose
        self.filepath = None
        self.source = None
        self.ast = None
        self.module = None
        if isinstance(arg1, str):
            self.filepath = arg1
            self.name = os.path.basename(self.filepath)
            self.stage = 0
        else:
            self.module = sys.modules['__main__']
            self.stage = self.STAGE_LOAD
        self.warnings = []

    def _parse_file(self):
        assert(isinstance(self.filepath, str))
        try:
            f = open(self.filepath, 'r')
            self.source = f.read() # should read all of the file
            f.close()
        except FileNotFoundError as fnf_exc:
            if self.raise_exceptions:
                raise fnf_exc
            else:
                return False, self.STAGE_READ, "file " + self.filepath + " not found"
        except Exception as exc:
            if self.raise_exceptions:
                raise exc
            else:
                return False, self.STAGE_READ, exc.__class__.__name__ + " " + \
                    str(exc) + " reading file " + self.filepath
        self.stage = self.STAGE_READ
        try:
            self.ast = ast.parse(self.source)
        except Exception as exc:
            if self.raise_exceptions:
                raise exc
            else:
                return False, self.STAGE_PARSE, exc.__class__.__name__ + " " + \
                    str(exc) + " parsing " + self.name
        assert(isinstance(self.ast, ast.Module))
        self.stage = self.STAGE_PARSE
        return True, self.STAGE_PARSE, "file parsed ok"

    def _check_ast_exception(self, item):
        if type(item) == ast.Expr:
            assert hasattr(item, 'value')
            if type(item.value) == ast.Str:
                self.warnings.append(("docstring outside function def",
                                      self.name + ", line " + str(item.lineno)))
                return True
        return False

    def _check_ast(self):
        assert(isinstance(self.ast, ast.Module))
        for item in ast.iter_child_nodes(self.ast):
            if self._check_ast_exception(item):
                continue
            elif type(item) not in self.allowed:
                msg = self.name + ", line " + str(item.lineno) + " : " \
                    + item.__class__.__name__ + " is not allowed" + \
                    "\n(only import statements and function definitions)"
                if self.raise_exceptions:
                    raise Exception(msg)
                else:
                    return False, self.STAGE_CHECK, msg
        self.stage = self.STAGE_CHECK
        return True, self.STAGE_CHECK, "ast check ok"

    def _recursive_check_imports(self, node, allowed, forbidden):
        msg = ""
        ok = True
        for item in ast.iter_child_nodes(node):
            if type(item) == ast.Import:
                assert hasattr(item, 'names')
                assert isinstance(item.names, list)
                assert len(item.names) > 0
                for alias in item.names:
                    assert hasattr(alias, 'name')
                    assert isinstance(alias.name, str)
                    if allowed is not None:
                        if alias.name not in allowed:
                            if len(msg) > 0:
                                msg += "; "
                            msg += self.name + ", line " + str(item.lineno) \
                                   + " : " + " use of module " + alias.name \
                                   + " is not allowed"
                            ok = False
                    if forbidden is not None:
                        if alias.name in forbidden:
                            if len(msg) > 0:
                                msg += "; "
                            msg += self.name + ", line " + str(item.lineno) \
                                   + " : " + " use of module " + alias.name \
                                   + " is not allowed"
                            ok = False
            elif type(item) == ast.ImportFrom:
                assert hasattr(item, 'module')
                assert isinstance(item.module, str)
                if allowed is not None:
                    if item.module not in allowed:
                        if len(msg) > 0:
                            msg += "; "
                        msg += self.name + ", line " + str(item.lineno) \
                               + " : " + " use of module " + item.module \
                               + " is not allowed"
                        ok = False
                if forbidden is not None:
                    if item.module in forbidden:
                        if len(msg) > 0:
                            msg += "; "
                        msg += self.name + ", line " + str(item.lineno) \
                               + " : " + " use of module " + item.module \
                               + " is not allowed"
                        ok = False
            else:
                r_ok, r_msg = self._recursive_check_imports(item, allowed, forbidden)
                if not r_ok:
                    if len(msg) > 0:
                        msg += "; "
                    msg += r_msg
                ok = ok & r_ok
        return ok, msg

    def _check_imports(self, allowed = None, forbidden = None):
        assert(isinstance(self.ast, ast.Module))
        ok, msg = self._recursive_check_imports(self.ast, allowed, forbidden)
        if not ok:
            if self.raise_exceptions:
                raise Exception(msg)
            else:
                return False, self.STAGE_CHECK, msg
        self.stage = self.STAGE_CHECK
        return True, self.STAGE_CHECK, "import check ok"

    def _load_file(self):
        assert(isinstance(self.filepath, str))
        loader = importlib.machinery.SourceFileLoader("_test_mod", self.filepath)
        try:
            self.module = loader.load_module()
        except ImportError as exc:
            if self.raise_exceptions:
                raise exc
            else:
                return False, self.STAGE_LOAD, "error " + str(exc) + \
                    " loading " + self.filepath
        self.stage = self.STAGE_LOAD
        return True, self.STAGE_LOAD, "load ok"

    def test_LOAD(self):
        if self.stage < self.STAGE_CHECK:
            (ok, stage, msg) = self.test_CHECK()
            if not ok:
                return False, stage, msg
        return self._load_file()

    def test_CHECK(self):
        if self.stage < self.STAGE_PARSE:
            (ok, stage, msg) = self._parse_file()
            if not ok:
                return False, stage, msg
        (ok, stage, msg) = self._check_ast()
        if ok:
            if self.allowed_modules is not None or \
               self.forbidden_modules is not None:
                (ok, stage, msg) = self._check_imports(self.allowed_modules,
                                                       self.forbidden_modules)
        return ok, stage, msg

    def run(self):
        return self.test_LOAD()

    def find_function(self, name):
        if self.stage < self.STAGE_LOAD:
            (ok, stage, msg) = self.test_LOAD()
            if not ok:
                return False, stage, msg
        if name not in self.module.__dict__:
            return True, None, name + " is not defined in " + self.name \
                + " (did you name it _exactly_ as the problem requires?)"
        fun = self.module.__dict__[name]
        if type(fun) != type(ModuleTestBase.find_function):
            return False, None, name + " is defined in " + self.name + \
                " but it is not a function"
        return True, fun, "ok"

    ## end class ModuleTestBase

class ReadOnlyStringIO (io.StringIO):

    def writable(self):
        return False

    def seekable(self):
        return False

class FunctionTestBase (object):

    def __init__(self, function, tests = tuple(),
                 type_cast_answer = True,
                 verbose = 0, raise_exceptions = True,
                 suppress_output = False):
        self.raise_exceptions = raise_exceptions
        self.suppress_output = suppress_output
        self.verbose = verbose
        self.function = function
        self.name = function.__name__
        self.tests = tests
        self.type_cast_answer = type_cast_answer
        self.details = None
        self.collate = 0

    # Methods _get_test_args and _check_answer can be overridden
    # by subclasses to extend/specialise the definition of a test
    # case (and/or the way the function return value is compared
    # to the expected value, and/or the message produced if it is
    # not correct). The default implementation (i.e., this class)
    # assumes a test is two-element sequence (args, ans), and that
    # answers are checked with simple equality.
    def _get_test_args(self, test):
        return test[0]

    def _str_tuple(self, args):
        return '(' + ', '.join([repr(arg) for arg in args]) + ')'

    def _test_type_ctor(self, test):
        return type(test[1])

    def _type_check_answer(self, test, fvalue):
        # special check for no return:
        if type(fvalue) == type(None):
            msg = "call " + self.name + self._str_tuple(self._get_test_args(test)) + \
                  " did not return any value (missing return statement?)"
            if self.raise_exceptions:
                raise Exception(msg)
            else:
                return False, msg
        # first, check if type already matches:
        if type(fvalue) == type(test[1]):
            return True, fvalue
        # if type casting enabled, check if returned value can
        # be cast to expected type:
        if self.type_cast_answer:
            ok = False
            try:
                fvalue_type = type(fvalue)
                expected_type = self._test_type_ctor(test)
                type_cast_fvalue = expected_type(fvalue)
                #print(fvalue, expected_type, type_cast_fvalue)
                if fvalue_type(type_cast_fvalue) == fvalue:
                    ok = True
                    fvalue = type_cast_fvalue
            except:
                pass
            if not ok:
                msg = "call " + self.name + self._str_tuple(self._get_test_args(test)) + \
                    " returned the value " + str(fvalue) + " of type " + \
                    str(type(fvalue)) + \
                    " which could not be converted to the type " + \
                    str(type(test[1])) + " of the expected answer " + \
                    str(test[1])
                if self.raise_exceptions:
                    raise Exception(msg)
                else:
                    return False, msg
        # else (type casting not enabled), check return type matches exactly
        elif type(fvalue) != type(test[1]):
            msg = "call " + self.name + self._str_tuple(self._get_test_args(test)) + \
                  " returned incorrect type " + str(type(fvalue)) \
                  + "; the expected type is " + str(type(test[1]))
            if self.raise_exceptions:
                raise Exception(msg)
            else:
                return False, msg
        return True, fvalue

    def _check_answer(self, test, fvalue):
        ok, result = self._type_check_answer(test, fvalue)
        if not ok:
            return ok, result
        fvalue = result
        # check returned value matches (equal)
        if fvalue != test[1]:
            msg = "call " + self.name + self._str_tuple(self._get_test_args(test)) + \
                  " returned incorrect answer " + str(fvalue) \
                  + "; the expected answer is " + str(test[1])
            if self.raise_exceptions:
                raise Exception(msg)
            else:
                return False, msg
        else:
            return True, "call " + self.name + self._str_tuple(self._get_test_args(test)) + " ok"

    def _run_test(self, test):
        args = self._get_test_args(test)
        if self.verbose > 1:
            print("calling " + self.name + self._str_tuple(args))
        try:
            fvalue = self.function(*args)
        except Exception as exc:
            msg = "call " + self.name + self._str_tuple(args) + " caused " \
                + exc.__class__.__name__ + " " + str(exc)
            if self.raise_exceptions:
                raise Exception(msg)
            else:
                return False, msg
        return self._check_answer(test, fvalue)

    def run(self):
        n_passed = 0
        self.details = []
        sys_stdin = sys.stdin
        sys_stdout = sys.stdout
        sys.stdin =  ReadOnlyStringIO('')
        if self.suppress_output:
            sys.stdout =  io.StringIO('')
        for num, test in enumerate(self.tests):
            passed, msg = self._run_test(test)
            if passed:
                n_passed += 1
            self.details.append((num, passed, msg))
            if self.verbose > 0:
                print(msg)
        sys.stdin =  sys_stdin
        if self.suppress_output:
            sys.stdout =  sys_stdout
        if self.collate == 2:
            rmsg = "; ".join(["#{}: {}".format(num, msg)
                              for (num, was_ok, msg) in self.details])
        elif self.collate == 1:
            if n_passed == 0:
                rmsg = "all (" + str(len(self.tests)) + ") tests failed"
            elif n_passed < len(self.tests):
                rmsg = str(len(self.tests) - n_passed) + " of " \
                       + str(len(self.tests)) + " tests failed: " \
                       + "; ".join(["#{}: {}".format(num, msg) for
                                    (num, was_ok, msg) in self.details
                                    if not was_ok])
            else:
                rmsg = str(len(self.tests)) + " tests passed"
        else:
            if n_passed < len(self.tests):
                rmsg = str(len(self.tests) - n_passed) + " of " \
                       + str(len(self.tests)) + " tests failed"
            else:
                rmsg = str(len(self.tests)) + " tests passed"
        return n_passed >= len(self.tests), rmsg

    def total(self):
        ## can only be called after tests have run:
        assert self.details is not None
        passed = 0
        failed = 0
        for (num, was_ok, msg) in self.details:
            if was_ok:
                passed += 1
            else:
                failed += 1
        return passed, failed

    ## end class FunctionTestBase


class FunctionTestWithExplanation (FunctionTestBase):

    # def __init__(self, function, tests = tuple(),
    #              type_cast_answer = True, 
    #              verbose = 0, raise_exceptions = True,
    #              suppress_output = False):
    #     FunctionTestBase.__init__(self, function, tests, type_cast_answer,
    #                               verbose, raise_exceptions, suppress_output)

    def _make_explanation(self, test):
        if len(test) > 3:
            expl = " (" + test[2].format(*test[3:]) + ")"
        elif len(test) > 2:
            expl = " (" + test[2] + ")"
        else:
            expl = ""
        return expl

    def _check_answer(self, test, fvalue):
        ok, result = self._type_check_answer(test, fvalue)
        if not ok:
            return ok, result
        fvalue = result
        # check returned value matches (equal)
        if fvalue != test[1]:
            msg = "call " + self.name + self._str_tuple(self._get_test_args(test)) + \
                " returned incorrect answer " + str(fvalue) \
                + "; the expected answer is " + str(test[1]) \
                + self._make_explanation(test)
            if self.raise_exceptions:
                raise Exception(msg)
            else:
                return False, msg
        else:
            return True, "call " + self.name + self._str_tuple(self._get_test_args(test)) + " ok"

    ## end class FunctionTestWithExplanation


class FunctionTestReturningFloat (FunctionTestWithExplanation):

    def __init__(self, function, tests = tuple(), precision = 1e-5,
                 verbose = 0, raise_exceptions = True,
                 suppress_output = False):
        FunctionTestBase.__init__(self, function, tests, True, verbose,
                                  raise_exceptions, suppress_output)
        self.precision = precision

    def _check_answer(self, test, fvalue):
        ok, result = self._type_check_answer(test, fvalue)
        if not ok:
            return ok, result
        fvalue = result
        # check returned value matches (to precision):
        if abs(fvalue - test[1]) > self.precision:
            msg = "call " + self.name + self._str_tuple(self._get_test_args(test)) + \
                " returned incorrect answer " + str(fvalue) \
                + "; the expected answer is " + str(test[1]) \
                + self._make_explanation(test) \
                + " and the difference is > " + str(self.precision)
            if self.raise_exceptions:
                raise Exception(msg)
            else:
                return False, msg
        else:
            return True, "call " + self.name + self._str_tuple(self._get_test_args(test)) + " ok"

    ## end class FunctionTestReturningFloat

class FunctionTestOnMutableArgs (FunctionTestWithExplanation):

    import copy

    def _run_test(self, test):
        args = self._get_test_args(test)
        args1 = self.copy.deepcopy(args)
        if self.verbose > 1:
            print("calling " + self.name + self._str_tuple(args))
        try:
            fvalue = self.function(*args1)
        except Exception as exc:
            msg = "call " + self.name + self._str_tuple(args) + " caused " \
                + exc.__class__.__name__ + " " + str(exc)
            if self.raise_exceptions:
                raise Exception(msg)
            else:
                return False, msg
        if not (args1 == args):
            msg = "call " + self.name + self._str_tuple(args) \
                + " modified argument(s): " + self._str_tuple(args1)
            if self.raise_exceptions:
                raise Exception(msg)
            else:
                return False, msg
        return self._check_answer(test, fvalue)

    ## end class FunctionTestOnMutableArgs

class StagedTest:

    def __init__(self, tests = tuple(), verbose = 0,
                 raise_exceptions = True):
        self.raise_exceptions = raise_exceptions
        self.verbose = verbose
        self.tests = tests
        self.details = None
        self.collate = 0

    def run(self):
        n_passed = 0
        self.details = []
        for (i, test) in enumerate(self.tests):
            if self.verbose > 1:
                print("testing stage " + str(i + 1))
            passed, msg = test.run()
            if passed:
                n_passed += 1
            self.details.append((i + 1, passed, msg))
            if self.verbose > 0:
                print("stage " + str(i + 1) + ": " + msg)
        if n_passed == len(self.tests):
            return True, "all stages passed"
        elif n_passed == 0:
            if self.collate == 1:
                return False, "all stages failed (" + self.failed_stage_messages() + ")"
            else:
                return False, "all stages failed"
        else:
            if self.collate == 1:
                return False, "stages " + " & ".join([str(snum) for snum in self.solved()]) + \
                    " of " + str(len(self.tests)) + " passed (" + self.failed_stage_messages() + ")"
            else:
                return False, "stages " + " & ".join([str(snum) for snum in self.solved()]) + \
                    " of " + str(len(self.tests)) + " passed"

    def solved(self):
        ## this can only be called after tests have been run
        assert self.details is not None
        return [snum for snum, spass, _ in self.details if spass]

    def total(self):
        ## can only be called after tests have run:
        assert self.details is not None
        passed = 0
        failed = 0
        for test in self.tests:
            stage_passed, stage_failed = test.total()
            passed += stage_passed
            failed += stage_failed
        return passed, failed

    def totals_by_stage(self):
        ## can only be called after tests have run:
        assert self.details is not None
        return [test.total() for test in self.tests]

    def failed_stage_messages(self):
        ## this can only be called after tests have been run
        assert self.details is not None
        return "; ".join([str(snum) + ":" + smsg for snum, spass, smsg in self.details if not spass])
        
    ## end class StagedTest
