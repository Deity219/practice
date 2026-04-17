# 실습 02: 계산기 (Python)
# 오픈소스SW기초 실습


def add(a, b):
    """덧셈"""
    return a + b


def subtract(a, b):
    """뺄셈"""
    return a - b


def multiply(a, b):
    """곱셈"""
    return a * b


def divide(a, b):
    """나눗셈"""
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b


def main():
    print("=== 간단한 계산기 ===")
    print("연산자를 선택하세요: +, -, *, /")
    print("종료하려면 'q'를 입력하세요.")

    while True:
        user_input = input("\n계산식 입력 (예: 3 + 4): ").strip()
        if user_input.lower() == 'q':
            print("계산기를 종료합니다.")
            break

        parts = user_input.split()
        if len(parts) != 3:
            print("올바른 형식으로 입력하세요. (예: 3 + 4)")
            continue

        try:
            a = float(parts[0])
            operator = parts[1]
            b = float(parts[2])
        except ValueError:
            print("숫자를 올바르게 입력하세요.")
            continue

        try:
            if operator == '+':
                result = add(a, b)
            elif operator == '-':
                result = subtract(a, b)
            elif operator == '*':
                result = multiply(a, b)
            elif operator == '/':
                result = divide(a, b)
            else:
                print(f"지원하지 않는 연산자입니다: {operator}")
                continue

            print(f"결과: {a} {operator} {b} = {result}")
        except ValueError as e:
            print(f"오류: {e}")


if __name__ == "__main__":
    main()
