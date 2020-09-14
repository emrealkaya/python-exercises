if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

avarage_list = list(student_marks[query_name])
summation = sum(avarage_list)
lenght = len(avarage_list)
avarage = summation / lenght
print("%.2f" % avarage)