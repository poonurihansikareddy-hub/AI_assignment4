# CSP Assignment

## Overview

This assignment implements multiple **Constraint Satisfaction Problems (CSPs)** using Python.  
All problems are solved using a **backtracking approach** to satisfy constraints.

Problems included:
- Australia Map Coloring  
- Telangana Map Coloring  
- Sudoku Solver  
- Cryptarithm (SEND + MORE = MONEY)  

---

## 1. Australia Map Coloring

**Goal:** Assign colors to regions such that adjacent regions have different colors.

**Details:**
- Variables: WA, NT, Q, SA, NSW, V, T  
- Domain: {Red, Green, Blue}  
- Constraint: Neighboring regions must have different colors  

---

## 2. Telangana Map Coloring

**Goal:** Assign colors to districts such that adjacent districts differ.

**Details:**
- Variables: Districts  
- Domain: {Red, Green, Blue, Yellow}  
- Constraint: Neighboring districts must differ  

*Note: Sample implementation is provided and can be extended to all districts.*

---

## 3. Sudoku Solver

**Goal:** Solve a 9×9 Sudoku puzzle.

**Constraints:**
- Unique values in each row  
- Unique values in each column  
- Unique values in each 3×3 grid  

---

## 4. Cryptarithm Puzzle

**Problem:**  
SEND + MORE = MONEY  

**Constraints:**
- Each letter maps to a unique digit  
- Leading digits are non-zero  
- Equation must be satisfied  

---

## How to Run

```bash
python3 australia_map_coloring.py
python3 telangana_map_coloring.py
python3 sudoku_csp.py
python3 cryptarithm.py
