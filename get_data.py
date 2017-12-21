import string

file_fp=open('all.DAT', 'r')
file_wt=open('write.DAT', 'w')
list_all_line=file_fp.readlines()

line_num=[]
str=''
for i in range(0,len(list_all_line) ):
    line=list_all_line[i]
    tmp=line.split(',')
    
    if tmp[0]=='BHDD2016        ':
        if i > 1:
            iteor=line_num[len(line_num)-1]
            tmp0=list_all_line[iteor].split(',') 
            wline=tmp0[2]+','+list_all_line[i-1]
            file_wt.writelines(wline)
            
#     file_wt.writelines(line)
        line_num.append(i)
        str=tmp[2]
        wline=tmp[2]+','+list_all_line[i+1]
        file_wt.writelines(wline)
    else:
        num=string.atoi(tmp[0])
        
        if num%5==0:
            wline=str+','+line
            file_wt.writelines(wline)
