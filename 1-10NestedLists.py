nlist=[]
score_list=[]
if __name__ == '__main__':
        for _ in range(int(input())):
                name = input()
                score = float(input())
                nlist+=[[name,score]]
                score_list+=[score]
        x=sorted(list(set(score_list)))[1] 

        for n,s in sorted(nlist):
                if s==x:
                    print(n)