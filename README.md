# Smart Interview Preparation Engine

A desktop-based interview preparation application that helps students prepare for technical interviews through personalized DSA roadmaps, adaptive study schedules, company-specific preparation guidance, progress tracking, and analytics.

---

## Project Overview

Smart Interview Preparation Engine is a Python desktop application designed to assist students in structured interview preparation.

The system takes user input such as:

- Name
- Target company
- Daily study hours
- Weak DSA topics

Based on this input, it generates:

- Personalized DSA study roadmap
- Adaptive daily study schedule
- Recommended coding questions
- Company-specific preparation focus
- Progress tracking dashboard
- Performance analytics

---

## Features

### Personalized DSA Roadmap Generation
Creates a structured roadmap based on weak topics.

Example:

- Trees
- BST
- Tree Traversal
- Recursion
- Graphs
- BFS
- DFS
- Dijkstra

---

### Adaptive Study Schedule
Generates study plans based on available study hours.

Example:

For 3 hours/day:

- Hour 1 → Learn concepts
- Hour 2 → Solve practice problems
- Hour 3 → Revision

---

### Company-Specific Preparation Guidance
Provides focused preparation areas for different companies.

Supported companies:

- Infosys
- TCS
- Wipro
- Amazon
- Microsoft

Example for Infosys:

- Aptitude
- Arrays
- Strings
- SQL
- OOP

---

### Coding Question Recommendation Engine
Suggests coding questions based on weak DSA topics.

Examples:

- Two Sum
- Number of Islands
- Reverse Linked List
- Dijkstra Shortest Path

---

### Progress Tracking
Users can mark completed questions and track solved problems.

---

### Analytics Dashboard
Displays:

- Total solved questions
- Weak topic count
- Study hours
- Completion level
- Target company

---

### Modern Desktop UI
Built using Tkinter with a professional desktop application layout.

---

## Tech Stack

- Python
- Tkinter
- JSON
- Git
- GitHub

---

## Data Structures & Algorithms Used

### Hash Maps (Dictionary)
Used for:

- question recommendation lookup
- company recommendation mapping
- roadmap dependency mapping

---

### Lists
Used for:

- storing questions
- storing roadmap steps
- storing solved questions

---

### Graph-style Dependency Mapping
Used for topic relationship traversal.

Example:

Trees → BST → Traversal

Graphs → BFS → DFS → Dijkstra

---

### Recommendation Logic
Rule-based recommendation engine using topic matching.

---

### Scheduling Logic
Adaptive schedule generation based on study hours.

---

## Project Structure

```bash
smart-interview-prep/
│
├── main.py
├── roadmap.py
├── recommender.py
├── questions.py
├── progress.py
├── data_manager.py
│
├── data/
│   ├── user_data.json
│   └── progress.json
│
├── screenshots/
│   ├── home.png
│   ├── analytics.png
│   └── progress.png
│
└── README.md