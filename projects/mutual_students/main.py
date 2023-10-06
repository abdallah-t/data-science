from bs4 import BeautifulSoup
import pprint

pp = pprint.PrettyPrinter(indent=4)

with open("./data/arab600.html") as f:
    arab600_html = f.read()

with open("./data/engl611.html") as f:
    engl611_html = f.read()

with open("./data/math631.html") as f:
    math631_html = f.read()

with open("./data/chem611.html") as f:
    chem611_html = f.read()

with open("./data/csci617.html") as f:
    csci617_html = f.read()

arabic_soup = BeautifulSoup(arab600_html, "html.parser")
english_soup = BeautifulSoup(engl611_html, "html.parser")
math_soup = BeautifulSoup(math631_html, "html.parser")
chem_soup = BeautifulSoup(chem611_html, "html.parser")
computing_soup = BeautifulSoup(csci617_html, "html.parser")

arabic_doctor = "Zainab Tarada"
arabic_students = arabic_soup.find_all("a")
arabic_students = [" ".join(student.text.title().strip().replace("\n", "").split()) for student in arabic_students]
arabic_students.remove(arabic_doctor)

english_doctor = "Husain Ebrahim"
english_students = english_soup.find_all("a")
english_students = [" ".join(student.text.title().strip().replace("\n", "").split()) for student in english_students]
english_students.remove(english_doctor)

math_doctor = "Lina Sobrepena Calucag"
math_students = math_soup.find_all("a")
math_students = [" ".join(student.text.title().strip().replace("\n", "").split()) for student in math_students]
math_students.remove(math_doctor)


chem_students = chem_soup.find_all("a")
chem_students = [" ".join(student.text.title().strip().replace("\n", "").split()) for student in chem_students]

computing_doctor = "Fayzeh Abdulkareem Jaber"
computing_students = computing_soup.find_all("a")
computing_students = [" ".join(student.text.title().strip().replace("\n", "").split()) for student in computing_students]
computing_students.remove(computing_doctor)

all_students = arabic_students + english_students + math_students + chem_students + computing_students
all_students = list(set(all_students))
all_students.sort()


mutual_students = {}

for student in all_students:
    mutual_classes = []
    if student in arabic_students:
        mutual_classes.append("Arabic")
    if student in english_students:
        mutual_classes.append("English")
    if student in math_students:
        mutual_classes.append("Math")
    if student in chem_students:
        mutual_classes.append("Chemistry")
    if student in computing_students:
        mutual_classes.append("Computing")
    
    mutual_students[student] = mutual_classes
# sort by number of mutual classes

sorted_mutual_students = sorted(mutual_students.items(), key=lambda x: len(x[1]), reverse=True)


arabic_and_math = [student for student in sorted_mutual_students if "Arabic" in student[1] and "Math" in student[1]]

math_arabic_computing_notchem = [student for student in sorted_mutual_students if "Arabic" in student[1] and "Math" in student[1] and "Computing" in student[1] and "Chemistry" not in student[1]]
pp.pprint(sorted_mutual_students)