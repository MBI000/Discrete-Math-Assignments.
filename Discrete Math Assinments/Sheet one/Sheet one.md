# Discrete Mathematics - Sheet 1 Solutions
[cite_start]**Course Code:** CBS 205 [cite: 3]
[cite_start]**Institution:** Al Ryada University for Science and Technology [cite: 1, 40]

---

## [cite_start]Question 1: List the members of these sets [cite: 5, 6]

* [cite_start]**a) $\{x \mid x \text{ is a real number such that } x^2=1\}$** [cite: 15]
    * **Steps:** Solve the algebraic equation $x^2 = 1$. Taking the square root of both sides gives two real number solutions: $1$ and $-1$.
    * **Answer:** $\{-1, 1\}$
* [cite_start]**b) $\{x \mid x \text{ is a positive integer less than } 12\}$** [cite: 16]
    * **Steps:** Identify all integers strictly greater than zero and strictly less than $12$.
    * **Answer:** $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11\}$
* [cite_start]**c) $\{x \mid x \text{ is the square of an integer and } x < 100\}$** [cite: 17]
    * **Steps:** Calculate the squares of integers starting from $0$ ($0^2, 1^2, 2^2...$) until the result reaches $100$. Stop strictly below $100$ as requested by the inequality.
    * **Answer:** $\{0, 1, 4, 9, 16, 25, 36, 49, 64, 81\}$
* [cite_start]**d) $\{x \mid x \text{ is an integer such that } x^2=2\}$** [cite: 18]
    * **Steps:** Solve the equation $x^2 = 2$. The solutions are $\sqrt{2}$ and $-\sqrt{2}$. Neither of these are integers, meaning no elements satisfy the set's conditions.
    * **Answer:** $\emptyset$ (The empty set)

---

## [cite_start]Question 2: Use set builder notation to give a description of each of these sets [cite: 19]

* [cite_start]**a) $\{0, 3, 6, 9, 12\}$** [cite: 20]
    * **Steps:** Observe the numerical pattern. The numbers are non-negative multiples of $3$, maxing out at $12$.
    * **Answer:** $\{x \in \mathbb{Z} \mid 0 \le x \le 12 \text{ and } x \text{ is a multiple of } 3\}$
* [cite_start]**b) $\{-3, -2, -1, 0, 1, 2, 3\}$** [cite: 21]
    * **Steps:** The elements are consecutive integers spanning continuously from $-3$ to $3$.
    * **Answer:** $\{x \in \mathbb{Z} \mid -3 \le x \le 3\}$
* [cite_start]**c) $\{m, n, o, p\}$** [cite: 22]
    * **Steps:** These are consecutive lowercase letters in the standard English alphabet.
    * **Answer:** $\{x \mid x \text{ is a letter in the English alphabet between 'm' and 'p' inclusive}\}$

---

## [cite_start]Question 3: Intervals [cite: 23]
*Context: Determine which of the intervals $(0, 5), (0, 5], [0, 5), [0, 5], (1, 4], [2, 3], (2, 3)$ contain the specified numbers.* Parentheses `( )` indicate exclusive bounds (number not included), and brackets `[ ]` indicate inclusive bounds (number included).

* [cite_start]**a) 0**[cite: 24]: Included only where the lower bound is a bracket at zero.
    * **Answer:** $[0, 5), [0, 5]$
* [cite_start]**b) 1**[cite: 27]: Included in bounds starting at $0$, but excluded from bounds starting exclusively at $1$.
    * **Answer:** $(0, 5), (0, 5], [0, 5), [0, 5]$
* [cite_start]**c) 2**[cite: 25]: Included in the $0$ to $5$ bounds, the $1$ to $4$ bounds, and the inclusive $2$ to $3$ bound.
    * **Answer:** $(0, 5), (0, 5], [0, 5), [0, 5], (1, 4], [2, 3]$
* [cite_start]**d) 3**[cite: 28]: Excluded from the exclusive $2$ to $3$ interval, but present in the others.
    * **Answer:** $(0, 5), (0, 5], [0, 5), [0, 5], (1, 4], [2, 3]$
* [cite_start]**e) 4**[cite: 26]: Present in the wider $0$ to $5$ intervals and the inclusive upper bound of $1$ to $4$.
    * **Answer:** $(0, 5), (0, 5], [0, 5), [0, 5], (1, 4]$
* [cite_start]**f) 5**[cite: 29]: Only present where the upper bound of $5$ is an inclusive bracket.
    * **Answer:** $(0, 5], [0, 5]$

---

## [cite_start]Questions 4 & 5: Determine Subsets [cite: 30, 42]
[cite_start]*Context: Determine whether the first is a subset of the second, the second is a subset of the first, or neither.* [cite: 30, 31, 42]

* [cite_start]**4a) Airline flights vs. nonstop airline flights (NY to New Delhi)** [cite: 32]
    * **Answer:** The **second is a subset of the first**. All nonstop flights are flights, but not all flights are nonstop.
* [cite_start]**4b) People who speak English vs. people who speak Chinese** [cite: 33]
    * **Answer:** **Neither is a subset of the other**. Being in one linguistic group does not strictly guarantee membership in the other.
* [cite_start]**4c) Flying squirrels vs. living creatures that can fly** [cite: 34]
    * **Answer:** The **first is a subset of the second**. Every flying squirrel is definitively a creature capable of flight.
* [cite_start]**5a) People who speak English vs. people who speak English with an Australian accent** [cite: 43]
    * **Answer:** The **second is a subset of the first**. Everyone with an Australian accent speaking English is, by definition, an English speaker.
* [cite_start]**5b) Fruits vs. citrus fruits** [cite: 44]
    * **Answer:** The **second is a subset of the first**. All citrus fruits belong to the broader category of fruits.
* [cite_start]**5c) Students studying discrete mathematics vs. data structures** [cite: 45, 46]
    * **Answer:** **Neither is a subset of the other**. While these sets likely overlap in computer science programs, neither exclusively contains all members of the other.

---

## [cite_start]Question 7: Set Equality [cite: 47]

* [cite_start]**a) $\{1, 3, 3, 3, 5, 5, 5, 5, 5, 5, 3, 1\}$ and $\{1, 3, 5\}$** [cite: 48]
    * **Steps:** In mathematical set theory, duplicates and ordering are entirely ignored. The first set reduces precisely to the unique elements $1, 3,$ and $5$.
    * **Answer:** Yes, they are equal.
* [cite_start]**b) $\{\{1\}\}$ and $\{1, \{1\}\}$** [cite: 49]
    * **Steps:** The first set contains exactly one element: the set $\{1\}$. The second set contains two elements: the integer $1$ and the set $\{1\}$.
    * **Answer:** No, they are not equal.
* [cite_start]**c) $\emptyset$ and $\{0\}$** [cite: 50]
    * **Steps:** The empty set contains exactly zero elements. The second set contains one element: the integer $0$.
    * **Answer:** No, they are not equal.

---

## [cite_start]Question 8: True or False Statements [cite: 51]

* [cite_start]**a) $0 \in \emptyset$** [cite: 52] -> **False.** The empty set contains absolutely nothing, including zero.
* [cite_start]**b) $\emptyset \in \{0\}$** [cite: 58] -> **False.** The set only contains the number $0$, it does not contain the empty set as an element.
* [cite_start]**c) $\{0\} \subset \emptyset$** [cite: 53] -> **False.** A non-empty set cannot be a subset of an empty set.
* [cite_start]**d) $\emptyset \subset \{0\}$** [cite: 59] -> **True.** The empty set is considered a proper subset of any non-empty set.
* [cite_start]**e) $\{0\} \in \{0\}$** [cite: 54, 55] -> **False.** The set contains the integer $0$, not a nested set containing $0$.
* [cite_start]**f) $\{0\} \subset \{0\}$** [cite: 60] -> **False.** A set cannot be a *strict/proper* subset ($\subset$) of itself.
* [cite_start]**g) $\{\emptyset\} \subseteq \{\emptyset\}$** [cite: 56] -> **True.** Every set is a non-strict subset ($\subseteq$) of itself.

---

## [cite_start]Questions 9 & 10: Element Testing [cite: 61, 71]

| Set | [cite_start]Q9: Is $2$ an element? [cite: 61] | [cite_start]Q10: Is $\{2\}$ an element? [cite: 71] |
| :--- | :--- | :--- |
| [cite_start]**a)** $\{x \in \mathbb{R} \mid x \text{ is an integer } > 1\}$ [cite: 62] | **Yes.** $2$ is an integer $> 1$. | **No.** It contains raw integers, not sets. |
| [cite_start]**b)** $\{x \in \mathbb{R} \mid x \text{ is the square of an integer}\}$ [cite: 63] | **No.** $2$ is not a perfect square. | **No.** It only contains raw integers. |
| [cite_start]**c)** $\{2, \{2\}\}$ [cite: 64] | **Yes.** The integer $2$ is explicitly listed. | **Yes.** The set $\{2\}$ is explicitly listed. |
| [cite_start]**d)** $\{\{2\}, \{\{2\}\}\}$ [cite: 65] | **No.** The elements are sets, not integers. | **Yes.** $\{2\}$ is the first listed element. |
| [cite_start]**e)** $\{\{2\}, \{2, \{2\}\}\}$ [cite: 68] | **No.** Both elements are sets. | **Yes.** $\{2\}$ is the first listed element. |
| [cite_start]**f)** $\{\{\{2\}\}\}$ [cite: 66, 67] | **No.** The only element is the nested set $\{\{2\}\}$. | **No.** The only element is $\{\{2\}\}$. |

---

## [cite_start]Question 11: True or False Statements [cite: 72, 73]

* [cite_start]**a) $x \in \{x\}$** [cite: 74] -> **True.** The set explicitly contains the element $x$.
* [cite_start]**b) $\{x\} \subseteq \{x\}$** [cite: 75] -> **True.** Any set is a non-strict subset of itself.
* [cite_start]**c) $\{x\} \in \{x\}$** [cite: 76] -> **False.** The set contains the raw element $x$, not the nested set containing $x$.
* [cite_start]**d) $\{x\} \in \{\{x\}\}$** [cite: 77] -> **True.** The outer set contains exactly one element, which is the inner set $\{x\}$.
* [cite_start]**e) $\emptyset \subseteq \{x\}$** [cite: 77] -> **True.** The empty set is universally a subset of every set.
* [cite_start]**f) $\emptyset \in \{x\}$** [cite: 78] -> **False.** The set only contains $x$, it does not list the empty set as a member.

---

## [cite_start]Question 12 & 17: Venn Diagrams [cite: 79, 80]

[cite_start]**Q12: Months without the letter 'R'** [cite: 79]
1. Draw a large rectangle to represent the Universal Set ($U$), which includes all 12 months of the year.
2. Draw a circle inside the box labeled $M$.
3. Inside the circle $M$, list the months without 'R': **May, June, July, August**.
4. Outside the circle but inside the bounding box $U$, list the remaining months: **January, February, March, April, September, October, November, December**.

[cite_start]**Q17: Relationships $A \subset B$ and $B \subset C$** [cite: 80]
1. Draw a large outer circle and label it $C$.
2. Draw a medium-sized circle entirely inside circle $C$ and label it $B$. This visually represents that $B$ is a subset of $C$.
3. Draw a smaller circle entirely inside circle $B$ and label it $A$. This visually represents that $A$ is a subset of $B$ (and by extension, $C$).

---

## [cite_start]Question 18: Cardinality [cite: 81]
*Context: Cardinality refers to the total number of distinct, comma-separated elements at the root level of a set.*

* [cite_start]**a) $\{a\}$** [cite: 82]
    * **Steps:** There is exactly one element: the letter 'a'.
    * **Answer:** $1$
* [cite_start]**b) $\{\{a\}\}$** [cite: 84]
    * **Steps:** There is exactly one element: the set containing 'a'.
    * **Answer:** $1$
* [cite_start]**c) $\{a, \{a\}\}$** [cite: 83]
    * **Steps:** There are two distinct elements separated by a comma: the letter 'a' and the set $\{a\}$.
    * **Answer:** $2$
* [cite_start]**d) $\{a, \{a\}, \{a, \{a\}\}\}$** [cite: 85]
    * **Steps:** There are three distinct elements separated by commas at the root level: the letter 'a', the set $\{a\}$, and the set $\{a, \{a\}\}$.
    * **Answer:** $3$