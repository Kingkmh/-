def WordCound(date):
    ls={}
    for i in date:
        ls[i]=ls.get(i,0)+1
    return ls

if __name__=="__main__":
    f=open("Shakespeare Sonnet.txt")
    st=""
    for line in f.readlines():
        st+=line
    print(WordCound(st))
    f.close()
