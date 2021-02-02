#num = 2520
#while True:
#    num+= 1
#    num_dict = {1:'no', 2:'no'}
#    for i in num_dict.keys():
#        if num / i == 0:
#            num_dict[i] == 'y'
#    if all(v == 'y' for v in num_dict.values()):
#        print(num)
#        break

check_list = [11, 13, 14, 16, 17, 18, 19, 20]

def find_solution(step):
    for num in range(step, 99999999999, step):
        if all(num % n == 0 for n in check_list):
            return num
    return None

if __name__ == '__main__':
    solution = find_solution(20)
    print(solution)
