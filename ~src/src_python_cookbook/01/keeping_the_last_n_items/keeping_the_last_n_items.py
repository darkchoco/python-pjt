# -*- coding=UTF-8 -*-

# Example of keeping the last n items

from collections import deque

# generator function. return 대신 yield 를 사용하고, 호출 시에는 for 등으로 호출한다.
# 이렇게 하는 것의 장점은(List Comprehension 등과 비교해서) 메모리의 절약이다.
# 아래 Logic을 보면, __main__으로부터 search 모듈이 실행, 계속 for line in lines loop를 돌다가 yield 문으로 들어가면
# 곧장 search 모듈을 빠져나와서 __main__의 for pline in prevlines를 실행한다. 이를 마치면 다시 search 모듈내 yield의
# 다음 문장, 즉 previous_lines.append(line)으로 가서 앞서 하던 것을 계속 실행한다.
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file
if __name__ == '__main__':
#    with open('somefile.txt') as f:
    with open('somefile.txt', 'r', encoding="utf8") as f:
        for line, prevlines in search(f, 'python', 3):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)
