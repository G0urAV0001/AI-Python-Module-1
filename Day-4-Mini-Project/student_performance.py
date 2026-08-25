# Student Performance Predictor

study_hours = float(input("Enter study hours per day: "))
attendance = float(input("Enter attendance percentage: "))
assignments = float(input("Enter assignment completion percentage: "))

if study_hours >= 3 and attendance >= 75 and assignments >= 75:
    print("Expected Performance: Good")
else:
    print("Expected Performance: Needs Improvement")
