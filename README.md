# Workload Manager CLI

A Python command-line application that helps students track assignments, visualize deadlines, and estimate weekly study workload.

The tool stores assignments locally, calculates daily workload, highlights heavy weeks, and breaks down time spent per course to help users plan more effectively.

---

## 🚀 Features

- Add assignments with course, due date, and estimated hours  
- View assignments sorted by due date  
- Automatic priority labeling (HIGH / MEDIUM / LOW)  
- Weekly workload estimation  
- Overload warning if weekly hours exceed threshold  
- Course-wise hour breakdown  
- Persistent storage using JSON  

---

## 🧠 How It Works

1. User enters assignments with:
   - Name  
   - Course  
   - Due date  
   - Estimated hours  

2. Program:
   - Sorts assignments by deadline  
   - Calculates upcoming 7-day workload  
   - Computes average daily study time  
   - Flags heavy workload weeks  

3. Data is saved to a local `tasks.json` file.

---

## ▶️ Running the App

```bash
git clone https://github.com/amalick8/workload-manager-cli.git
cd workload-manager-cli
python main.py
