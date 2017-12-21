import string

file_fp=open('all.DAT', 'r')
file_wt=open('1hj.DAT', 'w')
list_all_line=file_fp.readlines()

line_num=[]
str=''
for i in range(0,len(list_all_line) ):
    line=list_all_line[i]
    tmp=line.split(',')
    
    if tmp[0]=='jx              ':
        str=tmp[2]
        if i > 1:
            file_wt.writelines(';')
            file_wt.writelines('\n')
    else:
        wline=str+','+line
        file_wt.writelines(wline)
	
