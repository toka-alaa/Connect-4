## 🎮 Connect Four– Game with Ai(MinMax),(Tkinter)

## 👥 Team Members
- **Aya Ahmed Hussien Khalil Nasser**
- **Toka Nasr Saeed Reyad**
- **Toka Alaa Ebrahim Ahmed**
- **Radwa AbdElrahman Ahmed**
- **Reham Hamdy Abdelsattar**

## 🎓 Course Details
- **Course Name:** AI   
- **Professor:** Dr. Sara Sweidan
- **Instructor:** Eng. Yousef Elbaroudy   
- **Faculty:** Faculty of Computer Science and Artificial Intelligence – Benha University 
---

## 📌 Project Purpose

This project presents a complete implementation of the **Connect Four** game as part of the Artificial Intelligence course.  
The main objective is to design an interactive game that combines **game logic**, **graphical interface**, and **intelligent decision-making**.

An AI agent is implemented using the **Minimax algorithm with Alpha-Beta pruning**, enabling the computer player to make optimal and strategic moves.

---

## ✅ Functional Requirements

The game supports the following modes and features:

- Human vsHuman gameplay  
- Human vs Computer gameplay  
- Computer vs Computer gameplay  
- AI decision-making using Minimax  
- Performance optimization using Alpha-Beta pruning  
- Clear environment modeling  
- Modular and organized code structure  
- Graphical user interface (GUI)  
- Detailed documentation of logic and algorithms  

---

## 📘 Game Description

Connect Four is a two-player board game played on a **6×7 grid**.  
Players alternately drop discs into columns, and the disc occupies the lowest available position.  
The winner is the first player who forms **four connected discs** horizontally, vertically, or diagonally.

The game is developed using:
- **Python**
- **Tkinter** for the graphical interface
- **Minimax + Alpha-Beta pruning** for artificial intelligence

---

## 🧠 AI Environment Analysis (PEAS)

### **Performance Measure**
- Achieving a win  
- Preventing opponent victories  
- Maximizing strategic advantage  

### **Environment**
- A fixed 6×7 grid displayed on screen  

### **Actuators**
- Selecting a column to drop a disc  

### **Sensors**
- Current board configuration  
- Available valid moves  
- Win and draw detection  

---

## 🌍 Environment Characteristics

| Property | Description |
|--------|-------------|
| **Observability** | Fully observable |
| **Agents** | Multi-agent (competitive) |
| **Determinism** | Deterministic |
| **Task Nature** | Sequential |
| **Dynamics** | Static |
| **State Type** | Discrete |

---

## 🎨 Graphical User Interface

The game interface is designed using **Pygame** to ensure clarity and ease of interaction.

### **GUI Capabilities**
- Visual 6×7 grid layout  
- Color-coded player discs  
- Turn-based interaction  
- On-screen win notifications  
- Restart and exit options  

Additional improvements may include:
- Sound effects  
- Visual animations  
- Highlighting winning patterns  

---

## 🤖 Artificial Intelligence Design

### **Minimax Strategy**

The AI explores future game states by alternating between:
- A **maximizing agent** (computer player)
- A **minimizing agent** (human or opponent)

Each possible move is evaluated to determine the best achievable outcome.

### **Alpha-Beta Pruning**

Alpha-Beta pruning is applied to:
- Eliminate unnecessary branches  
- Speed up computation  
- Enable deeper search levels  
- Improve overall AI performance  

---

## 🧮 Evaluation Function

The evaluation function scores board states based on:
- Control of the center column  
- Potential winning connections  
- Blocking opponent threats  
- Immediate win or loss scenarios  

This approach allows the AI to behave intelligently rather than randomly.

---

## ⚙️ Core Game Logic

### **Board Representation**
- Implemented as a 6×7 matrix  

### **Winning Conditions**
The system checks for:
- Horizontal connections  
- Vertical connections  
- Ascending diagonals  
- Descending diagonals  

### **Move Validation**
- The selected column must not be full  
- Discs are placed in the lowest available cell  

---

