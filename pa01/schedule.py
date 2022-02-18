'''
schedule maintains a list of courses with features for operating on that list
by filtering, mapping, printing, etc.
'''

import json


class Schedule():
    '''
    Schedule represent a list of Brandeis classes with operations for filtering
    '''

    def __init__(self, courses=()):
        ''' courses is a tuple of the courses being offered '''
        self.courses = courses

    def load_courses(self):
        ''' load_courses reads the course data from the courses.json file'''
        print('getting archived regdata from file')
        with open("courses20-21.json", "r", encoding='utf-8') as jsonfile:
            courses = json.load(jsonfile)
        for course in courses:
            course['instructor'] = tuple(course['instructor'])
            course['coinstructors'] = [tuple(f)
                                       for f in course['coinstructors']]
        # making it a tuple means it is immutable
        self.courses = tuple(courses)

    def lastname(self, names):
        ''' lastname returns the courses by a particular instructor last name'''
        return Schedule([course for course in self.courses if course['instructor'][1] in names])

    def email(self, emails):
        ''' email returns the courses by a particular instructor email'''
        return Schedule([course for course in self.courses if course['instructor'][2] in emails])

    def term(self, terms):
        ''' email returns the courses in a list of term'''
        return Schedule([course for course in self.courses if course['term'] in terms])

    def enrolled(self, vals):
        ''' enrolled filters for enrollment numbers in the list of vals'''
        return Schedule([course for course in self.courses if course['enrolled'] in vals])

    def subject(self, subjects):
        ''' subject filters the courses by subject '''
        return Schedule([course for course in self.courses if course['subject'] in subjects])


    def sort(self,field):
        '''sort course by keywords'''
        if field=='subject':
            return Schedule(sorted(self.courses, key= lambda course: course['name']))
        print("can't sort by "+str(field)+" yet")
        return self

    def sort(self, field):

        if field == 'subject':
            return Schedule(sorted(self.courses, key=lambda course: course['name']))


        print("can't sort by "+str(field)+" yet")
        return self

    # author: Jiefang Li
    def description(self, phrase):

        '''description filter for key phrase in course description'''
        return Schedule([course for course in self.courses if phrase in course['description']])

     #author: Jiefang Li
    def status_text(self, phrase):
        '''course status filter for open or clsoed course'''
        return Schedule([course for course in self.courses if phrase in course['status_text']])


        if phrase in self.description:
            return Schedule([course for course in self.courses if phrase in course['description']])


    # author: Yiwen Luo
    def title(self, phrase):
        '''course title filter for key phrase in course title'''
        return Schedule([course for course in self.courses if phrase in course['name']])

    # author: Yiwen
    def capacity_less_than(self, capacity):

        '''classes that are currently full or only has capacity of less or equal to n'''
        return Schedule([course for course in self.courses if course['enrolled'] >= course['limit'] - capacity])
    # author: Yiwen
    def firstname(self,names):
        ''' firstname returns the courses by a particular instructor first name'''
        return Schedule([course for course in self.courses if course['instructor'][0] in names])

        return Schedule([course for course in self.courses if course['enrolled'] >= course['limit'] - capture])


    # author: Huijie

    def day(self, weekday):
        '''day filters the courses containing the specific instruction days. weekday should be in format of ['m', 'w', ...] '''

        return Schedule([course for course in self.courses if len(course['times'])!=0 and all(x in course['times'][0].get('days') for x in weekday)])

    # author: Huijie

        return Schedule([course for course in self.courses if len(course['times']) != 0 and all(x in course['times'][0].get('days') for x in weekday)])

    # author: Huijie Liu

    def coursenum(self, coursenumber):
        ''' coursenum filters the courses by coursenum '''

        return Schedule([course for course in self.courses if course['coursenum'] in coursenumber])


    # author: Qing Liu
    def starting_time_greater_than(self, starting_times):
        ''' classes that have a starting time greater than a given starting time '''
        return Schedule([course for course in self.courses for starting_time in starting_times if len(course['times'])!=0 and course['times'][0].get('start') >= starting_time])
    


    # author: Qing Liu

    def instructor(self, lastNameOrEmails):
        # First try last name
        schedule = self.lastname(lastNameOrEmails)
        if len(schedule.courses) > 0:
            return schedule

        # Second try email
        schedule = self.email(lastNameOrEmails)
        return schedule

    # author: Qing Liu
    # classes that have a starting time greater than a given starting time
    def starting_time_greater_than(self, startingTimes):
        return Schedule([course for course in self.courses for startingTime in startingTimes if len(course['times']) != 0 and course['times'][0].get('start') >= startingTime])

