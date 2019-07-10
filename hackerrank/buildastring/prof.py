import cProfile

import build
import build_test


cases = build_test.load_cases(build_test.case7_path)
case = cases[2]
expt = build_test.expt7[2]

cases = build_test.load_cases(build_test.case11_path)
case = cases[0]
expt = build_test.expt11[0]

cProfile.run("""
table = build.dp_fw(*case)
print("{} ?= {}".format(table[-1], expt))""")
