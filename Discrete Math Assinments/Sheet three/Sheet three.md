<!-- markdownlint-disable MD009 MD011 MD022 MD032 MD052 -->

# Discrete Mathematics - Sheet 3 Solutions
**Course Code:** CBS 205
**Institution:** Al Ryada University for Science and Technology

---

## Question 1: Propositions and Truth Values
*Context: A proposition is a declarative statement that is definitively true or false, but not both. We must determine which sentences are propositions and evaluate their truth values.*

* **a) Boston is the capital of Massachusetts.**
  * **Answer:** This is a proposition. Its truth value is **True**.
* **b) Miami is the capital of Florida.**
  * **Answer:** This is a proposition. Its truth value is **False** (Tallahassee is the capital).
* **c) $2+3=5$**
  * **Answer:** This is a mathematical proposition. Its truth value is **True**.
* **d) $5+7=10$**
  * **Answer:** This is a mathematical proposition. Its truth value is **False**.
* **e) $x+2=11.$**
  * **Answer:** This is **not a proposition**. It is an open sentence whose truth depends on the variable $x$.
* **f) Answer this question.**
  * **Answer:** This is **not a proposition**. It is a command (imperative sentence).

---

## Question 2: Propositions and Truth Values
*Context: Identify propositions and state their truth values.*

* **a) Do not pass go.**
  * **Answer:** **Not a proposition**. It is a command.
* **b) What time is it?**
  * **Answer:** **Not a proposition**. It is a question.
* **c) There are no black flies in Maine.**
  * **Answer:** This is a proposition. Its truth value is **False** (black flies do exist in Maine).
* **d) 4 + x = 5.**
  * **Answer:** **Not a proposition**. The truth depends on the variable $x$.
* **e) The moon is made of green cheese.**
  * **Answer:** This is a proposition. Its truth value is **False**.
* **f) $2^{n}\ge100$.**
  * **Answer:** **Not a proposition**. The truth depends on the value of the variable $n$.

---

## Question 3, 4, & 5: Negation of Propositions
*Context: Find the logical negation (opposite) of each statement.*

**Question 3:**
* **a) Linda is younger than Sanjay.**  $\rightarrow$ Linda is not younger than Sanjay (or Linda is older than or the same age as Sanjay).
* **b) Mei makes more money than Isabella.**  $\rightarrow$ Mei does not make more money than Isabella.
* **c) Moshe is taller than Monica.**  $\rightarrow$ Moshe is not taller than Monica.
* **d) Abby is richer than Ricardo.**  $\rightarrow$ Abby is not richer than Ricardo.

**Question 4:**
* **a) Mei has an MP3 player.**  $\rightarrow$ Mei does not have an MP3 player.
* **b) There is no pollution in New Jersey.**  $\rightarrow$ There is pollution in New Jersey.
* **c) 2+1=3.**  $\rightarrow$ $2+1 \neq 3$.
* **d) The summer in Maine is hot and sunny.**  $\rightarrow$ The summer in Maine is not hot or it is not sunny (applying De Morgan's Law to the English language).

**Question 5:**
* **a) Steve has more than 100 GB free disk space on his laptop.**  $\rightarrow$ Steve does not have more than 100 GB of free disk space on his laptop.
* **b) Zach blocks e-mails and texts from Jennifer.**  $\rightarrow$ Zach does not block e-mails and texts from Jennifer.
* **c) 71113= 999.**  $\rightarrow$ $71113 \neq 999$.
* **d) Diane rode her bicycle 100 miles on Sunday.**  $\rightarrow$ Diane did not ride her bicycle 100 miles on Sunday.

---

## Question 6: Truth Values and Negations
*Context: Determine the truth values and state their negation statements.*

* **(a) Everyone can say where they were when President J. F. Kennedy was assassinated**
  * **Truth Value:** False (many people alive today were born after the event).
  * **Negation:** Not everyone can say where they were when President J. F. Kennedy was assassinated (or: Someone cannot say...).
* **(b) $2^{n}=n^{2}$ for some $n\in\mathbb{N}$, where N is the set of natural numbers**
  * **Truth Value:** True (it holds true for $n=2$ and $n=4$).
  * **Negation:** $2^{n} \neq n^{2}$ for all $n \in \mathbb{N}$.
* **(c) The number 5 is negative**
  * **Truth Value:** False.
  * **Negation:** The number 5 is not negative.
* **(d) $2^{89~301}+1$ is a prime number**
  * **Truth Value:** False (Numbers of the form $a^3 + b^3$ are factorable, and the exponent 89301 is divisible by 3).
  * **Negation:** $2^{89~301}+1$ is not a prime number.
* **(e) Air temperatures were never above $0^{\circ}C$ in February 1935 in Bristol, UK**
  * **Truth Value:** False (historically, temperatures fluctuate above freezing in the UK).
  * **Negation:** Air temperatures were above $0^{\circ}C$ at least once in February 1935 in Bristol, UK.

---

## Question 7: Why are these not propositions?
*Context: Explain why the sentences are not propositions.*

* **(a) Maths is fun** : This is a subjective opinion, not a statement with an objective truth value.
* **(b) Your place or mine?** : This is a question.
* **(c) y-x=x-y** : This is an open equation whose truth depends entirely on the unspecified variables $x$ and $y$.
* **(d) Why am I reading this?** : This is a question.
* **(e) Flowers are more interesting than calculus** : This is a subjective opinion.
* **(f) n is a prime number** : The truth of this statement depends on the value of the variable $n$.
* **(g) He won an Olympic medal** : The truth depends on the unspecified pronoun "He".

---

## Question 8: Logical Translations
*Context: A: It is frosty , B: It is after 11.00 a.m. , C: Jim drives safely.*

* **(a) Translate into logical statements:**
  * (i) It is not frosty: **$\neg A$**
  * (ii) It is frosty and after 11.00 a.m.: **$A \wedge B$**
  * (iii) It is not frosty, it is before 11.00 a.m. and Jim drives safely: **$\neg A \wedge \neg B \wedge C$**
* **(b) Translate into English sentences:**
  * (i) $A\wedge\wedge B$ : **It is frosty and it is after 11.00 a.m.** (Note: assuming typographic error in source's double wedge ).
  * (ii) $\tilde{A}\rightarrow C$ : **If it is not frosty, then Jim drives safely.**
  * (iii) $A\wedge\tilde{B}\rightarrow\tilde{C}$ : **If it is frosty and it is not after 11.00 a.m., then Jim does not drive safely.**
  * (iv) $\tilde{A}\vee B\rightarrow C$ : **If it is not frosty or it is after 11.00 a.m., then Jim drives safely.**

---

## Question 9: Compound Propositions to English
*Context: p: "Swimming at the New Jersey shore is allowed" . q: "Sharks have been spotted near the shore".*

* **a) q** : Sharks have been spotted near the shore.
* **b) $p\wedge q$** : Swimming at the New Jersey shore is allowed, and sharks have been spotted near the shore.
* **c) $\neg p\vee q$** : Swimming at the New Jersey shore is not allowed, or sharks have been spotted near the shore.
* **d) $p\rightarrow\neg q$** : If swimming at the New Jersey shore is allowed, then sharks have not been spotted near the shore.
* **e) $\neg q\rightarrow p$** : If sharks have not been spotted near the shore, then swimming at the New Jersey shore is allowed.
* **f) $\neg p\rightarrow\neg q$** : If swimming at the New Jersey shore is not allowed, then sharks have not been spotted near the shore.
* **g) $p\leftrightarrow\neg q$** : Swimming at the New Jersey shore is allowed if and only if sharks have not been spotted near the shore.
* **h) $\neg p\wedge(p\vee\neg q)$** : Swimming at the New Jersey shore is not allowed, and either swimming is allowed or sharks have not been spotted near the shore.

---

## Question 10 & 11: English to Logical Connectives
**Question 10 Context:** p: It is below freezing . q: It is snowing.
* **a)** It is below freezing and snowing : **$p \wedge q$**
* **b)** It is below freezing but not snowing : **$p \wedge \neg q$**
* **c)** It is not below freezing and it is not snowing : **$\neg p \wedge \neg q$**
* **d)** It is either snowing or below freezing (or both) : **$q \vee p$**
* **e)** If it is below freezing, it is also snowing : **$p \rightarrow q$**
* **f)** Either it is below freezing or it is snowing, but it is not snowing if it is below freezing : **$(p \vee q) \wedge (p \rightarrow \neg q)$**
* **g)** That it is below freezing is necessary and sufficient for it to be snowing : **$p \leftrightarrow q$**

**Question 11 Context:** p: You drive over 65 miles per hour . q: You get a speeding ticket.
* **a)** You do not drive over 65 miles per hour : **$\neg p$**
* **b)** You drive over 65 miles per hour, but you do not get a speeding ticket : **$p \wedge \neg q$**
* **c)** You will get a speeding ticket if you drive over 65 miles per hour : **$p \rightarrow q$**
* **d)** If you do not drive over 65 miles per hour, then you will not get a speeding ticket : **$\neg p \rightarrow \neg q$**
* **e)** Driving over 65 miles per hour is sufficient for getting a speeding ticket : **$p \rightarrow q$**
* **f)** You get a speeding ticket, but you do not drive over 65 miles per hour : **$q \wedge \neg p$**
* **g)** Whenever you get a speeding ticket, you are driving over 65 miles per hour : **$q \rightarrow p$**

---

## Question 12: Truth Values of Biconditionals ($p \leftrightarrow q$)
*Context: Determine whether these biconditionals are true or false. A biconditional is true only when both sides share the exact same truth value.*

* **a) $2+2=4$ if and only if $1+1=2$.**
  * Both sides are True. Therefore, the statement is **True**.
* **b) $1+1=2$ if and only if $2+3=4$.**
  * Left is True, Right is False. Therefore, the statement is **False**.
* **c) $1+1=3$ if and only if monkeys can fly.**
  * Both sides are False. Therefore, the statement is logically **True**.
* **d) $0>1$ if and only if $2>1$.**
  * Left is False, Right is True. Therefore, the statement is **False**.

---

## Question 13: Truth Values of Conditionals ($p \rightarrow q$)
*Context: Determine whether each of these conditional statements is true or false. A conditional is false ONLY when the hypothesis (p) is True and the conclusion (q) is False.*

* **a) If $l+1=2$, then $2+2=5$.**
  * (Assuming typographic error 'l' means 1). Hypothesis is True, conclusion is False. Therefore, **False**.
* **b) If $1+1=3$, then $2+2=4$.**
  * Hypothesis is False, conclusion is True. Therefore, **True** (vacuously).
* **c) If $1+1=3$ then $2+2=5$.**
  * Hypothesis is False, conclusion is False. Therefore, **True** (vacuously).
* **d) If monkeys can fly, then $1+1=3$.**
  * Hypothesis is False, conclusion is False. Therefore, **True** (vacuously).

---

## Question 14: Inclusive vs. Exclusive OR
*Context: Determine whether an inclusive or, or an exclusive or, is intended and explain why.*

* **a) Coffee or tea comes with dinner.**
  * **Answer: Exclusive.** In standard restaurant contexts, a fixed meal comes with a choice of exactly one beverage, not both.
* **b) A password must have at least three digits or be at least eight characters long.**
  * **Answer: Inclusive.** A password can satisfy security requirements by simultaneously having at least three digits AND being at least eight characters long.
* **c) The prerequisite for the course is a course in number theory or a course in cryptography.**
  * **Answer: Inclusive.** A student who has taken both courses would still be permitted to take the prerequisite course.
* **d) You can pay using U.S. dollars or euros.**
  * **Answer: Exclusive.** A single purchase transaction typically requires full payment in one designated currency or the other, rather than a mix.

---

## Question 15: "If p, then q" Translations
*Context: Write each of these statements in the form "if p, then q" in English.*

* **a) It snows whenever the wind blows from the northeast.**  $\rightarrow$ If the wind blows from the northeast, then it snows.
* **b) That the Pistons win the championship implies that they beat the Lakers.**  $\rightarrow$ If the Pistons win the championship, then they beat the Lakers.
* **c) It is necessary to walk eight miles to get to the top of Long's Peak.**  $\rightarrow$ If you get to the top of Long's Peak, then you must have walked eight miles.
* **d) To get tenure as a professor, it is sufficient to be world famous.**  $\rightarrow$ If you are world famous, then you get tenure as a professor.
* **e) If you drive more than 400 miles, you will need to buy gasoline.**  $\rightarrow$ If you drive more than 400 miles, then you will need to buy gasoline.
* **f) Your guarantee is good only if you bought your CD player less than 90 days ago.**  $\rightarrow$ If your guarantee is good, then you bought your CD player less than 90 days ago.
* **g) Jan will go swimming unless the water is too cold.**  $\rightarrow$ If the water is not too cold, then Jan will go swimming.

---

## Question 16: "p if and only if q" Translations
*Context: Write each of these propositions in the form "p if and only if q" in English.*

* **a) If it is hot outside you buy an ice cream cone, and if you buy an ice cream cone it is hot outside.**  $\rightarrow$ You buy an ice cream cone if and only if it is hot outside.
* **b) For you to win the contest it is necessary and sufficient that you have the only winning ticket.**  $\rightarrow$ You win the contest if and only if you have the only winning ticket.
* **c) You get promoted only if you have connections, and you have connections only if you get promoted.**  $\rightarrow$ You get promoted if and only if you have connections.
* **d) If you watch television your mind will decay, and conversely.**  $\rightarrow$ Your mind will decay if and only if you watch television.
* **e) The trains run late on exactly those days when I take it.**  $\rightarrow$ The trains run late if and only if it is a day I take it.
