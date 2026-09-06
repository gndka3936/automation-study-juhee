import json

def read_emails():
    emails = []
    try:
        with open("emails.txt", "r", encoding="utf-8") as file:
            for line in file:
                email = line.strip()
                if email:
                    emails.append(email)
    except FileNotFoundError:
        print("emails.txt 파일을 찾을 수 없습니다.")
    return emails

def parse_emails(emails):
    result = []
    domain_count = {}

    for email in emails:
        if email.count("@") == 1:
            parts = email.split("@")

            if parts[0] and parts[1] and "." in parts[1]:
                user_id = parts[0]
                domain = parts[1]

                result.append({
                    "id": user_id,
                    "domain": domain
                })

                if domain in domain_count:
                    domain_count[domain] += 1
                else:
                    domain_count[domain] = 1
            else:
                print("잘못된 이메일:", email)
        else:
            print("잘못된 이메일:", email)

    return result, domain_count

def save_json(emails, domain_count):
    data = {
        "emails": emails,
        "domain_count": domain_count
    }

    try:
        with open("parsed_emails.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print("파일 저장 중 오류가 발생했습니다:", e)

emails = read_emails()
parsed_emails, domain_count = parse_emails(emails)
save_json(parsed_emails, domain_count)

print("이메일 분석이 완료되었습니다.")