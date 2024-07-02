#회원가입 (본인)
print("안녕하세요? 회원가입 시 개인정보를 입력해주세요.")
name1=input('이름을 입력하시오.')
age1=input('나이를 입력하시오.')
email1=input('이메일 주소를 입력하시오.')
phon1=input('연락처를 입력하시오.')

name2=input('이름을 입력하시오.')
age2=input('나이를 입력하시오.')
email2=input('이메일 주소를 입력하시오.')
phon2=input('연락처를 입력하시오.')

#등록자 (타인)
회원1={name1:[age1,email1,phon1]}
회원2={name2:[age2,email2,phon2]}

print(회원1)
print(회원2)