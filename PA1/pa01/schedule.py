'''
schedule maintains a list of courses with features for operating on that list
by filtering, mapping, printing, etc.
'''

import json

class Schedule():
    '''
    Schedule represent a list of Brandeis classes with operations for filtering
    '''
    def __init__(self,courses=()):
        ''' courses is a tuple of the courses being offered '''
        self.courses = courses

    def load_courses(self):
        ''' load_courses reads the course data from the courses.json file'''
        print('getting archived regdata from file')
        with open("courses20-21.json","r",encoding='utf-8') as jsonfile:
            courses = json.load(jsonfile)
        for course in courses:
            course['instructor'] = tuple(course['instructor'])
            course['coinstructors'] = [tuple(f) for f in course['coinstructors']]
        self.courses = tuple(courses)  # making it a tuple means it is immutable

    def lastname(self,names):
        ''' lastname returns the courses by a particular instructor last name'''
        return Schedule([course for course in self.courses if course['instructor'][1] in names])

    def email(self,emails):
        ''' email returns the courses by a particular instructor email'''
        return Schedule([course for course in self.courses if course['instructor'][2] in emails])

    def term(self,terms):
        ''' email returns the courses in a list of term'''
        return Schedule([course for course in self.courses if course['term'] in terms])

    def enrolled(self,vals):
        ''' enrolled filters for enrollment numbers in the list of vals'''
        return Schedule([course for course in self.courses if course['enrolled'] in vals])

    def subject(self,subjects):
        ''' subject filters the courses by subject '''
        return Schedule([course for course in self.courses if course['subject'] in subjects])

    def sort(self,field):
        if field=='subject':
            return Schedule(sorted(self.courses, key= lambda course: course['subject']))
        else:
            print("can't sort by "+str(field)+" yet")
            return self
        
    #author: Jiefang Li
    def description(self, phrase):
        if phrase in self.descriptiion:
            return self
 
    #author: Qing Liu
    def instructor(self, lastNameOrEmails):
        # First try last name
        schedule = self.lastname(lastNameOrEmails)
        if len(schedule.courses) > 0:
            return schedule
        
        # Second try email
        schedule = self.email(lastNameOrEmails)
        return schedule

    #author: Qing Liu
    def coursenum(self, coursenums):
        schedule = self.coursenums(coursenums)
        return schedule
    
    #author: Qing Liu
    def coursenums(self,coursenums):
        ''' email returns the courses by a particular course number'''
        return Schedule([course for course in self.courses if course['coursenum'] in coursenums])
