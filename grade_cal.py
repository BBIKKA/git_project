grade_list = []
grade_list_Fx = []

grade_credit = []
grade_credit_Fx = []

grade_credit_num = []
grade_credit_num_Fx = []

GPA_Fo = 0
GPA_Fx = 0


def input_grade():
    
    grade = int(input("학점을 입력하세요:\n"))
    grade_list.append(grade)

    credit = input("평점을 입력하세요:\n")
    grade_credit.append(credit)

    print("입력되었습니다.\n")

def grade_calculator_Fo():

    total_Fo = 0
    sum_grade_Fo = 0

    for i in range(len(grade_list)):

        match grade_credit[i]:
            case 'A+':
                grade_credit_num.append(4.5)
            case 'A':
                grade_credit_num.append(4.0)
            case 'B+':
                grade_credit_num.append(3.5)
            case 'B':
                grade_credit_num.append(3.0)
            case 'C+':
                grade_credit_num.append(2.5)
            case 'C':
                grade_credit_num.append(2.0)
            case 'D+':
                grade_credit_num.append(1.5)
            case 'D':
                grade_credit_num.append(1.0)
            case 'F':
                grade_credit_num.append(0.0)
        
    for j in range(len(grade_list)):

        sum_grade_Fo += grade_list[j]
        total_Fo += grade_list[j] * grade_credit_num[j]

    GPA_Fo = total_Fo / sum_grade_Fo
    
    print("열람용 : %d학점 (GPA : %.2f)" % (sum_grade_Fo, GPA_Fo))


def grade_calculator_Fx():

    total_Fx = 0
    sum_grade_Fx = 0

    F_location = 0

    grade_list_Fx = grade_list[:]
    grade_credit_Fx = grade_credit[:]

    for k in range(grade_credit.count('F')):
        
        F_location = grade_credit_Fx.index('F')

        del grade_list_Fx[F_location]
        del grade_credit_Fx[F_location]

    
    for i in range(len(grade_list_Fx)):

        match grade_credit_Fx[i]:
            case 'A+':
                grade_credit_num_Fx.append(4.5)
            case 'A':
                grade_credit_num_Fx.append(4.0)
            case 'B+':
                grade_credit_num_Fx.append(3.5)
            case 'B':
                grade_credit_num_Fx.append(3.0)
            case 'C+':
                grade_credit_num_Fx.append(2.5)
            case 'C':
                grade_credit_num_Fx.append(2.0)
            case 'D+':
                grade_credit_num_Fx.append(1.5)
            case 'D':
                grade_credit_num_Fx.append(1.0)
            case 'F':
                grade_credit_num_Fx.append(0.0)
        
    for j in range(len(grade_list_Fx)):

        sum_grade_Fx += grade_list_Fx[j]
        total_Fx += grade_list_Fx[j] * grade_credit_num_Fx[j]

    GPA_Fx = total_Fx / sum_grade_Fx

    print("제출용 : %d학점 (GPA : %.2f)" % (sum_grade_Fx, GPA_Fx))



def base():

    print("작업을 선택하세요.\n")
    print("1. 입력\n2. 계산")

    ans = int(input())

    match ans:
        case 1:
            input_grade()
            base()

        case 2:
            grade_calculator_Fx()
            grade_calculator_Fo()



base()
print('프로그램이 종료되었습니다.')

# 3학점 : A, 2학점 : F, 3학점 : B+, 1학점 : D