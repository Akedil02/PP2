def snake_to_camel(snake_case):
    words = snake_case.split('_')
    camel_case = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel_case

snake_string = "hello_world_example"
camel_string = snake_to_camel(snake_string)

print({snake_string})
print({camel_string})
