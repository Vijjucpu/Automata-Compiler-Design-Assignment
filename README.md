# Automata-Compiler-Design-Assignment

## DFA, NFA and Automata Conversion Using Python

**Name:** G. Vijayalaxmi  
**Course:** B.Tech 3rd Year  
**Branch:** Artificial Intelligence and Data Science  
**Roll No:** 25075A7202  
**Subject:** Automata Compiler Design (ACD)


## Problem Statement

Construct automata over the alphabet **{0, 1}** that accepts all strings containing **01 OR 11 as a substring**.

The same problem statement is used to construct both the DFA and NFA and to demonstrate the required automata conversions.


## Objectives

- Construct a DFA for the given problem statement.
- Construct an NFA for the same problem statement.
- Include an **epsilon (ε) transition**.
- Convert NFA to an equivalent DFA.
- Convert DFA to an equivalent NFA.
- Generate clear visual block diagrams using Python.
- Generate state mappings for the conversion programs.


## Technologies Used

- **Python 3**
- **Matplotlib**
- **Visual Studio Code**
- **Git**
- **GitHub**

---

## Project Structure

```text
Automata-Compiler-Design-Assignment/
│
├── DFA/
│   └── dfa.py
│
├── NFA/
│   └── nfa.py
│
├── NFA to DFA/
│   └── nfa_to_dfa.py
│
├── DFA to NFA/
│   └── dfa_to_nfa.py
│
└── ACD_Explanation_Video.mp4


# 1. DFA Construction

The first program constructs a **Deterministic Finite Automaton (DFA)** for the given problem statement.

The program defines:

* States
* Input alphabet
* Start state
* Final state
* Transition function

The transition function specifies one next state for every state and input symbol.

The program displays the DFA transition table and generates a visual block diagram using Matplotlib.

### DFA Code Logic


```text

States
   ↓
Alphabet
   ↓
Start and Final States
   ↓
Transitions
   ↓
Transition Table
   ↓
DFA Diagram
```

---

# 2. NFA Construction

The second program constructs a **Nondeterministic Finite Automaton (NFA)** using the same problem statement.

NFA transitions are represented using sets because an NFA can have multiple possible destination states.

The program also demonstrates an **epsilon (ε) transition**.

An epsilon transition allows the automaton to move from one state to another without consuming an input symbol.

### NFA Code Logic

```text
States
   ↓
Alphabet
   ↓
NFA Transitions
   ↓
Epsilon Transition
   ↓
Transition Table
   ↓
NFA Diagram
```

---

# 3. NFA to DFA Conversion

The third program converts the NFA into an equivalent DFA.

The conversion uses the **subset construction method** along with **epsilon closure**.

### Conversion Steps

1. Define the NFA states and transitions.
2. Calculate the epsilon closure.
3. Perform the move operation for input `0`.
4. Perform the move operation for input `1`.
5. Calculate epsilon closure for the resulting states.
6. Treat each set of NFA states as one DFA state.
7. Generate transitions for the new DFA states.
8. Identify the DFA final states.
9. Generate the state mapping.
10. Create the final DFA diagram.

### NFA to DFA Flow

```text
NFA
 ↓
Epsilon Closure
 ↓
Move Operation
 ↓
Epsilon Closure
 ↓
DFA States
 ↓
DFA Transitions
 ↓
Final States
 ↓
State Mapping
 ↓
DFA Diagram
```

### State Mapping

The state mapping shows which NFA states are represented by each generated DFA state.

This helps to understand how the NFA states are grouped during the conversion.

---

# 4. DFA to NFA Conversion

The fourth program converts the DFA into an equivalent NFA representation.

A DFA can be represented as an NFA because every DFA transition is also a valid NFA transition.

The DFA transitions are copied into the NFA transition structure, with destination states represented using sets.

A new state `F` is introduced to demonstrate an epsilon transition.

The epsilon transition is:

```text
D ── ε ──> F
```

The new state `F` is selected as the final state.

### DFA to NFA Flow

```text
DFA
 ↓
Copy DFA Transitions
 ↓
NFA Set Representation
 ↓
Add New State F
 ↓
Add Epsilon Transition
 ↓
State Mapping
 ↓
NFA Diagram
```

---

# Epsilon Transition

This project demonstrates the use of an epsilon transition.

```text
D ── ε ──> F
```

Here, **ε** represents an empty-string transition.

The automaton can move from `D` to `F` without consuming an input symbol.

---

# Visual Diagrams

The programs use **Matplotlib** to generate visual block diagrams.

The diagrams contain:

* Start state
* Normal states
* Final states
* Transition arrows
* Loops
* Input labels
* Epsilon transitions

Final states are represented using double circles.

---

# Installation

Make sure Python 3 is installed.

Check the Python version:

```bash
python --version
```

Install Matplotlib:

```bash
pip install matplotlib
```

---

# How to Run

## DFA

```bash
cd "DFA"
python dfa.py
```

## NFA

```bash
cd "NFA"
python nfa.py
```

## NFA to DFA

```bash
cd "NFA to DFA"
python nfa_to_dfa.py
```

## DFA to NFA

```bash
cd "DFA to NFA"
python dfa_to_nfa.py
```

---

# Expected Output

The project generates:

* DFA transition table
* DFA block diagram
* NFA transition table
* NFA block diagram
* NFA to DFA state mapping
* NFA to DFA block diagram
* DFA to NFA state mapping
* DFA to NFA block diagram

---

# Code Logic Summary

### DFA

```text
Define States
→ Define Alphabet
→ Define Transitions
→ Display Table
→ Generate Diagram
```

### NFA

```text
Define States
→ Define Transitions Using Sets
→ Add Epsilon Transition
→ Display Table
→ Generate Diagram
```

### NFA to DFA

```text
Epsilon Closure
→ Move Operation
→ Create DFA State
→ Repeat Until Complete
→ Identify Final States
→ State Mapping
→ Generate Diagram
```

### DFA to NFA

```text
Define DFA
→ Copy Transitions
→ Use NFA Set Representation
→ Add New State
→ Add Epsilon Transition
→ State Mapping
→ Generate Diagram
```

---

# Learning Outcomes

Through this assignment, I learned:

* DFA construction
* NFA construction
* Epsilon transitions
* Epsilon closure
* Subset construction
* NFA to DFA conversion
* DFA to NFA conversion
* State mapping
* Automata visualization using Python
* Using Matplotlib for block diagrams
* Managing a project using Git and GitHub

---
## 🎥 Explanation Video

This video explains the code logic, execution, and output of all four programs:

1. DFA Construction
2. NFA Construction
3. NFA to DFA Conversion
4. DFA to NFA Conversion

### ⬇️ Download the Explanation Video

[🎬 Click here to download the 15-minute Explanation Video](https://github.com/Vijjucpu/Automata-Compiler-Design-Assignment/raw/refs/heads/main/explanation-video.mp4)

---

# Conclusion

This project demonstrates the practical implementation of finite automata using Python.

The same problem statement is used to construct both DFA and NFA and to demonstrate NFA to DFA and DFA to NFA conversions.

The project also includes epsilon transitions, state mappings and visual block diagrams.

This assignment helped me understand how automata concepts can be implemented practically using Python.

---

## Author

**G.Vijayalaxmi**

**B.Tech 3rd Year – Artificial Intelligence and Data Science**

**Roll No: 25075A7202**

**Subject: Automata Compiler Design (ACD)**

```
```
