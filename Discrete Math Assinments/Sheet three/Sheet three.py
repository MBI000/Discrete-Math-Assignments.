# ==============================================================================
# Discrete Mathematics - Sheet 3 Solutions
# ==============================================================================

print("=== Question 1 & 2: Identifying Propositions ===")
# A proposition is a declarative sentence that is either strictly True or False.
print("Q1 a) Proposition. Truth Value: True")
print("Q1 b) Proposition. Truth Value: False (Tallahassee is the capital of Florida)")
print("Q1 c) Proposition. Truth Value: True")
print("Q1 d) Proposition. Truth Value: False")
print("Q1 e) Not a proposition (Depends on the value of x)")
print("Q1 f) Not a proposition (It is a command/imperative)")

print("\nQ2 a) Not a proposition (Command)")
print("Q2 b) Not a proposition (Question)")
print("Q2 c) Proposition. Truth Value: False (Maine has black flies)")
print("Q2 d) Not a proposition (Depends on x)")
print("Q2 e) Proposition. Truth Value: False")
print("Q2 f) Not a proposition (Depends on n)")


print("\n=== Question 12: Biconditionals (p <-> q) ===")
# True if and only if both sides share the same truth value
q12_a = (2 + 2 == 4) == (1 + 1 == 2)
q12_b = (1 + 1 == 2) == (2 + 3 == 4)
q12_c = (1 + 1 == 3) == False # Assuming monkeys cannot fly is False
q12_d = (0 > 1) == (2 > 1)

print(f"a) True <-> True   => {q12_a}")
print(f"b) True <-> False  => {q12_b}")
print(f"c) False <-> False => {q12_c}")
print(f"d) False <-> True  => {q12_d}")


print("\n=== Question 13: Conditionals (p -> q) ===")
# p -> q is False ONLY when p is True and q is False. Otherwise, it is True.
def conditional(p, q):
    return not p or q

q13_a = conditional(1 + 1 == 2, 2 + 2 == 5)
q13_b = conditional(1 + 1 == 3, 2 + 2 == 4)
q13_c = conditional(1 + 1 == 3, 2 + 2 == 5)
q13_d = conditional(False, 1 + 1 == 3) # Assuming monkeys cannot fly

print(f"a) True -> False   => {q13_a}")
print(f"b) False -> True   => {q13_b}")
print(f"c) False -> False  => {q13_c}")
print(f"d) False -> False  => {q13_d}")

print("\n(Note: Remaining logic translation questions are conceptual and fully detailed in the Markdown file below.)")