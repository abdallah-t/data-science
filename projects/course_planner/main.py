import json

with open ("./data/bcsc.json", "r") as f:
    data = json.load(f)

done_courses = [["CSCI617", "ENGL611", "ARAB600", "EUTH500", "MATH631", "CHEM611"], ["CSCI626", "CSCI627", "MATH711", "MATH622", "ENGL621", "PHYS631"]]
done_courses = done_courses[0] + done_courses[1]

available_courses = []


for course in data:
    if data[course]["prerequisite"] in done_courses or data[course]["prerequisite"] == "":
        available_courses.append(course)
    
available_courses = set(available_courses) - set(done_courses)


print(available_courses)
# remove done_courses from available_courses
