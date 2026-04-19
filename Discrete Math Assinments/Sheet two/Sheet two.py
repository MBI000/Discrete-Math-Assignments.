import itertools

print("=== Question 1: Cartesian Products ===")
A1 = {'a', 'b', 'c', 'd'}
B1 = {'y', 'z'}
print(f"a) A x B: {list(itertools.product(A1, B1))}")
print(f"b) B x A: {list(itertools.product(B1, A1))}")


print("\n=== Question 2: Triple Cartesian Products ===")
A2 = {'a', 'b', 'c'}
B2 = {'x', 'y'}
C2 = {0, 1}
print(f"a) A x B x C: {list(itertools.product(A2, B2, C2))}")
print(f"b) C x B x A: {list(itertools.product(C2, B2, A2))}")
print(f"c) C x A x B: {list(itertools.product(C2, A2, B2))}")
print(f"d) B x B x B: {list(itertools.product(B2, B2, B2))}")


print("\n=== Question 3: A^2 (A x A) ===")
A3_a = {0, 1, 3}
A3_b = {1, 2, 'a', 'b'}
print(f"a) A^2: {list(itertools.product(A3_a, A3_a))}")
print(f"b) A^2: {list(itertools.product(A3_b, A3_b))}")


print("\n=== Question 6 & 7: Set Operations ===")
A7 = {1, 2, 3, 4, 5}
B7 = {0, 3, 6}
print(f"Q7 a) A U B: {A7 | B7}")
print(f"Q7 b) A n B: {A7 & B7}")
print(f"Q7 c) A - B: {A7 - B7}")
print(f"Q7 d) B - A: {B7 - A7}")


print("\n=== Question 8: Reverse Engineering Sets ===")
# Given: A - B = {1, 5, 7, 8}, B - A = {2, 10}, A n B = {3, 6, 9}
A_minus_B = {1, 5, 7, 8}
B_minus_A = {2, 10}
A_int_B = {3, 6, 9}
A8 = A_minus_B | A_int_B
B8 = B_minus_A | A_int_B
print(f"A = {A8}")
print(f"B = {B8}")


print("\n=== Question 9: Multiple Set Operations ===")
A9 = {0, 2, 4, 6, 8, 10}
B9 = {0, 1, 2, 3, 4, 5, 6}
C9 = {4, 5, 6, 7, 8, 9, 10}
print(f"a) A n B n C: {A9 & B9 & C9}")
print(f"b) A U B U C: {A9 | B9 | C9}")
print(f"c) (A U B) n C: {(A9 | B9) & C9}")
print(f"d) (A n B) U C: {(A9 & B9) | C9}")


print("\n=== Question 12: Venn Diagram Word Problem ===")
total_users = 100
none = 14
at_least_one = total_users - none # 86
x_only = 30
y_only = 22
z_only = 18
# Given equations: 
# (X n Y) = xy_only + k = 8  => xy_only = 8 - k
# (X n Z) = xz_only + k = 9  => xz_only = 9 - k
# (Y n Z) = yz_only + k = 7  => yz_only = 7 - k
# Sum of all parts = 86
# 30 + 22 + 18 + (8 - k) + (9 - k) + (7 - k) + k = 86
# 94 - 2k = 86 => 2k = 8 => k = 4
k = 4
print(f"(a) Users who used all three (k): {k}")
print(f"(b) Users who used X and Z but not Y (xz_only): {9 - k}")


print("\n=== Question 13: Cranes and Subassemblies ===")
a = {'p', 'q', 'r', 's'}
b = {'q', 'r', 't', 'v'}
c = {'p', 'r', 's', 't'}
d = {'p', 'w', 'y'}
e = {'u', 'x'}
f = {'p', 'r', 'u', 'v', 'x', 'y'}

print(f"(a)(i) a U b: {a | b}")
print(f"(a)(ii) a U c U f: {a | c | f}")
print(f"(a)(iii) d U e: {d | e}")

crane_A = a | b | c | d
crane_B = a | c | f
crane_C = b | d | e
birmingham_components = crane_B | crane_C
newcastle_components = crane_A
needed_on_both = newcastle_components & birmingham_components

print(f"(b) Components needed on both sites: {needed_on_both}")