
from testing import ModuleTestBase, FunctionTestWithExplanation, StagedTest

class Homework3Test (ModuleTestBase):

    fun_name_1 = "sum_odd_digits"

    tests_fun_1 = (
        ((0,), 0, '0'),
        ((5432,), 8, '5 + 3'),
        ((444,), 0, 'no odd digits'),
        ((505,), 10, '5 + 5'),
    )

    fun_name_2 = "sum_even_digits"

    tests_fun_2 = (
        ((0,), 0, '0'),
        ((5432,), 6, '4 + 2'),
        ((444,), 12, '4 + 4 + 4'),
        ((505,), 0, 'the only even digit is 0'),
    )

    fun_name_3 = "sum_all_digits"

    tests_fun_3 = (
        ((0,), 0, '0'),
        ((5432,), 14, '5 + 4 + 3 + 2'),
        ((444,), 12, '4 + 4 + 4'),
        ((505,), 10, '5 + 0 + 5'),
    )

    def test_function(self, fname, ftests, _suppress_output = False):
        ok, fun, msg = self.find_function(fname)
        if not ok:
            return False, msg
        if fun is None:
            return False, msg
        ft = FunctionTestWithExplanation(fun, ftests,
                                         type_cast_answer = False,
                                         verbose = self.verbose - 1,
                                         raise_exceptions = self.raise_exceptions,
                                         suppress_output = _suppress_output)
        ok, msg = ft.run()
        return ok, msg


    def run(self):
        ## function 1
        print("checking function " + self.fun_name_1 +
              " in file " + self.filepath)
        print()
        ok, msg = self.test_function(self.fun_name_1, self.tests_fun_1,
                                     (self.verbose == 0));
        print(msg)
        ## function 2
        print()
        print("checking function " + self.fun_name_2 +
              " in file " + self.filepath)
        print()
        ok, msg = self.test_function(self.fun_name_2, self.tests_fun_2,
                                     (self.verbose == 0));
        print(msg)
        ## function 2
        print()
        print("checking function " + self.fun_name_3 +
              " in file " + self.filepath)
        print()
        ok, msg = self.test_function(self.fun_name_3, self.tests_fun_3,
                                     (self.verbose == 0));
        print(msg)

    ## end Homework3Test


## To produce less verbose output, change 3 to 2 or 1:

Homework3Test("digit_sums.py", verbose = 3).run()
