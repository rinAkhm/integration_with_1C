import requests
from requests.auth import AuthBase
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import os
from dotenv import load_dotenv


load_dotenv()

class Stud_list:
    def __init__ (self, param):
        self.param = param
        self.SREVICE2 = os.getenv('SERVICE2')
        self.PASSWORD = os.getenv('PASSWORD')
        self.LOGIN = os.getenv('LOGIN')

    @property
    def format_post(self):
        if self.param == 'course1_bs':
            students = self.get_list_students('course=1&degree=bachelor&status=студент')
            return students
        elif self.param == 'course2_bs':
            students = self.get_list_students('course=2&degree=bachelor&status=студент')
            return students
        elif self.param == 'course3_bs':
            students = self.get_list_students('course=3&degree=bachelor&status=студент')
            return students
        elif self.param == 'course4_bs':
            students = self.get_list_students('course=4&degree=bachelor&status=студент')
            return students
        elif self.param == 'course1_ms':
            students = self.get_list_students('course=1&degree=magister&status=студент')
            return students
        elif self.param == 'course2_ms':
            students = self.get_list_students('course=2&degree=magister&status=студент')
            return students


    def get_list_students(self, token):
        '''can get lisy of students'''
        URL = self.SREVICE2
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        request = requests.post(url = URL, auth = (self.LOGIN, self.PASSWORD), verify = False, data = token.encode('utf-8'))
        if request.status_code == 200:
            return request.json()
        else:
            return 'sorry, now server is unavailable'

    @property
    def allstudents(self):
        '''create new dict and send to main file'''
        list_person = set()
        amount_stud  = len(self.format_post[''][1]['collection'])
        for num, stud_id in enumerate(self.format_post[''][1]['collection']):
            list_person.add((stud_id['fullName'], stud_id['group'], stud_id['email'], stud_id['guid']))      
            print("sid - " + f"{stud_id['guid']}")
        print(f'list of students {len(list_person)}')
        return list_person


    def pivot(self, list_person):
        '''create pivot list'''
        pivot = {}
        for num, line in enumerate(list_person):
            if line[3] not in pivot:
                pivot[line[3]] = {}
        return pivot





    