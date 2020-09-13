if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 == 1:
        print ("Weird")
    elif n in range(6,21):
        print("Weird")
    elif n in range(2,5):
        print("Not Weird")
    else:
        print("Not Weird")
