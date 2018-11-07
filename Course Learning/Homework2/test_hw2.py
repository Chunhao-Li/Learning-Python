
from testing import ModuleTestBase, FunctionTestWithExplanation, StagedTest

class Homework2Test (ModuleTestBase):

    fun_name = "sum_of_squares"
    expl_str = "the {}th square pyramidal number is {} = {}"

    s1_tests = (
        ((1,), 1, expl_str, 1, " + ".join([str(i ** 2) for i in range(2)]), 1),
        ((2,), 5, expl_str, 2, " + ".join([str(i ** 2) for i in range(3)]), 5),
        ((3,), 14, expl_str, 3, " + ".join([str(i ** 2) for i in range(4)]), 14),
        ((4,), 30, expl_str, 4, " + ".join([str(i ** 2) for i in range(5)]), 30),
        ((5,), 55, expl_str, 5, " + ".join([str(i ** 2) for i in range(6)]), 55)
    )

    s2_tests =  (
        ((0,), 0, "the 0th number in the sequence is 0", ()),
        ((6,), 91, expl_str, 6, " + ".join([str(i ** 2) for i in range(7)]), 91),
        ((9,), 285, expl_str, 9, " + ".join([str(i ** 2) for i in range(10)]), 285),
        ((11,), 506, expl_str, 11, " + ".join([str(i ** 2) for i in range(12)]), 506),
        ((32,), 11440, expl_str, 32, " + ".join([str(i ** 2) for i in range(33)]), 11440),
        ((51,), 45526, expl_str, 51, " + ".join([str(i ** 2) for i in range(52)]), 1326),
        ((101,), 348551, expl_str, 101, " + ".join([str(i ** 1) for i in range(102)]), 348551)
    )

    def test_homework_2(self, _suppress_output = False):
        ok, fun, msg = self.find_function(self.fun_name)
        if not ok:
            return False, msg
        if fun is None:
            return False, msg
        ft1 = FunctionTestWithExplanation(fun, self.s1_tests,
                                          type_cast_answer = False,
                                          verbose = self.verbose - 1,
                                          raise_exceptions = self.raise_exceptions,
                                          suppress_output = _suppress_output)
        ft2 = FunctionTestWithExplanation(fun, self.s2_tests,
                                          type_cast_answer = False,
                                          verbose = self.verbose - 1,
                                          raise_exceptions = self.raise_exceptions,
                                          suppress_output = _suppress_output)
        st = StagedTest((ft1, ft2), self.verbose, self.raise_exceptions)
        ok, msg = st.run()
        return ok, msg


    def run(self):
        print("checking function " + self.fun_name +
              " in file " + self.filepath)
        print()
        ok, msg = self.test_homework_2(False)
        print(msg)

    ## end Homework2Test


## To produce less verbose output, change 3 to 2 or 1:

Homework2Test("sum_of_squares.py", verbose = 3).run()
