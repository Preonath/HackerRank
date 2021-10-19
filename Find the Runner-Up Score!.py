s=map(int,input().split())
st=set(s)
st.remove(max(st))
print(max(st))