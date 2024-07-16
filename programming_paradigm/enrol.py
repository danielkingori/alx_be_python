
from classes import *

def new_enrolment(student, course):
    return student.enrol(course)

#abstratction , not seing the logic
enroll = new_enrolment(Ungrad, "Spanish")
enroll = new_enrolment(Ungrad, "G")