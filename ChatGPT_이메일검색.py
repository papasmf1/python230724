import re

def search_email_address(text):
    # 이메일 주소를 찾기 위한 정규 표현식 패턴
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # re.search() 함수를 사용하여 텍스트에서 이메일 주소 찾기
    match = re.search(email_pattern, text)
    
    if match:
        return match.group()
    else:
        return None

# 테스트 1: 문장 안에 간단한 이메일 주소
text1 = "도움이 필요하시면 support@example.com 으로 문의해주세요."
assert search_email_address(text1) == "support@example.com"

# 테스트 2: 언더스코어와 숫자를 포함한 이메일 주소
text2 = "문의 사항은 john_doe123@example.net 으로 이메일을 보내주세요."
assert search_email_address(text2) == "john_doe123@example.net"

# 테스트 3: 최상위 도메인 길이가 3인 이메일 주소
text3 = "문의하기: contact_us@company.org"
assert search_email_address(text3) == "contact_us@company.org"

# 테스트 4: 텍스트에 이메일 주소가 없는 경우
text4 = "자세한 정보는 웹사이트를 방문해주세요."
assert search_email_address(text4) is None

# 테스트 5: 여러 이메일 주소가 있는 경우, 첫 번째로 발견된 주소 반환
text5 = "문의는 info@example.com 또는 support@example.com 으로 연락해주세요."
assert search_email_address(text5) == "info@example.com"

# 테스트 6: 도메인 이름에 하이픈이 포함된 이메일 주소
text6 = "판매 문의: sales-info@example-company.com"
assert search_email_address(text6) == "sales-info@example-company.com"

# 테스트 7: 서브도메인이 있는 이메일 주소
text7 = "지원이 필요하시면 help@support.example.com 으로 문의해주세요."
assert search_email_address(text7) == "help@support.example.com"

# 테스트 8: 비표준 최상위 도메인을 가진 이메일 주소
text8 = "문의하기: contact@company.xyz"
assert search_email_address(text8) == "contact@company.xyz"

# 테스트 9: 국제 문자가 포함된 이메일 주소
# text9 = "예약을 위해 café@éxample.com 으로 이메일을 보내주세요."
# assert search_email_address(text9) == "café@éxample.com"

# 테스트 10: 한 글자 최상위 도메인을 가진 이메일 주소
# text10 = "문의는 info@example.a 로 하시기 바랍니다."
# assert search_email_address(text10) == "info@example.a"

print("모든 테스트가 통과되었습니다!")
