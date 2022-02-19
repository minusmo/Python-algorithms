def solution(answers):
    scored_highest = []
    scored_highest = get_scored_highest(answers)
    return scored_highest

def get_scored_highest(answers):
    scores = [-1] * 4
    highest_students = []
    
    first_student_score = check_answers(1, answers)
    second_student_score = check_answers(2, answers)
    third_student_score = check_answers(3, answers)
    
    scores[1] = first_student_score
    scores[2] = second_student_score
    scores[3] = third_student_score
    
    higest_score = max(scores)
    for index, score in enumerate(scores):
        if score == higest_score:
            highest_students.append(index)
    return sorted(highest_students)

def check_answers(student_index, answers):
    score = 0
    number_of_answers = len(answers)
    if student_index == 1:
        first_student_answers = generate_first_student_answers(number_of_answers)
        for first_answer, answer in zip(first_student_answers, answers):
            if first_answer == answer:
                score += 1
    elif student_index == 2:
        second_student_answers = generate_second_student_answers(number_of_answers)
        for second_answer, answer in zip(second_student_answers, answers):
            if second_answer == answer:
                score += 1
    else:
        third_student_answers = generate_third_student_answers(number_of_answers)
        for third_answer, answer in zip(third_student_answers, answers):
            if third_answer == answer:
                score += 1
                
    return score
    
def generate_first_student_answers(number_of_answers):
    first_student_answers = [1, 2, 3, 4, 5] * (number_of_answers // 5 + 1)
    return first_student_answers[:number_of_answers]

def generate_second_student_answers(number_of_answers):
    second_student_answers = [2, 1, 2, 3, 2, 4, 2, 5] * (number_of_answers // 8 + 1)
    return second_student_answers[:number_of_answers]

def generate_third_student_answers(number_of_answers):
    third_student_answers = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (number_of_answers // 10 + 1)
    return third_student_answers[:number_of_answers]

