import json
import os
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

memo_file = os.getenv("MEMO_FILE", "memos.json")
memo_file = Path(__file__).parent / memo_file

def load_memos():
    try:
        with open(memo_file, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("JSON 파일의 데이터가 잘못되었습니다.")
        return []

def save_memos(memos):
    with open(memo_file, "w", encoding="utf-8") as file:
        json.dump(memos, file, ensure_ascii=False, indent=4)

def add_memo(memos):
    content = input("메모 내용: ")
    memo = {
        "id": len(memos) + 1,
        "content": content,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    memos.append(memo)
    save_memos(memos)
    print("메모가 저장되었습니다.")

def show_memos(memos):
    if len(memos) == 0:
        print("등록된 메모가 없습니다.")
        return
    for memo in memos:
        print("--------------------")
        print("번호:", memo["id"])
        print("내용:", memo["content"])
        print("작성일:", memo["date"])

def search_memo(memos):
    keyword = input("검색할 내용: ")
    found = False
    for memo in memos:
        if keyword in memo["content"]:
            print("--------------------")
            print("번호:", memo["id"])
            print("내용:", memo["content"])
            print("작성일:", memo["date"])
            found = True
    if found == False:
        print("검색 결과가 없습니다.")

memos = load_memos()

while True:
    print("===== 메모 프로그램 =====")
    print("1. 메모 추가")
    print("2. 전체 메모 조회")
    print("3. 메모 검색")
    print("4. 종료")
    choice = input("메뉴 선택: ")
    if choice == "1":
        add_memo(memos)
    elif choice == "2":
        show_memos(memos)
    elif choice == "3":
        search_memo(memos)
    elif choice == "4":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 메뉴입니다.")

