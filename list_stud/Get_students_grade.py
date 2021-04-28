import requests
from requests.auth import AuthBase
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import os
from dotenv import load_dotenv


load_dotenv()

class Stud_grade:
    def __init__ (self, semester, *args):
        self.args = args
        self.semester = semester
        self.SREVICE1 = os.getenv('SERVICE1')
        self.PASSWORD = os.getenv('PASSWORD')
        self.LOGIN = os.getenv('LOGIN')

    def format(self):
        dataframe = []
        name_dict = ''
        list_semester = ['First semester', 'Second semester', \
                                'Third semester', 'Fourth semester', \
                                'Fifth semester', 'Sixth semester', \
                                'Seventh semester','Eighth semester']


        if self.semester <= 8 and self.semester >= 1:
            for num in range(len(self.args)):
                data_letter = []
                disiplines = {}
                print(self.args[num]['sid'])
                response_from_grades = self.get_grade(self.args[num]['sid'])
                if response_from_grades == 'sorry, now server is unavailable':
                    break
                
                for name in response_from_grades:
                    name_dict = name
                
                for i in response_from_grades[f'{name_dict}']:
                    if i['ControlPeriod'] == list_semester[self.semester-1]:
                        disipline = {}           
                        disipline.setdefault('CourseName', i['CourseName'])
                        disipline.setdefault('ConrolResult', i['ConrolResult'])
                        disipline.setdefault('TeacherName', i['TeacherName'])
                        disipline.setdefault('ControlForm', i['ControlForm'])
                        data_letter.append(disipline)

                disiplines.setdefault(self.args[num]['sid'], data_letter)   
                dataframe.append(disiplines)
            print(f'полученио оценок по студентам {num+1} / {len(self.args)}')
            return dataframe
        else:
            return 'You write uncorrect semester'

    def get_grade(self, sid):
        URL = self.SREVICE1 + f'{sid}' + '&lang=ru'
        request = requests.get(url = URL ,verify = False, auth = (self.LOGIN, self.PASSWORD))
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        if request.status_code == 200:
            return request.json()
        else:
            return f'sorry, not found grade for {sid}'   