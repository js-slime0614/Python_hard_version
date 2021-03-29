#url = "http://sharebook.kr" 에서 kr(도메인) 만 따로 분리하여라
#문자열로 표현된 url에서 .을 기준으로 분리합니다. 분리된 url 중 마지막을 인덱싱하면 도메인만 출력할 수 있습니다.

url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[1])

#028 문자열은 immutable
#아래 코드의 실행 결과를 예상해보세요.
#
# >> lang = 'python'
# >> lang[0] = 'P'
# >> print(lang)

#문자열은 수정할 수 없습니다. 실행 결과를 확인해보면 문자열이 할당(assignment) 메서드를 지원하지 않음을 알 수 있습니다.

#아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.

string_replace = 'abcdfe2a354a32a'
string_replace = string_replace.replace('a', 'A')
print(string_replace)