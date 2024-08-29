import re 
def is_valid_password(password): 
    #Позитивний Lookahead Assertion: 
    '''(?=...) — Це позитивний lookahead. Він перевіряє, чи слідує за поточною позицією в рядку
      певний шаблон, але не змінює позицію в рядку
      і не включає перевіряний шаблон у фінальний результат.'''
    
    ''' .* — Це частина шаблону всередині lookahead, що означає "будь-яка кількість 
    будь-яких символів". .* дозволяє шаблону перевіряти, чи є зазначений шаблон (...) десь
    у рядку після будь-якої кількості символів. '''
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,16}$') 
    return bool(pattern.match(password)) 


password = input("Enter your password: ") 
if is_valid_password(password): 
    print("Password is valid.")
else: 
    print("Password is invalid.")