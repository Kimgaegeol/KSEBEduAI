import numpy as np
import pandas as pd

{
# a = np.array([1,3,5,7])
# print(a, a.ndim) # 1

# b = np.array([[1,2,3,4], [5,6,7,8],[9,10,11,12]])
# print(b, b.ndim) # 2

# c = np.array([[[1,2,3,4,1], [5,6,7,8,1]]])
# print(c)
# print(c.ndim) # ndim : 배원의 차원 수
# print(c.shape) # shape : 배열의 차원과 크기를 나타내는 tuple 형태의 속성
# print(c.dtype) # dtype : 배열 요소들의 데이터 타입을 나타내는 속성 (요소들은 해당 데이터 타입으로 일괄적으로 처리)
# print(c.strides) # 면 행 열의 간격 이라고 보면됨

# zeros(), ones() : 주어진 모양(shape)에 대해 모든 요소가 0 또는 1인 배열을 생성하는 함수
# ones = np.ones([3,4])
# zeros = np.zeros([3,4], dtype=np.int16) # int 32, int 64 다 가능
# zeros2 = np.zeros([2,3,4]) # int 32, int 64 다 가능
# print(zeros)
# print(zeros2)

# arange() : 지정된 범위 내에서 일정한 간격으로 숫자가 담긴 배열을 생성하는 함수
# a = np.arange(5,11)
# print(a, a.ndim, a.shape, a.size)

# a = np.arange(2.0,11.8,2.0, dtype=np.int16)
# print(a, a.ndim, a.shape, a.size)

# linspace() : 지정된 범위 내에서 균등하게 분할된 숫자가 담긴 배열을 생성하는 함수
# reshape() : 배열의 모양(shape)을 변경하는 메서드로, 새로운 모양에 맞게 요소들을 재배열

# df = pd.DataFrame(
# {"a" : [4, 5, 6],"b" : [7, 8, 9],"c" : [10, 11, 12]},
#     index = [1,2,3]
# )
# print(df , end="\n\n")
#
# df = pd.DataFrame(
#     [[4,7,10],[5,8,11],[6,9,12]],
#     index = [1,2,3],
#     columns = ['a','b','c']
# )
# print(df)
# print()

# s = pd.Series([1,2,3,4])
# s = pd.Series([1,2,3,4], index=['a','b','c','d'])
# print(s)
# s2 = pd.Series([99,100,98,91,93])
# s2_subset = s2[2:4]
# print(s2_subset)

# df = pd.DataFrame(
#     {"a" : [4 ,5, 6],
#     "b" : [7, 8, 9],
#     "c" : [10, 11, 12]},
#     index = pd.MultiIndex.from_tuples([('d', 0), ('e', 1), ('f', 2)], names=['x','y'])
# )
#
# print(df)
#
# pd.melt(df)
# print(df)
}
