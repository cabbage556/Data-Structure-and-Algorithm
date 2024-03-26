# 숫자와 배열을 포함하는 배열의 모든 원소를 출력하기
#       원소인 배열은 다시 수와 배열을 포함할 수 있음
def print_every_element(arr):
    for value in arr:
        # 원소가 리스트이면 재귀 호출
        if isinstance(value, list):
            print_every_element(value)
        # 원소가 리스트가 아니면 출력
        else:
            print(value)


array = [
    1,
    2,
    3,
    [4, 5, 6],
    7,
    [8,
     [9, 10, 11,
      [12, 13, 14],
      ]
     ],
    [15, 16, 17, 18, 19,
     [20, 21, 22,
      [23, 24, 25,
       [26, 27, 29]
       ], 30, 31
      ], 32
     ], 33
]
print_every_element(array)
