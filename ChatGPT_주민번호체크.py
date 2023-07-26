import re

def check_korean_social_security_number(ssn):
    pattern = r'^\d{6}-(1|2)\d{6}$'
    return re.search(pattern, ssn) is not None

# Test cases
print(check_korean_social_security_number("123456-1234567"))  # Should return True
print(check_korean_social_security_number("12345-1234567"))   # Should return False
print(check_korean_social_security_number("123456-2234567"))  # Should return True
print(check_korean_social_security_number("123456-0234567"))  # Should return False
print(check_korean_social_security_number("123456-123456"))   # Should return False
print(check_korean_social_security_number("12345-12345678"))  # Should return False
