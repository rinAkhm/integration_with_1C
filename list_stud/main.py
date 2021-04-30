from Get_students_list import Stud_list
from Get_students_grade import Stud_grade
from Manage_data import Merge_data
import json
import pandas as pd


if __name__ == '__main__':
# получаем список студентов 
    student = Stud_list('course4_bs')
    list_students = student.allstudents
    pivot = student.pivot(list_students)

# Получаем список оценок на основании list_sid
    sids = Stud_grade(7,'2020 - 2021', pivot)
    pivot = sids.format
    courses = sids.get_course

# Сопоставляем оценки с их оценками
    merge = Merge_data()
    data = merge.merge_dict(pivot, list_students, courses)





    

                





