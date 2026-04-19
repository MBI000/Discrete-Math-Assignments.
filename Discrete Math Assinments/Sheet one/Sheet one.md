# Discrete Mathematics - Sheet 1 Solutions

**Course Code:** CBS 205
**Institution:** Al Ryada University for Science and Technology

---

## Question 1: List the members of these sets

* **a) $\{x \mid x \text{ is a real number such that } x^2=1\}$**
  * **Steps:** Solve the algebraic equation $x^2 = 1$. Taking the square root of both sides gives two real number solutions: $1$ and $-1$.
  * **Answer:** $\{-1, 1\}$
* **b) $\{x \mid x \text{ is a positive integer less than } 12\}$**
  * **Steps:** Identify all integers strictly greater than zero and strictly less than $12$.
  * **Answer:** $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11\}$
* **c) $\{x \mid x \text{ is the square of an integer and } x < 100\}$**
  * **Steps:** Calculate the squares of integers starting from $0$ ($0^2, 1^2, 2^2...$) until the result reaches $100$. Stop strictly below $100$ as requested by the inequality.
  * **Answer:** $\{0, 1, 4, 9, 16, 25, 36, 49, 64, 81\}$
* **d) $\{x \mid x \text{ is an integer such that } x^2=2\}$**
  * **Steps:** Solve the equation $x^2 = 2$. The solutions are $\sqrt{2}$ and $-\sqrt{2}$. Neither of these are integers, meaning no elements satisfy the set's conditions.
  * **Answer:** $\emptyset$ (The empty set)

---

## Question 2: Use set builder notation to give a description of each of these sets

* **a) $\{0, 3, 6, 9, 12\}$**
  * **Steps:** Observe the numerical pattern. The numbers are non-negative multiples of $3$, maxing out at $12$.
  * **Answer:** $\{x \in \mathbb{Z} \mid 0 \le x \le 12 \text{ and } x \text{ is a multiple of } 3\}$
* **b) $\{-3, -2, -1, 0, 1, 2, 3\}$**
  * **Steps:** The elements are consecutive integers spanning continuously from $-3$ to $3$.
  * **Answer:** $\{x \in \mathbb{Z} \mid -3 \le x \le 3\}$
* **c) $\{m, n, o, p\}$**
  * **Steps:** These are consecutive lowercase letters in the standard English alphabet.
  * **Answer:** $\{x \mid x \text{ is a letter in the English alphabet between 'm' and 'p' inclusive}\}$

---

## Question 3: Intervals

*Context: Determine which of the intervals $(0, 5), (0, 5], [0, 5), [0, 5], (1, 4], [2, 3], (2, 3)$ contain the specified numbers.* Parentheses `( )` indicate exclusive bounds (number not included), and brackets `[ ]` indicate inclusive bounds (number included).

* **a) 0**: Included only where the lower bound is a bracket at zero.
  * **Answer:** $[0, 5), [0, 5]$
* **b) 1**: Included in bounds starting at $0$, but excluded from bounds starting exclusively at $1$.
  * **Answer:** $(0, 5), (0, 5], [0, 5), [0, 5]$
* **c) 2**: Included in the $0$ to $5$ bounds, the $1$ to $4$ bounds, and the inclusive $2$ to $3$ bound.
  * **Answer:** $(0, 5), (0, 5], [0, 5), [0, 5], (1, 4], [2, 3]$
* **d) 3**: Excluded from the exclusive $2$ to $3$ interval, but present in the others.
  * **Answer:** $(0, 5), (0, 5], [0, 5), [0, 5], (1, 4], [2, 3]$
* **e) 4**: Present in the wider $0$ to $5$ intervals and the inclusive upper bound of $1$ to $4$.
  * **Answer:** $(0, 5), (0, 5], [0, 5), [0, 5], (1, 4]$
* **f) 5**: Only present where the upper bound of $5$ is an inclusive bracket.
  * **Answer:** $(0, 5], [0, 5]$

---

## Questions 4 & 5: Determine Subsets

*Context: Determine whether the first is a subset of the second, the second is a subset of the first, or neither.*

* **4a) Airline flights vs. nonstop airline flights (NY to New Delhi)**
  * **Answer:** The **second is a subset of the first**. All nonstop flights are flights, but not all flights are nonstop.
* **4b) People who speak English vs. people who speak Chinese**
  * **Answer:** **Neither is a subset of the other**. Being in one linguistic group does not strictly guarantee membership in the other.
* **4c) Flying squirrels vs. living creatures that can fly**
  * **Answer:** The **first is a subset of the second**. Every flying squirrel is definitively a creature capable of flight.
* **5a) People who speak English vs. people who speak English with an Australian accent**
  * **Answer:** The **second is a subset of the first**. Everyone with an Australian accent speaking English is, by definition, an English speaker.
* **5b) Fruits vs. citrus fruits**
  * **Answer:** The **second is a subset of the first**. All citrus fruits belong to the broader category of fruits.
* **5c) Students studying discrete mathematics vs. data structures**
  * **Answer:** **Neither is a subset of the other**. While these sets likely overlap in computer science programs, neither exclusively contains all members of the other.

---

## Question 7: Set Equality

* **a) $\{1, 3, 3, 3, 5, 5, 5, 5, 5, 5, 3, 1\}$ and $\{1, 3, 5\}$**
  * **Steps:** In mathematical set theory, duplicates and ordering are entirely ignored. The first set reduces precisely to the unique elements $1, 3,$ and $5$.
  * **Answer:** Yes, they are equal.
* **b) $\{\{1\}\}$ and $\{1, \{1\}\}$**
  * **Steps:** The first set contains exactly one element: the set $\{1\}$. The second set contains two elements: the integer $1$ and the set $\{1\}$.
  * **Answer:** No, they are not equal.
* **c) $\emptyset$ and $\{0\}$**
  * **Steps:** The empty set contains exactly zero elements. The second set contains one element: the integer $0$.
  * **Answer:** No, they are not equal.

---

## Question 8: True or False Statements

* **a) $0 \in \emptyset$**  -> **False.** The empty set contains absolutely nothing, including zero.
* **b) $\emptyset \in \{0\}$**  -> **False.** The set only contains the number $0$, it does not contain the empty set as an element.
* **c) $\{0\} \subset \emptyset$**  -> **False.** A non-empty set cannot be a subset of an empty set.
* **d) $\emptyset \subset \{0\}$**  -> **True.** The empty set is considered a proper subset of any non-empty set.
* **e) $\{0\} \in \{0\}$**  -> **False.** The set contains the integer $0$, not a nested set containing $0$.
* **f) $\{0\} \subset \{0\}$**  -> **False.** A set cannot be a *strict/proper* subset ($\subset$) of itself.
* **g) $\{\emptyset\} \subseteq \{\emptyset\}$**  -> **True.** Every set is a non-strict subset ($\subseteq$) of itself.

---

## Questions 9 & 10: Element Testing

| Set | Q9: Is $2$ an element? | Q10: Is $\{2\}$ an element? |
| :--- | :--- | :--- |
| **a)** $\{x \in \mathbb{R} \mid x \text{ is an integer } > 1\}$ | **Yes.** $2$ is an integer $> 1$. | **No.** It contains raw integers, not sets. |
| **b)** $\{x \in \mathbb{R} \mid x \text{ is the square of an integer}\}$ | **No.** $2$ is not a perfect square. | **No.** It only contains raw integers. |
| **c)** $\{2, \{2\}\}$ | **Yes.** The integer $2$ is explicitly listed. | **Yes.** The set $\{2\}$ is explicitly listed. |
| **d)** $\{\{2\}, \{\{2\}\}\}$ | **No.** The elements are sets, not integers. | **Yes.** $\{2\}$ is the first listed element. |
| **e)** $\{\{2\}, \{2, \{2\}\}\}$ | **No.** Both elements are sets. | **Yes.** $\{2\}$ is the first listed element. |
| **f)** $\{\{\{2\}\}\}$ | **No.** The only element is the nested set $\{\{2\}\}$. | **No.** The only element is $\{\{2\}\}$. |

---

## Question 11: True or False Statements

* **a) $x \in \{x\}$**  -> **True.** The set explicitly contains the element $x$.
* **b) $\{x\} \subseteq \{x\}$**  -> **True.** Any set is a non-strict subset of itself.
* **c) $\{x\} \in \{x\}$**  -> **False.** The set contains the raw element $x$, not the nested set containing $x$.
* **d) $\{x\} \in \{\{x\}\}$**  -> **True.** The outer set contains exactly one element, which is the inner set $\{x\}$.
* **e) $\emptyset \subseteq \{x\}$**  -> **True.** The empty set is universally a subset of every set.
* **f) $\emptyset \in \{x\}$**  -> **False.** The set only contains $x$, it does not list the empty set as a member.

---

## Question 12 & 17: Venn Diagrams

### Q12: Months without the letter 'R'

1. Draw a large rectangle to represent the Universal Set ($U$), which includes all 12 months of the year.
2. Draw a circle inside the box labeled $M$.
3. Inside the circle $M$, list the months without 'R': **May, June, July, August**.
4. Outside the circle but inside the bounding box $U$, list the remaining months: **January, February, March, April, September, October, November, December**.

### Q17: Relationships $A \subset B$ and $B \subset C$

1. Draw a large outer circle and label it $C$.
2. Draw a medium-sized circle entirely inside circle $C$ and label it $B$. This visually represents that $B$ is a subset of $C$.
3. Draw a smaller circle entirely inside circle $B$ and label it $A$. This visually represents that $A$ is a subset of $B$ (and by extension, $C$).

---

## Question 18: Cardinality

*Context: Cardinality refers to the total number of distinct, comma-separated elements at the root level of a set.*

* **a) $\{a\}$**
  * **Steps:** There is exactly one element: the letter 'a'.
  * **Answer:** $1$
* **b) $\{\{a\}\}$**
  * **Steps:** There is exactly one element: the set containing 'a'.
  * **Answer:** $1$
* **c) $\{a, \{a\}\}$**
  * **Steps:** There are two distinct elements separated by a comma: the letter 'a' and the set $\{a\}$.
  * **Answer:** $2$
* **d) $\{a, \{a\}, \{a, \{a\}\}\}$**
  * **Steps:** There are three distinct elements separated by commas at the root level: the letter 'a', the set $\{a\}$, and the set $\{a, \{a\}\}$.
  * **Answer:** $3$
