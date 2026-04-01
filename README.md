# CSP Assignment

## Overview

This assignment implements several **Constraint Satisfaction Problems (CSPs)** using Python.  
Each problem is solved using a **backtracking approach** to satisfy given constraints.

Problems included:
- Australia Map Coloring  
- Telangana Map Coloring  
- Sudoku Solver  
- Cryptarithm (SEND + MORE = MONEY)  

---

## 1. Australia Map Coloring

**Goal:** Assign colors to regions (WA, NT, Q, SA, NSW, V, T) such that adjacent regions have different colors.

**CSP Details:**
- Variables: Regions  
- Domain: {Red, Green, Blue}  
- Constraint: Neighboring regions must differ  

**Method:** Backtracking with constraint checking  

---

## 2. Telangana Map Coloring

**Goal:** Color districts so that no neighboring districts share the same color.

**CSP Details:**
- Variables: Districts  
- Domain: {Red, Green, Blue, Yellow}  
- Constraint: Adjacent districts must differ  

**Method:** Graph representation + backtracking  

---

## 3. Sudoku Solver

**Goal:** Fill a 9×9 grid following Sudoku rules.

**Constraints:**
- Unique numbers in each row  
- Unique numbers in each column  
- Unique numbers in each 3×3 box  

**Method:** Backtracking search  

---

## 4. Cryptarithm Puzzle

**Problem:**  
SEND + MORE = MONEY  

**Constraints:**
- Each letter → unique digit  
- Leading digits ≠ 0  
- Equation must be valid  

**Method:** Permutation-based search  

---

## How to Run

```bash
python australia_map_coloring.py
python telangana_map_coloring.py
python sudoku_csp.py
python cryptarithm.py