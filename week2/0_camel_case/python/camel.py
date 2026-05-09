def convert(camel_case: str) -> str:
    snake_case = ''
    for char in camel_case:
        c = '_' + char.lower() if char.isupper() else char
        snake_case = snake_case + c
    return snake_case