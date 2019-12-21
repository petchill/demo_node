result_list = []
num = 2
while len(result_list)<5:
  list_com = []
  for i in range(1,num):
    if num%i ==0:
      list_com.append(i)
  result=sum(list_com)
  if(result==num):
    result_list.append(num)
  num=num+1
print(result_list)