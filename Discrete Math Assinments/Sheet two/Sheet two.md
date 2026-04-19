# Discrete Mathematics - Sheet 2 Solutions

**Course Code:** CBS 205
**Institution:** Al Ryada University for Science and Technology

---

## Question 1: Cartesian Products

**Given:** Let $A=\{a,b,c,d\}$ and $B=\{y,z\}$.

* **a) $A\times B$**
  * **Steps:** The Cartesian product $A \times B$ pairs every element in $A$ with every element in $B$ as an ordered pair $(a, b)$.
  * **Answer:** $\{(a, y), (a, z), (b, y), (b, z), (c, y), (c, z), (d, y), (d, z)\}$
* **b) $B\times A$**
  * **Steps:** Pair every element in $B$ with every element in $A$ as an ordered pair $(b, a)$.
  * **Answer:** $\{(y, a), (y, b), (y, c), (y, d), (z, a), (z, b), (z, c), (z, d)\}$

---

## Question 2: Triple Cartesian Products

**Given:** Let $A=\{a,b,c\}$, $B=\{x,y\}$, and $C=\{0,1\}$.

* **a) $A\times B\times C$**
  * **Answer:** $\{(a,x,0), (a,x,1), (a,y,0), (a,y,1), (b,x,0), (b,x,1), (b,y,0), (b,y,1), (c,x,0), (c,x,1), (c,y,0), (c,y,1)\}$
* **b) $C\times B\times A$**
  * **Answer:** $\{(0,x,a), (0,x,b), (0,x,c), (0,y,a), (0,y,b), (0,y,c), (1,x,a), (1,x,b), (1,x,c), (1,y,a), (1,y,b), (1,y,c)\}$
* **c) $C\times A\times B$**
  * **Answer:** $\{(0,a,x), (0,a,y), (0,b,x), (0,b,y), (0,c,x), (0,c,y), (1,a,x), (1,a,y), (1,b,x), (1,b,y), (1,c,x), (1,c,y)\}$
* **d) $B\times B\times B$**
  * **Answer:** $\{(x,x,x), (x,x,y), (x,y,x), (x,y,y), (y,x,x), (y,x,y), (y,y,x), (y,y,y)\}$

---

## Question 3: Find $A^2$

**Note:** $A^2$ is shorthand for the Cartesian product $A \times A$.

* **a) $A=\{0,1,3\}$**
  * **Answer:** $\{(0,0), (0,1), (0,3), (1,0), (1,1), (1,3), (3,0), (3,1), (3,3)\}$
* **b) $A=\{1,2,a,b\}$**
  * **Answer:** $\{(1,1), (1,2), (1,a), (1,b), (2,1), (2,2), (2,a), (2,b), (a,1), (a,2), (a,a), (a,b), (b,1), (b,2), (b,a), (b,b)\}$

---

## Question 4: Cardinality of a Cartesian Product

**Question:** How many different elements does $A\times B$ have if A has m elements and B has n elements?

* **Answer:** $m \times n$ (or $mn$) elements. The fundamental counting principle states that if choosing the first element has $m$ options and the second element has $n$ options, there are $mn$ total combinations.

---

## Question 5: Associativity of Cartesian Products

**Question:** Explain why $A\times B\times C$ and $(A\times B)\times C$ are not the same.

* **Answer:** The elements of $A\times B\times C$ are 3-tuples (triplets) formatted as $(a, b, c)$. The elements of $(A\times B)\times C$ are 2-tuples (pairs) where the first element is itself a pair, formatted as $((a, b), c)$. Because $(a, b, c) \neq ((a, b), c)$ structurally, the sets are not technically equal.

---

## Question 6 & 7: Set Operations

**Context for Q6:** Let A be the set of students who live within one mile of school and let B be the set of students who walk to classes. Describe the students in each of these sets.

* **$A\cap B$:** Students who live within one mile of school AND walk to classes.
* **$A\cup B$:** Students who EITHER live within one mile of school OR walk to classes (or both) .
* **$A-B$:** Students who live within one mile of school BUT DO NOT walk to classes.
* **$B-A$:** Students who walk to classes BUT DO NOT live within one mile of school.

**Context for Q7:** Let $A=\{1,2,3,4,5\}$ and $B=\{0,3,6\}$. Find:

* **a) $A\cup B$:** $\{0, 1, 2, 3, 4, 5, 6\}$
* **b) $A\cap B$:** $\{3\}$
* **c) $A-B$:** $\{1, 2, 4, 5\}$
* **d) $B-A$:** $\{0, 6\}$

---

## Question 8: Reverse Engineering Sets

**Given:** Find the sets A and B if $A-B=\{1,5,7,8\}$, $B-A=\{2,10\}$, and $A\cap B=\{3,6,9\}$.

* **Steps:**
  * Set $A$ is formed by uniting elements uniquely in $A$ with the shared elements: $A = (A-B) \cup (A\cap B)$.
  * Set $B$ is formed by uniting elements uniquely in $B$ with the shared elements: $B = (B-A) \cup (A\cap B)$.
* **Answer:**
  * $A = \{1, 3, 5, 6, 7, 8, 9\}$
  * $B = \{2, 3, 6, 9, 10\}$

---

## Question 9: Multiple Set Operations

**Given:** Let $A=\{0,2,4,6,8,10\}$, $B=\{0,1,2,3,4,5,6\}$, and $C=\{4,5,6,7,8,9,10\}$.

* **a) $A\cap B\cap C$**
  * **Steps:** Find elements present in all three sets.
  * **Answer:** $\{4, 6\}$
* **b) $A\cup B\cup C$**
  * **Steps:** Combine all unique elements from all three sets.
  * **Answer:** $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$
* **c) $(A\cup B)\cap C$**
  * **Steps:** First find $A\cup B = \{0, 1, 2, 3, 4, 5, 6, 8, 10\}$. Then intersect with $C$.
  * **Answer:** $\{4, 5, 6, 8, 10\}$
* **d) $(A\cap B)\cup C$**
  * **Steps:** First find $A\cap B = \{0, 2, 4, 6\}$. Then unite with $C$.
  * **Answer:** $\{0, 2, 4, 5, 6, 7, 8, 9, 10\}$

---

## Question 10: Set Property Deductions

**What can you say about sets A and B if we know that:**

* **a) $A\cup B=A$?**
  * **Answer:** This implies that every element in $B$ is already in $A$. Therefore, $B \subseteq A$.
* **b) $A\cap B=A^{\prime}$?**
  * **Answer:** $A^{\prime}$ is the complement of $A$, meaning it contains no elements of $A$. Because $A \cap B$ must be a subset of $A$, the only way for it to equal $A^{\prime}$ is if $A^{\prime} = \emptyset$. This means $A = U$ (the universal set). If $A = U$, then $A \cap B = U \cap B = B$. Therefore, $B = \emptyset$.
* **c) $A-B=A^{\prime}$?**
  * **Answer:** $A-B$ yields a subset of $A$. $A^{\prime}$ contains no elements of $A$. For a subset of $A$ to equal $A^{\prime}$, it must be that $A^{\prime} = \emptyset$. This means $A = U$. Consequently, $U-B = \emptyset$, meaning $B = U$.
* **d) $A\cap B=B\cap A^{\prime}$?**
  * **Answer:** The right side $B\cap A^{\prime}$ is equivalent to $B-A$. The intersection of $(A\cap B)$ and $(B-A)$ is always empty. For them to be equal, both must be empty. Therefore, $B = \emptyset$.
* **e) $A-B=B-A^{\prime}$?**
  * **Answer:** The right side $B-A^{\prime}$ is equivalent to $B\cap (A^{\prime})^{\prime} = B\cap A$. So the equation is $A-B = A\cap B$. Since $A-B$ and $A\cap B$ are disjoint, they can only be equal if both are the empty set $\emptyset$. For $A-B=\emptyset$, $A \subseteq B$. For $A\cap B=\emptyset$, they share no elements. Both conditions can only be true if $A = \emptyset$.

---

## Question 11: Set Verification

**Verify the statement: $(\overline{A\cap B})\cup(\overline{A}\cap\overline{B}\cap C)\cup A=U$**. State clearly the law used in each step.

* **Step 1:** Apply De Morgan's Law to the first term.
  * $(\overline{A} \cup \overline{B}) \cup (\overline{A} \cap \overline{B} \cap C) \cup A$
* **Step 2:** Use the Commutative and Associative Laws to group $\overline{A}$ and $A$.
  * $(\overline{A} \cup A) \cup \overline{B} \cup (\overline{A} \cap \overline{B} \cap C)$
* **Step 3:** Apply the Complement Law ($\overline{A} \cup A = U$).
  * $U \cup \overline{B} \cup (\overline{A} \cap \overline{B} \cap C)$
* **Step 4:** Apply the Domination Law ($U \cup X = U$).
  * $U$

---

## Question 12: Word Problem (Venn Diagram)

**Data Given:**

* 100 users interviewed.
* 30 used brand X only.
* 22 used brand Y only.
* 18 used brand Z only.
* 8 used brands X and Y.
* 9 used brands X and Z.
* 7 used brands Z and Y.
* 14 used none of the brands.

**Calculations:**
Let total users in at least one brand = $100 - 14 = 86$.
Let $k$ = users of X, Y, and Z.
The intersection of "X and Y" includes those who used X, Y, and Z. Therefore, users of *only* X and Y = $8 - k$.
Similarly, *only* X and Z = $9 - k$.
Similarly, *only* Z and Y = $7 - k$.

Summing all distinct regions yields the total active users (86):
$$30 + 22 + 18 + (8-k) + (9-k) + (7-k) + k = 86$$
$$70 + 24 - 2k = 86$$
$$94 - 2k = 86 \implies 2k = 8 \implies k = 4$$

* **(a) How many users used brands X, Y and Z?**
  * **Answer:** $4$ users.
* **(b) How many users used brands X and Z but not brand Y?**
  * **Steps:** This region represents those using only X and Z, which is calculated as $9 - k$.
  * **Answer:** $9 - 4 = 5$ users.

---

## Question 13: Cranes and Subassemblies

**Data Given:**

* Crane A = $\{a, b, c, d\}$
* Crane B = $\{a, c, f\}$
* Crane C = $\{b, d, e\}$
* Subassembly a = $\{p, q, r, s\}$
* Subassembly b = $\{q, r, t, v\}$
* Subassembly c = $\{p, r, s, t\}$
* Subassembly d = $\{p, w, y\}$
* Subassembly e = $\{u, x\}$
* Subassembly f = $\{p, r, u, v, x, y\}$

**Part (a) Give the make-up of the following subassemblies:**

* **(i) $a\cup b$**
  * **Answer:** $\{p, q, r, s, t, v\}$
* **(ii) $a\cup c\cup f$**
  * **Answer:** $\{p, q, r, s, t, u, v, x, y\}$
* **(iii) $d\cup e$**
  * **Answer:** $\{p, u, w, x, y\}$

**Part (b) Shared Components:** Given that A is made in Newcastle, and B and C are made in Birmingham, what components need to be available on both sites?

* **Steps:**
  1. Find components needed in Newcastle (Crane A): $a \cup b \cup c \cup d = \{p, q, r, s\} \cup \{q, r, t, v\} \cup \{p, r, s, t\} \cup \{p, w, y\} = \{p, q, r, s, t, v, w, y\}$.
  2. Find components needed in Birmingham (Cranes B and C): $(a \cup c \cup f) \cup (b \cup d \cup e) = \{p, q, r, s, t, u, v, x, y\} \cup \{p, q, r, t, u, v, w, x, y\} = \{p, q, r, s, t, u, v, w, x, y\}$.
  3. Find the intersection of components needed at both locations.
* **Answer:** $\{p, q, r, s, t, v, w, y\}$ (Essentially, all components required for Crane A must be present at both sites).
