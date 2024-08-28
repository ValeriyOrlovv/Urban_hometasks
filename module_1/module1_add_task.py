import statistics

GRADES = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
STUDENTS = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

def get_arithmetic_mean_for_students(grades, students):
    sorted_students = sorted(list(students))
    result = {}
    for i in range(len(sorted_students)):
        result[sorted_students[i]] = statistics.mean(grades[i])
    return result


print(get_arithmetic_mean_for_students(GRADES, STUDENTS))
