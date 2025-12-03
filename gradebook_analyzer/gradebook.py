"""
Gradebook Analyzer
By Jai Kashyap
Date: 2025-12-03
"""

import csv

# Task 3
def calculateAverage(marksDict):
    if not marksDict:
        return 0
    total = sum(marksDict.values())
    count = len(marksDict)
    return total / count

def calculateMedian(marksDict):
    if not marksDict:
        return 0
    values = sorted(marksDict.values())
    n = len(values)
    mid = n // 2
    if n % 2 == 1:
        return values[mid]
    else:
        return (values[mid - 1] + values[mid]) / 2

def findMaxScore(marksDict):
    if not marksDict:
        return None, None
    name = max(marksDict, key=marksDict.get)
    return name, marksDict[name]

def findMinScore(marksDict):
    if not marksDict:
        return None, None
    name = min(marksDict, key=marksDict.get)
    return name, marksDict[name]

# Task 4
def assignGrades(marksDict):
    grades = {}
    for name, mark in marksDict.items():
        if mark >= 90:
            grades[name] = "A"
        elif mark >= 80:
            grades[name] = "B"
        elif mark >= 70:
            grades[name] = "C"
        elif mark >= 60:
            grades[name] = "D"
        else:
            grades[name] = "F"
    return grades

def gradeDist(grades):
    dist = {"A":0, "B":0, "C":0, "D":0, "F":0}
    for g in grades.values():
        dist[g] += 1
    return dist

# Task 2a
def manualEntry():
    marksDict = {}
    print("\nManual entry (type 'done' to stop)")
    while True:
        name = input("Name: ").strip()
        if name.lower() == "done":
            break
        mark = input("Mark: ")
        try:
            marksDict[name] = float(mark)
        except:
            print("Invalid number.")
    return marksDict

# Task 2b
def loadCSV():
    marksDict = {}
    filename = input("CSV filename: ")
    try:
        with open(filename, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 2:
                    try:
                        marksDict[row[0]] = float(row[1])
                    except:
                        pass
    except:
        print("File not found.")
    return marksDict

# Task 6
def printTable(marksDict, gradesDict):
    print("\nName\t\tMarks\tGrade")
    print("------------------------------------")
    for name in marksDict:
        print(f"{name:<15}{marksDict[name]:<10}{gradesDict[name]}")
    print("------------------------------------")

# Task 1
def main():
    print("Gradebook Analyzer")
    print("------------------")
    print("1. Manual Input")
    print("2. Load CSV")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "3":
        return
    elif choice == "1":
        marksDict = manualEntry()
    elif choice == "2":
        marksDict = loadCSV()
    else:
        print("Invalid option.")
        return

    if not marksDict:
        print("No data available.")
        return

    avg = calculateAverage(marksDict)
    med = calculateMedian(marksDict)
    maxName, maxScore = findMaxScore(marksDict)
    minName, minScore = findMinScore(marksDict)

    print("\nStats:")
    print("Average:", round(avg, 2))
    print("Median:", round(med, 2))
    print("Highest:", maxName, maxScore)
    print("Lowest:", minName, minScore)

    gradesDict = assignGrades(marksDict)
    distribution = gradeDist(gradesDict)

    print("\nGrade Distribution:")
    for g, c in distribution.items():
        print(g + ":", c)

    # Task 5
    passedStudents = [name for name, score in marksDict.items() if score >= 40]
    failedStudents = [name for name, score in marksDict.items() if score < 40]

    print("\nPassed:", passedStudents)
    print("Failed:", failedStudents)

    printTable(marksDict, gradesDict)

if __name__ == "__main__":
    main()
