from Get_students_list import Stud_list
from Get_students_grade import Stud_grade
import json



if __name__ == '__main__':
    # print("Please input number course and name degree: \nexample: course3_bs")
    request = Stud_list('course4_bs')
    list_sid = request.filling()
    # print("Now input number of semester:\n")
    
    x = Stud_grade(4, *list_sid )



    with open('test.txt', 'w', encoding='utf-8') as file:
        lines = x.format()
        for i, line  in enumerate(lines):
            file.write(str(line) + '\n')
            if i > len(lines):
                print('successful')
                break



    # with open('test.txt', 'r', encoding='utf-8') as file:
    #     with open('text2.txt', 'w', encoding='utf-8') as new_file:
    #         for line in file:
    #             lines = file.readline().replace("\'", "\"")
    #             lines = json.loads(lines.strip('\n'))

                





