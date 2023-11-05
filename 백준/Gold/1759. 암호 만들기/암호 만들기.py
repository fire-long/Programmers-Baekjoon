def generate_passwords(password_length, characters, current_password, idx, vowels_count, consonants_count):
    if len(current_password) == password_length:
        if vowels_count >= 1 and consonants_count >= 2:
            print(current_password)
        return
    
    if idx >= len(characters):
        return

    # 현재 문자를 포함하고 다음 문자를 확인
    generate_passwords(password_length, characters, current_password + characters[idx],
                       idx + 1, vowels_count + (characters[idx] in 'aeiou'),
                       consonants_count + (characters[idx] not in 'aeiou'))
    
    # 현재 문자를 제외하고 다음 문자를 확인
    generate_passwords(password_length, characters, current_password,
                       idx + 1, vowels_count, consonants_count)

# 입력값 읽어오기
L, C = map(int, input().split())
characters = input().split()

# 정렬
characters.sort()

generate_passwords(L, characters, '', 0, 0, 0)