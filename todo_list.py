import os

TODO_FILE = 'todo_list.txt'

# Read
# 프로그램 시작 시 할 일 목록을 파일(todo_list.txt)에서 불러옴
# 파일 존재하는 경우, 읽기모드 & 라인 단위로 자른 리스트 값 반환
# 파일 존재하지 않는 경우, 빈 리스트 반환
def load_todo_list():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return file.read().splitlines()
    return []

# 할 일 목록 저장
# 파일 쓰기모드로 열기
# 파일에 한 줄 씩 작성 가능 
def save_todo_list(todo_list):
    with open(TODO_FILE, 'w') as file:
        for item in todo_list:
            file.write(item + '\n')

# 할 일 목록 표시 (Read)
# 할 일 존재하지 않는 경우: 할 일이 없음을 출력
# 할 일 존재하는 경우: 할 일 목록 출력  
def display_todo_list(todo_list):
    if not todo_list:
        print("할 일이 없습니다.")
    else:
        print("\n할 일 목록:")
        for idx, item in enumerate(todo_list, 1):
            print(f"{idx}. {item}")

# 할 일 추가 (Create)
def add_todo_item(todo_list):
    item = input("추가할 할 일을 입력하세요: ")
    todo_list.append(item)
    print(f"'{item}'이(가) 목록에 추가되었습니다.")

# 할 일 수정 (Update)
# 할 일 목록 표시
# 특정 라인의 내용을 새로운 내용으로 업데이트
# 0보다 크고 목록 개수보다 작은 범위 내의 번호를 입력하지 않을 시 유효하지 않은 번호임을 출력
# 숫자가 아닌 잘못된 값을 입력한 경우 예외 처리 
def edit_todo_item(todo_list):
    display_todo_list(todo_list)
    if todo_list:
        try:
            idx = int(input("수정할 할 일 번호를 입력하세요: ")) - 1
            if 0 <= idx < len(todo_list):
                new_item = input(f"수정할 내용을 입력하세요 (현재: {todo_list[idx]}): ")
                todo_list[idx] = new_item
                print(f"할 일 {idx+1}번 '{new_item}'으로 수정되었습니다.")
            else:
                print("유효하지 않은 번호입니다.")
        except ValueError:
            print("유효한 번호를 입력하세요.")

# 할 일 삭제 (Delete)
# 할 일 목록 표시
# 사용자가 삭제할 할 일 번호 입력
# 0보다 크고 목록 개수보다 작은 범위 내의 번호를 입력하지 않을 시 유효하지 않은 번호임을 출력
# 숫자가 아닌 잘못된 값을 입력한 경우 예외 처리 
def delete_todo_item(todo_list):
    display_todo_list(todo_list)
    if todo_list:
        try:
            idx = int(input("삭제할 할 일 번호를 입력하세요: ")) - 1
            if 0 <= idx < len(todo_list):
                removed_item = todo_list.pop(idx)
                print(f"'{removed_item}'이(가) 목록에서 삭제되었습니다.")
            else:
                print("유효하지 않은 번호입니다.")
        except ValueError:
            print("유효한 번호를 입력하세요.")

def main():
    todo_list = load_todo_list()

    while True:
        print("\n[오늘의 할 일]")
        print("1. 할 일 목록 표시")
        print("2. 할 일 추가")
        print("3. 할 일 삭제")
        print("4. 할 일 수정")
        print("5. 종료")

        choice = input("원하는 작업의 번호를 입력하세요: ")

        if choice == '1':
            display_todo_list(todo_list)
        elif choice == '2':
            add_todo_item(todo_list)
            save_todo_list(todo_list)
        elif choice == '3':
            delete_todo_item(todo_list)
            save_todo_list(todo_list)
        elif choice == '4':
            edit_todo_item(todo_list)
            save_todo_list(todo_list)
        elif choice == '5':
            save_todo_list(todo_list)
            print("프로그램을 종료합니다.")
            break
        else:
            print("유효하지 않은 선택입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()