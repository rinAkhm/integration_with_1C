import xlsxwriter



class Merge_data:
    def merge_dict(self, pivot, list_students, courses):
        '''doing dataframe'''
        ab = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        columns = list(ab)
        for p in ab:
            columns += [p + let for let in ab]
        # print(len(columns))

        ######################################################

        workbook = xlsxwriter.Workbook("FinalGrades.xlsx")
        # The workbook object is then used to add new
        # worksheet via the add_worksheet() method.
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'Full name')
        worksheet.write('B1', 'Group')
        worksheet.write('C1', 'Email')


        for i, course in enumerate(courses):
            worksheet.write(columns[i + 3] + '1', course['CourseName'])


        studs = sorted(list(list_students))
        for i, student in enumerate(studs):
            worksheet.write(columns[0] + str(i + 2), student[0])
            worksheet.write(columns[1] + str(i + 2), student[1])
            worksheet.write(columns[2] + str(i + 2), student[2])
            
            for j, course in enumerate(courses):
                grade = pivot[student[3]][course['CourseName']] if course['CourseName'] in pivot[student[3]] else ''
                worksheet.write(columns[j + 3] + str(i + 2), grade)
        
        ##################################################
        workbook.close()
        return 'Успешно'

