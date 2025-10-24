# Author: Faith Lamah
# Date: 10/24/2025
# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.

def Course_Info():

    course_info = {}
    another_course = 'y'
    while another_course == 'y':
        course_ID = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        course_info.update({course_ID: course_name})
        another_course = input("Would you like another course? (y/n): ")
        another_course = another_course.lower()

    subject_search(course_info)


def subject_search(course_info):
    subject = input("Enter subject name: ")
    found = False

    print("Search Results:")
    for course_ID, course_name in course_info.items():
        if subject in course_name.lower():
            print(f"{course_ID}: {course_name}")
            found = True

    if not found:
        print("No courses found with that subject.")


Course_Info()