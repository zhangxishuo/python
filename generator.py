import randomchar;

def generate_password(length):
    if length < 4:
        raise ValueError('密码至少为 4 位')

    random_char = randomchar.RandomChar()
    # 随机大写字符
    password = random_char.uppercase()
    # 随机小写字符
    password += random_char.lowercase()
    # 随机数字
    password += random_char.digit()
    # 随机特殊字符
    password += random_char.special()
    
    count = 4
    while count < length:
        password += random_char.anyone()
        count += 1
    return password

password_length = int(input('请输入密码长度（8 ~ 20）：'))

if password_length < 8 or password_length > 20:
    raise ValueError('密码长度不符合要求')

password = generate_password(password_length)
print(password)