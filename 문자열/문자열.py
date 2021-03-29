#python 에서 p 와 t 만 출력해 보아라

letters = 'python'
print(letters[0], letters[2])   

#license_plate = "24가 2210" 에서 뒤의 4자리만 출력해보아라

license_plate = '24가 2210'
print(license_plate[-4:])

#홀짝홀짝홀짝 에서 홀만 출력하기

string = '홀짝홀짝홀짝'
print(string[::2])

#PYTHON 을 거꾸로 출력해보아라

string2 = 'PYTHON'
print(string2[::-1])

#010-1234-1234 에서 - 제거 하여 출력해보기

string3 = '010-1234-1234'
string3_1 = string3.replace('-', '')
print(string3_1)

