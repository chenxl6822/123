'''创建一个包含不同数据类型的元组，并尝试访问和修改（注意元组不可变性）。'''
tuple = (10, 'hello', 3.14, True)

# 访问元组中的元素
print(tuple[0])  # 输出 10
print(tuple[1])  # 输出 'hello'
print(tuple[2])  # 输出 3.14
print(tuple[3])  # 输出 True

# 尝试修改元组中的元素，会报错
tuple[0] = 20

'''创建一个字典，键为字符串，值为整数，模拟一个简单的学生分数表。添加、修改、删除元素，并遍历字典。'''
# 创建学生分数表字典
stuscores = {'xiaoming': 90, 'kangkang': 85, 'hhh': 92}

# 添加元素
stuscores['who'] = 88

# 修改元素
stuscores['kangkang'] = 87

# 删除元素
del stuscores['xiaoming']

# 遍历字典
print("学生分数表：")
for student, score in stuscores.items():
    print(f"{student}: {score}")

'''使用集合操作，计算两个列表的交集和并集。'''
a = set('abcdabcdef')
 b = set('abcdlmn')
 a | b                              # 集合a或b中包含的所有元素（并集）
{'a', 'b', 'e', 'l', 'd', 'm', 'n', 'f', 'c'}
 a & b                              # 集合a和b中都包含了的元素（交集）
{'a', 'd', 'b', 'c'}

'''编写一个函数，将给定字符串中的每个单词反转（保持单词间的空格不变）。'''
def reverse_words(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

s = "hello world how are you"
print(reverse_words(s))

'''使用字符串格式化方法，生成一个包含姓名、年龄和职业的简单介绍。'''
name = "张三"
age = 35
carrer = "工程师"

introduction = f"大家好，我叫{name}，今年{age}岁，是一名{carrer}。"
print(introduction)
