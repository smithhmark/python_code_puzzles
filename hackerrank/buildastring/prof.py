import cProfile

import build
import build_test

cases = build_test.load_cases(build_test.case11_path)

cProfile.run("""
table = build.dp_fw(*cases[1])
print("{} ?= {}".format(table[-1], build_test.expt11[2]))""")
