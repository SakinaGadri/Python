# Global variables. Feel free to play around with these
# but please return them to their original values before you submit.
# HINT: Your code should be using these values, if I change them (and I will)
# your output should change accordingly
#a0_weight = 5
a1_weight = 7
a2_weight = 8
assignment_weight = 20
term_tests_weight = 25
exam_weight = 40
exercises_weight = 10
quizzes_weight = 5

a0_max_mark = 125
a1_max_mark = 200
a2_max_mark = 140
term_tests_max_mark = 45+30
exam_max_mark = 55
exercises_max_mark = 10
quizzes_max_mark = 5
exam_pass_mark = 40
overall_pass_mark = 50


def get_max(component_name):
    '''(str) -> float
    Given the name of a course component (component_name),
    return the maximum mark for that component. This is used to allow the GUI
    to display the "out of" text beside each input field.
    REQ: component_name in {'a0', 'a1', 'a2', 'exercises', 'term tests',
    'quizzes', 'exam'}
    >>> get_max('a0')
    25
    >>> get_max('exam')
    100
    '''
    # DO NOT EDIT THIS FUNCTION. This function exists to allow the GUI access
    # to some of the global variables. You can safely ignore this function
    # for the purposes of Ex2.
    if(component_name == 'a0'):
        result = a0_max_mark
    elif(component_name == 'a1'):
        result = a1_max_mark
    elif(component_name == 'a2'):
        result = a2_max_mark
    elif(component_name == 'exercises'):
        result = exercises_max_mark
    elif(component_name == 'term tests'):
        result = term_tests_max_mark
    elif(component_name == 'quizzes'):
        result = quizzes_max_mark
    else:
        result = exam_max_mark

    return result


def percentage(raw_mark, max_mark):
    ''' (float, float) -> float
    Return the percentage mark on a piece of work that received a mark of
    raw_mark where the maximum possible mark of max_mark.
    REQ: raw_mark >=0
    REQ: max_mark > 0
    REQ: raw_max <= max_mark
    >>> percentage(15, 20)
    75.0
    >>> percentage(4.5, 4.5)
    100.0
    '''
    # calculate the percentage of the numbers entered
    result = (raw_mark/max_mark)*100
    # return the percentage
    return result


def contribution(raw_mark, max_mark, weight):
    ''' (float, float, float) -> float
    Given a piece of work where the student earned raw_mark marks out of a
    maximum of max_marks marks possible, return the number of marks it
    contributes to the final course mark if this piece of work is worth weight
    marks in the course marking scheme.
    REQ: raw_mark >=0
    REQ: max_mark > 0
    REQ: weight >= 0
    >>> contribution(13.5, 15, 10)
    9.0
    '''
    result = (raw_mark/max_mark)*weight
    return result


def term_work_mark(assign0, assign1, assign2, exercises, quizzes, term_tests):
    ''' (float, float, float, float, float, float) -> float
    Returns a float value of the term mark based on the inputs of
    assign0, assign1, assign2, exercises, quizzes, term_tests.
    REQ: 0 <= assign0
    REQ: assign0 <= a0_max_mark
    REQ: 0 <= assign1
    REQ: assign1 <= a1_max_mark
    REQ: 0 <= assign2
    REQ: assign2 <= a2_max_mark
    REQ: 0 <= exercises
    REQ: exercises <= exercises_max_mark
    REQ: 0 <= quizzes
    REQ: quizzes <= quizzes_max_mark
    REQ: 0 <= term_tests
    REQ: term_tests <= term_tests_max_mark
    >>> term_work_mark(0, 0, 0, 0, 0, 0)
    0.0
    >>> term_work_mark(20, 25, 50, 5, 3.5, 24.6)
    32.3
    >>> term_work_mark(25, 50, 100, 10, 5, 50)
    60.0
    '''
    # calculate assignment 0 mark
    mark_for_assign_0 = contribution(assign0, a0_max_mark, a0_weight)
    # calculate assignment 1 mark
    mark_for_assign_1 = contribution(assign1, a1_max_mark, a1_weight)
    # calculate assignment 2 mark
    mark_for_assign_2 = contribution(assign2, a2_max_mark, a2_weight)
    # calculate exercises mark
    mark_for_exercises = contribution(exercises, exercises_max_mark,
                                      exercises_weight)
    # calculate quizzes mark
    mark_for_quizzes = contribution(quizzes, quizzes_max_mark, quizzes_weight)
    # calculate term test mark
    mark_for_term_tests = contribution(term_tests, term_tests_max_mark,
                                       term_tests_weight)
    # add all the marks calculated by contribution
    term_mark = (mark_for_assign_0 + mark_for_assign_1 + mark_for_assign_2 +
                 mark_for_exercises + mark_for_quizzes + mark_for_term_tests)
    # display the result
    return term_mark


def final_mark(assign0, assign1, assign2, exercises, quizzes, term_tests,
               exam_mark):
    ''' (float, float, float, float, float, float, float) -> float
    Returns a float value based on the inputs of assign0, assign1, assign2,
    exercises, quizzes, term_tests, and exam_mark.
    REQ: 0 <= assign0
    REQ: assign0 <= a0_max_mark
    REQ: 0 <= assign1
    REQ: assign1 <= a1_max_mark
    REQ: 0 <= assign2
    REQ: assign2 <= a2_max_mark
    REQ: 0 <= exercises
    REQ: exercises <= exercises_max_mark
    REQ: 0 <= quizzes
    REQ: quizzes <= quizzes_max_mark
    REQ: 0 <= term_tests
    REQ: term_tests <= term_tests_max_mark
    REQ: 0 <= exam_mark
    REQ: exam_mark <= exam_max_mark
    >>> final_mark(0, 0, 0, 0, 0, 0, 0)
    0.0
    >>> final_mark(24.5, 45, 80, 8, 3.5, 25, 70)
    69.6
    >>> final_mark(25, 50, 100, 10, 5, 50, 100)
    100.0
    '''
    # add exam_mark to term_mark to get the finishing_mark
    term_grade = term_work_mark(assign0, assign1, assign2, exercises, quizzes,
                                term_tests)
    finishing_mark = term_grade + contribution(exam_mark, exam_max_mark,
                                               exam_weight)
    # return the output
    return finishing_mark


def is_pass(assign0, assign1, assign2, exercises, quizzes, term_tests,
            exam_mark):
    ''' (float, float, float, float, float, float, float) -> bool
    Returns True if exam_mark is at 40 or above and assign_0, assign_1,
    assign_2, exercises, quizzes, term_tests combined is at 50 or above.
    REQ: 0 <= assign0
    REQ: assign0 <= a0_max_mark
    REQ: 0 <= assign1
    REQ: assign1 <= a1_max_mark
    REQ: 0 <= assign2
    REQ: assign2 <= a2_max_mark
    REQ: 0 <= exercises
    REQ: exercises <= exercises_max_mark
    REQ: 0 <= quizzes
    REQ: quizzes <= quizzes_max_mark
    REQ: 0 <= term_tests
    REQ: term_tests <= term_tests_max_mark
    REQ: 0 <= exam_mark
    REQ: exam_mark <= exam_max_mark
    >>> is_pass(24, 45, 80, 8, 5, 48, 70)
    True
    >>> is_pass(10, 15, 10, 5, 2, 12, 80)
    False
    >>> is_pass(21, 41, 79, 7, 5, 45, 39)
    False
    '''
    # calculate exam_grade
    overall_grade = final_mark(assign0, assign1, assign2, exercises, quizzes,
                               term_tests, exam_mark)
    # compare it with the passing mark of each
    overall_pass = overall_grade >= overall_pass_mark
    exam_pass = exam_mark >= exam_pass_mark
    # return the result
    result = (overall_pass) and (exam_pass)
    return result
