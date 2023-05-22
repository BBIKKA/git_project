# 재수강 과정에서, 높은 성적만을 반영하는 기능은 결국 구현하지 못했습니다. 앞으로 더 열심히 공부하도록 하겠습니다.

# 클래스 정의
class CourseList:

    # '과목명'의 중복을 허용하는 리스트
    include_rep_list = []
    # '과목명'의 중복을 허용하지 않는 리스트
    not_include_rep_list = []

    # '과목명'이 key, '과목코드'가 value인 딕셔너리 ('과목명'의 중복을 허용하지 않음)
    name_code_dict = {}

    # 허용할 수 있는 평점 리스트
    grade_list = ['A+', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']

    # ['과목코드', '과목명', '학점', '평점']을 저장하는 리스트 ('과목명'의 중복을 허용함 + 평점 'F'의 존재를 허용함)
    all_list = []
    # ['과목코드', '과목명', '학점', '평점']을 저장하는 리스트 ('과목명'의 중복을 허용함 + 평점 'F'의 존재를 허용하지 않음)
    not_f_all_list = []

    # '3. 조회'함수에서 입력받은 과목이 all_list에 2개 이상 존재할 경우, 각 위치를 저장하는 리스트
    subject_num = []

    # 평점에서 점수로 변환하는 과정에서, 점수를 저장하는 리스트 (평점 'F'의 존재를 허용함)
    grade_score = []
    # 평점에서 점수로 변환하는 과정에서, 점수를 저장하는 리스트 (평점 'F'의 존재를 허용하지 않음)
    not_f_grade_score = []

    # (학점 * 평점)의 합 (평점 'F'의 존재를 허용함)
    sum_score = 0
    # (학점 * 평점)의 합 (평점 'F'의 존재를 허용함)
    sum_credit = 0
    # 평균 학점 (평점 'F'의 존재를 허용함)
    gpa = 0

    # (학점 * 평점)의 합 (평점 'F'의 존재를 허용하지 않음)
    not_f_sum_score = 0
    # 학점의 합 (평점 'F'의 존재를 허용하지 않음)
    not_f_sum_credit = 0
    # 평균 학점 (평점 'F'의 존재를 허용하지 않음)
    not_f_gpa = 0

    # 초기 과목 코드
    init_code = 10000

    # 인스턴스 정의
    def __init__(self):

        # 과목의 이름
        self.name = 'default_str'

        # 과목의 코드
        self.code = 'default_int'

        # 과목의 학점
        self.credit = 'default_int'

        # 과목의 평점
        self.grade = 'default_str'


# '1. 입력'함수
def credit_input():
    course = CourseList()

    # 과목명을 입력받음
    print("과목명을 입력하세요:")
    course.name = input()

    # 과목명을 '과목명'의 중복을 허용하는 리스트에 추가
    course.include_rep_list.append(course.name)

    # 과목명을 '과목명'의 중복을 허용하지 않는 리스트에 추가
    if course.name not in course.not_include_rep_list:
        course.not_include_rep_list.append(course.name)
    else:
        print("재수강 과목입니다")

    # 과목코드 생성
    course.code = code_gen(course)

    # 학점을 입력받음 & 예외처리
    print("학점을 입력하세요:")
    try:
        course.credit = int(input())
    except ValueError:
        print("올바른 형식의 데이터가 아닙니다.")
    finally:
        print("학점을 다시 입력하세요:")
        course.credit = int(input())

    # 평점을 입력받음
    print("평점을 입력하세요:")
    course.grade = input()

    # 예외처리
    if course.grade not in course.grade_list:
        print("올바른 형식의 평점이 아닙니다.")
        print("평점을 다시 입력하세요:.")
        course.grade = input()

    # 평점이 'F'인지 여부를 판단
    if course.grade != 'F':

        # 만약 평점이 'F'가 아니라면 평점 'F'를 허용하지 않는, 과목의 모든 정보가 담긴 리스트에 요소를 추가
        course.not_f_all_list.append([course.code, course.name, course.credit, course.grade])

    # 평점 'F'를 허용하는, 과목의 모든 정보가 담긴 리스트에 요소를 추가
    course.all_list.append([course.code, course.name, course.credit, course.grade])

    print("입력되었습니다.\n")


# 과목 코드 생성기
def code_gen(course):
    course = CourseList()
    if course.name not in course.not_include_rep_list:
        course.init_code += 1
        course.name_code_dict[course.name] = course.init_code
        course.name_code_dict[course.init_code] = course.name
        return course.init_code
    else:
        return course.name_code_dict[course.name]


# '2. 출력'함수
def credit_output():
    course = CourseList()

    # 평점 'F'를 허용하는, 과목의 모든 정보가 담긴 리스트에서 값을 뽑아와서 출력
    for i in range(len(course.include_rep_list)):
        print(f'[{course.all_list[i][1]}] {course.all_list[i][2]}학점 : {course.all_list[i][3]}')

# '3. 조회'함수
def credit_inquiry():
    course = CourseList()
    num = 0
    print("과목명을 입력하세요:")
    course.name = input()

    # 입력받은 과목명이 '과목명'의 중복을 허용하는 리스트에 존재하는지 확인
    if course.name in course.include_rep_list:

        # 입력받은 '과목명'이 '과목명'의 중복을 허용하는 리스트에서 어디에 위치해있는지 위치 정보를 알아내 리스트에 추가
        course.subject_num.append(course.include_rep_list.index(course.name))

        # 최악의 경우, 과목 10개를 입력하였고, 10개의 과목 중 9개의 과목이 나머지 1개의 과목에 대한 재수강일수 있으므로, '과목명'의 중복을 허용하는 리스트의 크기만큼 반복함
        for i in range(len(course.include_rep_list)):

            # '과목명'이 재수강 과목일경우, '과목명'의 위치 정보가 2개 이상이므로, 모든 위치 정보를 찾아야 함
            # 마지막 탐색의 경우, 찾는 정보가 없으므로 오류가 생김. 따라서 예외 처리를 통해 반복문 탈출
            try:

                # (이전에 찾았던 위치 + 1)부터 새롭게 '과목명'의 위치를 찾고, 그 위치 정보를 리스트에 추가
                course.subject_num.append(course.include_rep_list.index(course.name, course.subject_num[num] + 1))

                # '이전에 찾았던 위치'를 한 칸 옮겨서, 현재 시점에서, (이전에 찾았던 위치 + 1)부터 찾을 수 있도록 함
                num += 1

            except Exception:
                break

        # 위 과정을 통해 찾아낸 과목의 정보를 출력
        for i in range (len(course.subject_num)):
            print(f'[{course.all_list[course.subject_num[i]][1]}] {course.all_list[course.subject_num[i]][2]}학점 : {course.all_list[course.subject_num[i]][3]}')

    # 예외처리
    else:
        print("해당하는 과목이 없습니다.")

# '4. 계산'함수
def credit_calculation():
    course = CourseList()
    grade_to_score(course)

def grade_to_score(course):
    course = CourseList()

    for i in range(len(course.all_list)):
        match course.all_list[i][3]:
            case 'A+':
                course.grade_score.append(4.5)
            case 'A':
                course.grade_score.append(4.0)
            case 'B+':
                course.grade_score.append(3.5)
            case 'B':
                course.grade_score.append(3.0)
            case 'C+':
                course.grade_score.append(2.5)
            case 'C':
                course.grade_score.append(2.0)
            case 'D+':
                course.grade_score.append(1.5)
            case 'D':
                course.grade_score.append(1.0)
            case 'F':
                course.grade_score.append(0.0)

        course.sum_score += course.grade_score[i]*course.all_list[i][2]
        course.sum_credit += course.all_list[i][2]
    course.gpa = course.sum_score / course.sum_credit

    for i in range(len(course.not_f_all_list)):
        match course.not_f_all_list[i][3]:
            case 'A+':
                course.not_f_grade_score.append(4.5)
            case 'A':
                course.not_f_grade_score.append(4.0)
            case 'B+':
                course.not_f_grade_score.append(3.5)
            case 'B':
                course.not_f_grade_score.append(3.0)
            case 'C+':
                course.not_f_grade_score.append(2.5)
            case 'C':
                course.not_f_grade_score.append(2.0)
            case 'D+':
                course.not_f_grade_score.append(1.5)
            case 'D':
                course.not_f_grade_score.append(1.0)
            case 'F':
                course.not_f_grade_score.append(0.0)

        course.not_f_sum_score += course.not_f_grade_score[i] * course.not_f_all_list[i][2]
        course.not_f_sum_credit += course.not_f_all_list[i][2]
    course.not_f_gpa = course.not_f_sum_score / course.not_f_sum_credit

    print(f"제출용 : {course.not_f_sum_credit}학점 (GPA : {course.not_f_gpa:.2f})")
    print(f"열람용 : {course.sum_credit}학점 (GPA : {course.gpa:.2f})")

def credit_calculator():
    is_running = True
    while is_running == True:
        print("작업을 선택하세요.")
        print("     1. 입력")
        print("     2. 출력")
        print("     3. 조회")
        print("     4. 계산")
        print("     5. 종료")
        operation_num = input()
        match operation_num:
            case '1':
                credit_input()
            case '2':
                credit_output()
            case '3':
                credit_inquiry()
            case '4':
                credit_calculation()
            case '5':
                print("프로그램을 종료합니다.")
                is_running = False


credit_calculator()
