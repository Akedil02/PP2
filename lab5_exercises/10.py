def camel_to_snake(camel_case):
    snake_case = ''.join(['_' + char.lower() if char.isupper() else char for char in camel_case])
    # 如果字符串以下划线开头，则去除第一个下划线
    if snake_case.startswith('_'):
        snake_case = snake_case[1:]
    return snake_case

# 示例使用
camel_string = "thisIsCamelCaseString"
snake_string = camel_to_snake(camel_string)

print(f'驼峰式字符串: {camel_string}')
print(f'转换后的蛇形式字符串: {snake_string}')
