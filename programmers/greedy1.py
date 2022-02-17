def solution(n, lost, reserve):
    max_students_attending = 0
    students = [1 for _ in range(n+1)]
    
    for reserve_index in reserve:
        students[reserve_index] += 1
        
    for lost_index in lost:
        students[lost_index] -= 1
    
    for student_index in range(n+1):
        if students[student_index] == 0:
            if left_student_has_reserve(students, student_index):
                students[student_index-1] -= 1
                students[student_index] += 1
            elif right_student_has_reserve(students, student_index, n):
                students[student_index+1] -= 1
                students[student_index] += 1
            
    max_students_attending = students_has_suit(students)
    return max_students_attending

def left_student_has_reserve(students, student_index):
    if student_index == 1:
        return False
    if students[student_index-1] == 2:
        return True
    else:
        return False
    
def right_student_has_reserve(students, student_index, n):
    if student_index == n:
        return False
    if students[student_index+1] == 2:
        return True
    else:
        return False

def students_has_suit(students):
    students_has_suit = 0
    for student in students:
        if student >= 1:
            students_has_suit += 1
    return students_has_suit - 1 