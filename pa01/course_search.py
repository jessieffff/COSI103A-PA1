'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
'''

from schedule import Schedule

schedule = Schedule()
schedule.load_courses()
# eliminate courses with no students
schedule = schedule.enrolled(range(5, 1000))

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
        if command == 'quit':
            return
        elif command in ['h', 'help']:
            print(TOP_LEVEL_MENU)
            print('-'*40+'\n\n')
            continue
        elif command in ['r', 'reset']:
            schedule.load_courses()
            schedule = schedule.enrolled(range(5, 1000))
            continue
        elif command in ['t', 'term']:
            term = input("enter a term:"+str(terms)+":")
            schedule = schedule.term([term]).sort('subject')
        elif command in ['s', 'subject']:
            subject = input("enter a subject:")
<<<<<<< HEAD
            schedule = schedule.subject([subject]) 
        #author: Qing Liu
        #enter an instructor
        elif command in ['i','instructor']:
            instructor = input("enter a instructor lastname or email:")
            if "edu" in instructor:
                schedule = schedule.email([instructor]) 
            else:
                schedule = schedule.lastname([instructor]) 
        #author: Qing Liu
        #enter a starting time
        elif command in ['startingTime']:
            startingTime = int(input("enter a minimum starting time:"))
            schedule = schedule.starting_time_greater_than([startingTime]) 
        #author: Jiefang Li
        elif command in ['ti', 'title'] :
            phrase = input("enter a phrase:")
            schedule = schedule.title(phrase)
        #author: Jiefang Li
        #filter by course status (either open or closed)
        elif command in ['sta','status']:
            status = input("enter a phrase(Open/Closed): ")
            schedule = schedule.status_text(status)
        #author Yiwen
=======
            schedule = schedule.subject([subject])
        # author: Qing Liu
        # enter an instructor
        elif command in ['i', 'instructor']:
            instructor = input("enter a instructor:")
            schedule = schedule.instructor([instructor])
        # author: Qing Liu
        # enter a starting time
        elif command in ['startingTime']:
            startingTime = int(input("enter a minimum starting time:"))
            schedule = schedule.starting_time_greater_than([startingTime])
        # author: Jiefang Li
        # not sure if this is correct ):
        elif command in ['ti', 'title']:
            phrase = input("enter a phrase:")
            schedule = schedule.title(phrase)
        # author: Jiefang Li
        # filter by course status (either open or closed)
        elif command in ['sta', 'status']:
            status = input("enter a phrase(Open/Closed): ")
            schedule = schedule.status_text([status])
        # author Yiwen
>>>>>>> 6c4588fa2464a6bc0140baba7fd0de7482655719
        elif command in ['d', 'description']:
            phrase = input("enter a phrase about the course description: ")
            schedule = schedule.description(phrase)
<<<<<<< HEAD
        #auothor Yiwen
        elif command in ['f', 'firstname']:
            instructor = input("enter a first name of instructor: ")
            schedule = schedule.firstname([instructor])
=======
        # author Yiwen
        # filter by last name of the instructor:
        elif command in ['ln', 'lastname']:
            lastname = input("enter last name of instructor: ")
            schedule = schedule.lastname(name)

>>>>>>> 6c4588fa2464a6bc0140baba7fd0de7482655719
        #author: Huijie
        # filter by course subject and number(in the form of 'COSI 103A')
        elif command in ['c', 'course']:
<<<<<<< HEAD
            course = input("enter a course number(in the form of 'COSI 103A'):")
            ans = course.split(' ')
=======
            course = input(
                "enter a course number(in the form of 'COSI 103A'):")
            ans = number.split(' ')
>>>>>>> 6c4588fa2464a6bc0140baba7fd0de7482655719
            subject = ans[0]
            coursenum = ans[1]
            schedule = schedule.subject([subject])
            schedule = schedule.coursenum([coursenum])

        #author: Huijie
        # filter by course instruction day
        elif command in ['day']:
            days = input(
                "enter a string of weekdays(e.g. 'mw' -> Monday and Wednesday): ")
            daylist = [char for char in days]
            schedule = schedule.day(daylist)

        else:
            print('command', command, 'is not supported')
            continue

        print("courses has", len(schedule.courses), 'elements', end="\n\n")
        print('here are the first 10')
        for course in schedule.courses[:10]:
            print_course(course)
        print('\n'*3)


def print_course(course):
    '''
    print_course prints a brief description of the course
    '''
    print(course['subject'], course['coursenum'], course['section'],
          course['name'], course['term'], course['instructor'])


if __name__ == '__main__':
    topmenu()
