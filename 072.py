# 숫자 리스트에서 최댓값과 최솟값을 찾아 출력합니다.
listdata = [9.96, 1.27, 5.07, 6.45, 8.38, 9.29, 4.93, 7.73, 4.71, 0.93]
maxval = max(listdata)
minval = min(listdata)
print(maxval)  # 최댓값 9.96이 출력됩니다.
print(minval)  # 최솟값 0.93이 출력됩니다.

# 문자열에서 최댓값과 최솟값을 찾아 출력합니다.
txt = 'Alotofthingsoccureachday'
maxval = max(txt)  # 문자열에서 최댓값 'y'가 출력됩니다.
minval = min(txt)  # 문자열에서 최솟값 'A'가 출력됩니다.
print(maxval)   # 'y'가 출력됩니다.
print(minval)   # 'A'가 출력됩니다.

# 숫자식 결과와 문자열 비교에서 최댓값과 최솟값을 찾아 출력합니다.
maxval = max(2+3, 2*3, 2**3, 3**2)  # 숫자식 결과 중 최댓값 9가 출력됩니다.
minval = min('abx', 'a12')           # 문자열 비교 중 최솟값 'a12'가 출력됩니다.
print(maxval)  # 9가 출력됩니다.
print(minval)  # 'a12'가 출력됩니다.
