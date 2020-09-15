def count_substring(string, sub_string):
    strlen = len(string)
    sblen = len(sub_string)
    counter=0
    for i in range(strlen-sblen+1):
        if(string[i:i+sblen]==sub_string):
            counter+=1
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)