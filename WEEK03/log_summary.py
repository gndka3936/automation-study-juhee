import json

def read_log():
    logs = []
    try:
        with open("test_log.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split(",")
                if len(parts) != 3:
                    print("잘못된 로그:", line)
                    continue
                date = parts[0].strip()
                test_name = parts[1].strip()
                result = parts[2].strip()
                if result != "PASS" and result != "FAIL":
                    print("잘못된 결과:", line)
                    continue
                logs.append({
                    "date": date,
                    "test_name": test_name,
                    "result": result
                })
    except FileNotFoundError:
        print("test_log.txt 파일을 찾을 수 없습니다.")
    return logs

def make_summary(logs):
    total = len(logs)
    pass_count = 0
    fail_count = 0
    fail_tests = []
    for log in logs:
        if log["result"] == "PASS":
            pass_count += 1
        elif log["result"] == "FAIL":
            fail_count += 1
            fail_tests.append(log["test_name"])
    if total > 0:
        success_rate = pass_count / total * 100
    else:
        success_rate = 0
    summary = {
        "total": total,
        "pass": pass_count,
        "fail": fail_count,
        "success_rate": success_rate,
        "fail_tests": fail_tests
    }
    return summary

def save_summary(summary):
    with open("summary.json", "w", encoding="utf-8") as file:
        json.dump(summary, file, ensure_ascii=False, indent=4)

logs = read_log()
summary = make_summary(logs)
print("전체 테스트:", summary["total"])
print("PASS:", summary["pass"])
print("FAIL:", summary["fail"])
print("성공률:", summary["success_rate"], "%")
print("실패한 테스트")
for test in summary["fail_tests"]:
    print("-", test)
save_summary(summary)
print("summary.json 저장 완료")