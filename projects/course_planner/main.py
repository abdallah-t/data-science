import json

def load_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def get_all_finished_courses(data):
    finished_courses_per_trimester = data.get("finished_courses", {})
    return [course for trimester in finished_courses_per_trimester.values() for course in trimester]

def get_unlocked_courses(data, all_finished_courses):
    program_specifications = data.get("program_specifications", {})
    unlocked_courses = []

    for course, details in program_specifications.items():
        prerequisites_met = details["prerequisite"] in all_finished_courses or details["prerequisite"] == ""
        if prerequisites_met and course not in all_finished_courses:
            unlocked_courses.append(course)

    return unlocked_courses

def main():
    file_path = "./data/bcsc.json"
    data = load_data(file_path)

    all_finished_courses = get_all_finished_courses(data)
    print("All Finished Courses:", all_finished_courses)

    unlocked_courses = get_unlocked_courses(data, all_finished_courses)
    print("Unlocked Courses:", unlocked_courses)

if __name__ == "__main__":
    main()