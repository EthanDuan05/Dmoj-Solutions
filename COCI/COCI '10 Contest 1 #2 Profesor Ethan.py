grade_f = [0]*5
student_f = [0]*5

cnt = 0
N = int(input())
for _ in range(N):
    A, B = map(int, input().split())
    if N == 1:
        grade_f[A - 1] += 1
        student_f[A - 1] += 1
        grade_f[B - 1] += 1
        student_f[B - 1] += 1
    else:
        if cnt == 0:
            grade_f[B - 1] += 1
            student_f[B - 1] += 1
            cnt += 1
        elif cnt == N-1:
            grade_f[A - 1] += 1
            student_f[A - 1] += 1
            cnt += 1
        else:
            grade_f[A - 1] += 1
            student_f[A - 1] += 1
            grade_f[B - 1] += 1
            student_f[B - 1] += 1
            cnt += 1

ans = max(grade_f)
grade = 0
student = 0
for i in range(5):
    if grade_f[i] == ans:
        grade = i+1
        student = student_f[i]
        break

print(student, grade)
print(student_f)
print(grade_f)
