# a=int(input())
# count=0
# while a!=0:
#     if a%10==0:
#         count +=1
#     a//=10
# print(count)

# a=int(input())
# mini=a
# maxi=0
# c=0
# while a!=0:
#     c=a%10
#     if maxi<c:
#         maxi=c
#     if mini >c:
#         mini=c
#     a//=10
# print(mini, maxi)

print(str(bin(int(input()))).replace("0b",'')[::-1])