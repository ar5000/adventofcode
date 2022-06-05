with open('input.txt','r',encoding='utf-8') as f:
    rules = []
    for line in f:
        rules.append(line.strip('\n').split('contain'))

global shiny
shiny = []
def findbag(color):
    count = len(shiny)
    print(f'Current count is {count}')
    for line in rules:
        for i in line[1:]:
            # print(i)
            if color in i:
                shiny.append(line)
    if count == len(shiny):
        return shiny
    else:
        return findbag(??)


    return shiny

findbag('shiny gold')

for line in shiny:
    print(line)

# def get_recursive_factorial(n):
#     if n < 0:
#         return -1
#     elif n < 2:
#         return 1
#     else:
#         return n * get_recursive_factorial(n-1)

# print(get_recursive_factorial(6))