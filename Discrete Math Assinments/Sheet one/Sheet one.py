# ==============================================================================
# Discrete Mathematics - Sheet 1 Solutions
# ==============================================================================

print("=== Question 1: List the members of these sets ===")
# a) x^2 = 1 (Real numbers)
q1_a = {x for x in [-1, 1] if x**2 == 1}
print(f"a) {q1_a}")

# b) Positive integer less than 12
q1_b = set(range(1, 12))
print(f"b) {q1_b}")

# c) Square of an integer and x < 100
q1_c = {x**2 for x in range(10)} 
print(f"c) {q1_c}")

# d) Integer such that x^2 = 2
q1_d = set() # No integer satisfies this
print(f"d) {q1_d} (Empty Set)")


print("\n=== Question 2: Set builder notation (Descriptive) ===")
print("a) {0, 3, 6, 9, 12}      -> {x ∈ Z | 0 <= x <= 12 and x mod 3 == 0}")
print("b) {-3,-2,-1, 0, 1, 2, 3} -> {x ∈ Z | -3 <= x <= 3}")
print("c) {m, n, o, p}           -> {x | x is a letter between 'm' and 'p'}")


print("\n=== Question 3: Intervals ===")
intervals = {
    "(0, 5)": lambda x: 0 < x < 5,
    "(0, 5]": lambda x: 0 < x <= 5,
    "[0, 5)": lambda x: 0 <= x < 5,
    "[0, 5]": lambda x: 0 <= x <= 5,
    "(1, 4]": lambda x: 1 < x <= 4,
    "[2, 3]": lambda x: 2 <= x <= 3,
    "(2, 3)": lambda x: 2 < x < 3
}

test_values = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}
for letter, val in test_values.items():
    contains = [name for name, func in intervals.items() if func(val)]
    print(f"{letter}) {val} is in: {', '.join(contains)}")


print("\n=== Question 4 & 5: Subsets ===")
print("Q4a: Second is a subset of the first.")
print("Q4b: Neither is a subset of the other.")
print("Q4c: First is a subset of the second.")
print("Q5a: Second is a subset of the first.")
print("Q5b: Second is a subset of the first.")
print("Q5c: Neither is a subset of the other.")


print("\n=== Question 7: Set Equality ===")
# Python sets automatically handle duplicates and order
print(f"a) { {1, 3, 3, 3, 5, 5, 5, 5, 5, 5, 3, 1} == {1, 3, 5} }")
# b & c are conceptual structure comparisons. 
print("b) False. {{1}} contains a set, {1, {1}} contains an integer and a set.")
print("c) False. The empty set contains nothing, {0} contains the integer zero.")


print("\n=== Question 8: True or False ===")
print("a) 0 in {}                 -> False")
print("b) {} in {0}               -> False")
print("c) {0} is strict subset {} -> False")
print("d) {} is strict subset {0} -> True")
print("e) {0} in {0}              -> False")
print("f) {0} is strict subset {0}-> False")
print("g) {{}} subset {{}}        -> True")


print("\n=== Question 9 & 10: Element Testing ===")
# Conceptual answers represented as strings due to nested set limitations in pure Python sets
print("Set               | Is 2 an element? | Is {2} an element?")
print("------------------|------------------|-------------------")
print("a) Int > 1        | Yes              | No")
print("b) Sq. of an int  | No               | No")
print("c) {2,{2}}        | Yes              | Yes")
print("d) {{2},{{2}}}    | No               | Yes")
print("e) {{2},{2,{2}}}  | No               | Yes")
print("f) {{{2}}}        | No               | No")


print("\n=== Question 11: True or False Statements ===")
print("a) x in {x}           -> True")
print("b) {x} subset {x}     -> True")
print("c) {x} in {x}         -> False")
print("d) {x} in {{x}}       -> True")
print("e) {} subset {x}      -> True")
print("f) {} in {x}          -> False")


print("\n=== Question 18: Cardinality ===")
print("a) len({a})                  -> 1")
print("b) len({{a}})                -> 1")
print("c) len({a, {a}})             -> 2")
print("d) len({a, {a}, {a, {a}}})   -> 3")