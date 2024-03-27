#!/usr/bin/env python3

def calculate_average_score(student):
    # Calculate the average score for a student
    scores = student.get("scores", [])
    total_score = 0
    count = 0

    for score in scores:
        if score["type"] == "homework":
            total_score += score["score"]
            count += 1

    average_score = total_score / count if count > 0 else 0
    return average_score

def top_students(mongo_collection):
    # Fetch data from the MongoDB collection
    students = mongo_collection.find()

    # Calculate the average score for each student and add it to the student data
    students_with_average = []

    for student in students:
        average_score = calculate_average_score(student)
        student["averageScore"] = average_score
        students_with_average.append(student)

    # Sort the students by average score in descending order
    sorted_students = sorted(students_with_average, key=lambda x: x["averageScore"], reverse=True)

    return sorted_students
