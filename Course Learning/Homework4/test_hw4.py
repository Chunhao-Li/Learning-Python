# -*- coding: utf-8 -*-

from testing import ModuleTestBase, FunctionTestReturningFloat, StagedTest

class Homework4Test (ModuleTestBase):

    fun_name = "max_increase"
    expl_str = "the increase from index {} to index {}"

    s0_tests = (
        (((1,2,3,2),), 2, expl_str, 0, 2),
        (((1,3,1,2),), 2, expl_str, 0, 1),
        (((3,-1,2,1),), 3, expl_str, 1, 2),
        (((3,2,1,1),), 0, "there is no increasing pair"),
        (((1,),), 0, "there is no pair (length < 2)")
    )

    btc_data = [ 6729.44, 6690.88, 6526.36, 6359.98, 6475.89, 6258.74,
                 6485.10, 6396.64, 6579.00, 6313.51, 6270.20, 6195.01,
                 6253.67, 6313.90, 6233.10, 6139.99, 6546.45, 6282.50,
                 6718.22, 6941.20, 7030.01, 7017.61, 7414.08, 7533.92,
                 7603.99, 7725.43, 8170.01, 8216.74, 8235.70, 8188.00,
                 7939.00, 8174.06 ]
    btc_data.reverse()

    s1_tests = (
        (((226, 264, 337, 364, 485, 529),), 303, expl_str, 0, 5),
        ((tuple(btc_data),), 589.45, expl_str, 16, 31)
    )

    def test_homework_4(self, _suppress_output = False):
        ok, fun, msg = self.find_function(self.fun_name)
        if not ok:
            return False, msg
        if fun is None:
            return False, msg
        ft0 = FunctionTestReturningFloat(fun, self.s0_tests,
                                         precision = 0.0001,
                                         verbose = self.verbose - 1,
                                         raise_exceptions = self.raise_exceptions,
                                         suppress_output = _suppress_output)
        ft1 = FunctionTestReturningFloat(fun, self.s1_tests,
                                         precision = 0.0001,
                                         verbose = self.verbose - 1,
                                         raise_exceptions = self.raise_exceptions,
                                         suppress_output = _suppress_output)
        st = StagedTest((ft0, ft1), self.verbose, self.raise_exceptions)
        ok, msg = st.run()
        return ok, msg


    def run(self):
        print("checking function " + self.fun_name +
              " in file " + self.filepath)
        print()
        ok, msg = self.test_homework_4(False)
        print(msg)

    ## end Homework4Test


## To produce less verbose output, change verbose from 3 to 2 or 1:

Homework4Test("max_increase.py", verbose = 3).run()
