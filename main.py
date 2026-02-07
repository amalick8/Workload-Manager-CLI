import json
from datetime import datetime, timedelta
from pathlib import Path

DATA_FILE = Path("tasks.json")

class Task:
    def __init__(self, name, course, due_date, hours):
        self.name = name
        self.course = course
        self.due_date = due_date
        self.hours = float(hours)

    def to_dict(self):
        return {
            "name": self.name,
            "course": self.course,
            "due_date": self.due_date,
            "hours": self.hours
        }

class WorkloadManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, name, course, due_date, hours):
        self.tasks.append(Task(name, course, due_date, hours))
        self.save_tasks()

    def sorted_tasks(self):
        return sorted(
            self.tasks,
            key=lambda t: datetime.strptime(t.due_date, "%Y-%m-%d")
        )

    def upcoming_week_tasks(self):
        today = datetime.now()
        week = today + timedelta(days=7)
        return [
            t for t in self.tasks
            if today <= datetime.strptime(t.due_date, "%Y-%m-%d") <= week
        ]

    def daily_workload(self):
        return sum(t.hours for t in self.upcoming_week_tasks()) / 7

    def overload_detected(self):
        return sum(t.hours for t in self.upcoming_week_tasks()) > 40

    def course_breakdown(self):
        result = {}
        for t in self.tasks:
            result.setdefault(t.course, 0)
            result[t.course] += t.hours
        return result

    def priority(self, task):
        days_left = (
            datetime.strptime(task.due_date, "%Y-%m-%d") - datetime.now()
        ).days
        if days_left <= 2:
            return "HIGH"
        if days_left <= 5:
            return "MEDIUM"
        return "LOW"

    def save_tasks(self):
        with open(DATA_FILE, "w") as f:
            json.dump([t.to_dict() for t in self.tasks], f)

    def load_tasks(self):
        if DATA_FILE.exists():
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.tasks = [Task(**item) for item in data]

def menu():
    print("\n1. Add Assignment")
    print("2. View Timeline")
    print("3. Weekly Workload")
    print("4. Course Breakdown")
    print("5. Exit")

def main():
    manager = WorkloadManager()

    while True:
        menu()
        choice = input("Choose option: ").strip()

        if choice == "1":
            name = input("Assignment name: ")
            course = input("Course: ")
            due = input("Due date (YYYY-MM-DD): ")
            hours = input("Estimated hours: ")
            manager.add_task(name, course, due, hours)
            print("Task added.")

        elif choice == "2":
            for t in manager.sorted_tasks():
                p = manager.priority(t)
                print(f"{t.due_date} | {p} | {t.course} | {t.name} | {t.hours} hrs")

        elif choice == "3":
            daily = manager.daily_workload()
            print(f"Estimated Daily Workload: {daily:.2f} hrs")
            if manager.overload_detected():
                print("Warning: Heavy workload detected.")

        elif choice == "4":
            breakdown = manager.course_breakdown()
            for c, h in breakdown.items():
                print(f"{c}: {h:.2f} hrs")

        elif choice == "5":
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
