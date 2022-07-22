
# import json
# a={
#     "shopping_list":
#         { 
#             "chaco":"15",
#             "Biscuits":"50",
#             "Diary_milk":"30",
#             "ice_cream":"20",
#         } 
# }

# k=input("enter the item")
# s=int(input("enter the quantity"))
# for i in a:
#     for j in a[i]:
#         if k in a[i]:
#             if j==k and int(a[i][j])>=s:
#                 b=int(a[i][j])-s
#                 a[i][j]=str(b)
#                 break
#         elif j!=k:
#             print("not available")
#             break
# n=open("data2.json","w")
# json.dump(a,n,indent=4)
