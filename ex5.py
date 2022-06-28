import json
import os



def names_of_registered_students(input_json_path, course_name):
    """
    This function returns a list of the names of the students who registered for
    the course with the name "course_name".

    :param input_json_path: Path of the students database json file.
    :param course_name: The name of the course.
    :return: List of the names of the students.
    """

    with open(input_json_path, 'r') as input_file:
        loaded_students = json.load(input_file)

    required_students = []

    for student_info in loaded_students.values():
        tmp_courses = student_info["registered_courses"]
        for course in tmp_courses:
            if course == course_name:
                student_name = student_info["student_name"]
                required_students.append(student_name)
    return required_students
    pass

def enrollment_numbers(input_json_path, output_file_path):
    """
    This function writes all the course names and the number of enrolled
    student in ascending order to the output file in the given path.

    :param input_json_path: Path of the students database json file.
    :param output_file_path: Path of the output text file.
    """

    out = open(output_file_path, 'w')

    required_courses = {}

    with open(input_json_path, 'r') as input_file:
        loaded_students = json.load(input_file)

    for student_info in loaded_students.values():
        tmp_courses = student_info["registered_courses"]
        for course in tmp_courses:
            if course in required_courses:
                required_courses[course] += 1
            else:
                required_courses[course] = 1

    for name, counter in sorted(required_courses.items()):
        out.write('"')
        out.write(name)
        out.write('"')
        out.write(' ')
        out.write(str(counter))
        out.write('\n')

    out.close()
    pass

def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """

    lecturers = {}

    files = os.listdir(json_directory_path)

    #opening files in directory
    for file in files:
        split_path = os.path.splitext(file)
        suffix = split_path[1]

        #check if file is json type
        if suffix == ".json" :
            with open(file, 'r') as input_file:
                loaded_courses = json.load(input_file)

            #The dict of the course number
            for details in loaded_courses.values():

                course_lecturers = details["lecturers"]

                #lecturers in each course
                for lecturer in course_lecturers:
                    if not (lecturer in lecturers):
                       lecturers[lecturer] = [details["course_name"]]
                    else:
                        if not details["course_name"] in lecturers[lecturer]:
                            lecturers[lecturer].append(details["course_name"])

    with open (output_json_path, 'w') as out_file:
        json.dump(lecturers, out_file)

    pass



