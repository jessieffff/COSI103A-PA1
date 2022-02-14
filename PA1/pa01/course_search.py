'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
'''

from schedule import Schedule
import sys

schedule = Schedule()
schedule.load_courses()
schedule = schedule.enrolled(range(5,1000)) # eliminate courses with no students

TOP_LEVEL_MENU = '''
quit
reset
term  (filter by term)
course (filter by coursenum, e.g. COSI 103a)
instructor (filter by instructor)
subject (filter by subject, e.g. COSI, or LALS)
title  (filter by phrase in title)
description (filter by phrase in description)
timeofday (filter by day and time, e.g. meets at 11 on Wed)
'''

terms = {c['term'] for c in schedule.courses}

def topmenu():
    '''
    topmenu is the top level loop of the course search app
    '''
    global schedule
    while True:
        command = input(">> (h for help) ")
        if command=='quit':
            return
        elif command in ['h','help']:
            print(TOP_LEVEL_MENU)
            print('-'*40+'\n\n')
            continue
        elif command in ['r','reset']:
            schedule.load_courses()
            schedule = schedule.enrolled(range(5,1000))
            continue
        elif command in ['t', 'term']:
            term = input("enter a term:"+str(terms)+":")
            schedule = schedule.term([term]).sort('subject')
        elif command in ['s','subject']:
            subject = input("enter a subject:")
            schedule = schedule.subject([subject])

        #author: Jiefang Li
        #not sure if this is correct ):
        elif command in ['ti', 'title'] :
            phrase = input("enter a phrase:")
            schedule = schedule.title(phrase)
        #author: Jiefang Li
        #filter by course status (either open or closed)
        elif command in ['sta','status']:
             status = input("enter a phrase(Open/Closed): ")
             schedule = schedule.status_text([status])
<<<<<<< HEAD
        #author Yiwen
        elif command in ['d', 'description']:
            phrase = input("enter a phrase(Open/Closed): ")
            schedule = schedule.description(phrase)
        #author Yiwen
        # filter by last name of the instructor:
        elif command in ['ln', 'lastname']:
            lastname = input("enter last name of instructor: ")
            schedule = schedule.lastname(name)
=======

        #author: Huijie
        #filter by course subject and number(in the form of 'COSI 103A')
        elif command in ['c', 'course']:
            course = input("enter a course number(in the form of 'COSI 103A'):")
            ans = number.split(' ')
            subject = ans[0]
            coursenum = ans[1]
            schedule = schedule.subject([subject])
            schedule = schedule.coursenum([coursenum])



>>>>>>> c28a25aae6aa2574db25d2c8d8e2cf464c246016
        else:
            print('command',command,'is not supported')
            continue

        print("courses has",len(schedule.courses),'elements',end="\n\n")
        print('here are the first 10')
        for course in schedule.courses[:10]:
            print_course(course)
        print('\n'*3)

def print_course(course):
    '''
    print_course prints a brief description of the course
    '''
    print(course['subject'],course['coursenum'],course['section'],
          course['name'],course['term'],course['instructor'])

if __name__ == '__main__':
    topmenu()
