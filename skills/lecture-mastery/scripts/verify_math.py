#!/usr/bin/env python3
"""
Verify math with SymPy before presenting it.

Usage:
  verify_math.py equal     "<expr1>" "<expr2>"          # are they identical? (symbolic + numeric spot check)
  verify_math.py simplify  "<expr>"
  verify_math.py diff      "<expr>" <var> [order]
  verify_math.py integrate "<expr>" <var> [a b]         # indefinite, or definite from a to b
  verify_math.py limit     "<expr>" <var> <point> [+|-]
  verify_math.py series    "<expr>" <var> <point> <n>
  verify_math.py solve     "<expr or lhs=rhs>" <var>
  verify_math.py numeric   "<expr>" var=value [var=value ...]
  verify_math.py matrix    "<python list of lists>" [det|inv|eig|rank|rref]

Input syntax: Python/SymPy style; '^' is accepted as power, implicit multiplication (2x) allowed.
Use 'oo' for infinity, 'pi', 'E' or 'exp(1)'.
"""
import random
import sys

import sympy as sp
from sympy.parsing.sympy_parser import (
    convert_xor, implicit_multiplication_application, parse_expr, standard_transformations,
)

T = standard_transformations + (implicit_multiplication_application, convert_xor)


def P(s):
    return parse_expr(s, transformations=T, evaluate=True)


def equal(a, b):
    e1, e2 = P(a), P(b)
    diff = sp.simplify(e1 - e2)
    symbolic = diff == 0
    syms = sorted((e1 - e2).free_symbols, key=str)
    numeric_ok, trials = True, 0
    for _ in range(12):
        subs = {s: sp.Rational(random.randint(-9, 9), random.randint(1, 5)) for s in syms}
        try:
            v1, v2 = complex(e1.subs(subs).evalf()), complex(e2.subs(subs).evalf())
        except Exception:
            continue
        trials += 1
        if abs(v1 - v2) > 1e-8 * max(1, abs(v1), abs(v2)):
            numeric_ok = False
            print(f"counterexample: {subs} -> {v1} vs {v2}")
            break
    verdict = "EQUAL" if (symbolic or (numeric_ok and trials >= 5)) else "NOT EQUAL"
    print(f"{verdict}  (symbolic difference simplifies to: {diff}; numeric trials: {trials}, all agree: {numeric_ok})")


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == "equal":
        equal(args[0], args[1])
    elif cmd == "simplify":
        e = P(args[0])
        print("simplify:", sp.simplify(e))
        print("factor:  ", sp.factor(e))
        print("expand:  ", sp.expand(e))
    elif cmd == "diff":
        v = sp.Symbol(args[1])
        order = int(args[2]) if len(args) > 2 else 1
        r = sp.diff(P(args[0]), v, order)
        print("raw:       ", r)
        print("simplified:", sp.simplify(r))
    elif cmd == "integrate":
        v = sp.Symbol(args[1])
        e = P(args[0])
        if len(args) >= 4:
            r = sp.integrate(e, (v, P(args[2]), P(args[3])))
            print(sp.simplify(r), " ≈ ", sp.N(r))
        else:
            print(sp.simplify(sp.integrate(e, v)), "+ C")
    elif cmd == "limit":
        v = sp.Symbol(args[1])
        d = args[3] if len(args) > 3 else "+-"
        print(sp.limit(P(args[0]), v, P(args[2]), dir=d))
    elif cmd == "series":
        v = sp.Symbol(args[1])
        print(sp.series(P(args[0]), v, P(args[2]), int(args[3])))
    elif cmd == "solve":
        v = sp.Symbol(args[1])
        s = args[0]
        eq = sp.Eq(P(s.split("=")[0]), P(s.split("=")[1])) if "=" in s else P(s)
        print(sp.solve(eq, v))
    elif cmd == "numeric":
        e = P(args[0])
        subs = {sp.Symbol(k): P(val) for k, val in (a.split("=") for a in args[1:])}
        r = e.subs(subs)
        print(sp.simplify(r), " ≈ ", sp.N(r))
    elif cmd == "matrix":
        M = sp.Matrix(eval(args[0], {"__builtins__": {}}, {}))
        op = args[1] if len(args) > 1 else "det"
        if op == "det":
            print(M.det())
        elif op == "inv":
            print(M.inv())
        elif op == "eig":
            for val, mult, vecs in M.eigenvects():
                print(f"eigenvalue {val} (multiplicity {mult}): {[list(v) for v in vecs]}")
        elif op == "rank":
            print(M.rank())
        elif op == "rref":
            print(M.rref())
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
