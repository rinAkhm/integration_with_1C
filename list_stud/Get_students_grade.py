import requests
from requests.auth import AuthBase
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import os
from dotenv import load_dotenv


load_dotenv()

class Stud_grade:
    def __init__ (self, semester, year, pivot):
        self.year = year
        self.pivot = pivot
        self.semester = semester
        self.SREVICE1 = os.getenv('SERVICE1')
        self.PASSWORD = os.getenv('PASSWORD')
        self.LOGIN = os.getenv('LOGIN')

    @property
    def format(self):
        name_dict = ''
        list_semester = ['First semester', 'Second semester', \
                                'Third semester', 'Fourth semester', \
                                'Fifth semester', 'Sixth semester', \
                                'Seventh semester','Eighth semester']
        pivot = self.pivot
        if self.semester <= 8 and self.semester >= 1:
            for num, sid in enumerate(pivot):
                list_grades = self.get_grade(sid)
                if list_grades == 'sorry, now server is unavailable':
                    break

                for name in list_grades:
                    prefix = name
                
                for grade in list_grades[f'{prefix}']:
                    if grade['ControlPeriod'] == list_semester[self.semester-1] and grade['StudyYear'] == self.year:
                        pivot[sid][grade['CourseName']] = grade['ConrolResult']      

                print(f'grades received {num+1} / {len(pivot)}') 
            list_grades.clear()
            return pivot
        else:
            return 'You write uncorrect semester'

    def get_grade(self, sid):
        '''Func get grade '''
        URL = self.SREVICE1 + f'{sid}' + '&lang=eng'
        request = requests.get(url = URL ,verify = False, auth = (self.LOGIN, self.PASSWORD))
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        if request.status_code == 200:
            return request.json()
        else:
            return f'sorry, not found grade for {sid}'
    
    @property
    def get_course(self):
        pivot = self.pivot 
        course_list = []

        for i in pivot:
            for keys in pivot[i]: 
                disipline = {}
                disipline['CourseName'] = keys
                course_list.append(disipline)

        result = list({d['CourseName']: d for d in course_list}.values())
        return result


    