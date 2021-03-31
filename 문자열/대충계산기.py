num1 = int(input("첫번째 숫자 입력"))
num2 = int(input("두번째 숫자 입력"))

print("1.+ 2.- 3.* 4./ 5.제곱")
choice = int(input())

if choice == 1:
    print(num1 + num2)
elif choice == 2:
    print(num1 - num2)
elif choice == 3:
    print(num1 * num2)
elif choice == 4:
    print(num1 / num2)
elif choice == 5:
    print(num1 ** num2)