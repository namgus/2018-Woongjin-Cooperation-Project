fin = open("asd.txt",'r')
fout= open("sample.txt",'w')

#informal spliting for showing index
time = []
loc = []
cur_time = []
cur_loc = []
prev_time = []
prev_loc = []
time_log = []
log = []
userID = []
userAll = []

fence = []
zone = []

sex = []
age = []

wr_sex = []
wr_age = []
wr_zone = []

line = fin.readline().strip().split("\t")
fout.write("userID\tTime_log\tZone\tFence\tAge\tSex\tRemains\n")

#read data from input file and slice it
# user  x  y  time  zone  fence  age  sex

while (1): 
    factor = fin.readline()
    factor_string = factor.strip().split("\t")
    if not factor:
        break
    if not userID :
        userID.append(factor_string[0])
    else :
        if userID[-1] != factor_string[0] :
             userID.append(factor_string[0])
    log.append(factor_string[1])
    zone.append(factor_string[2])
    time.append(factor_string[1][8:])
    fence.append(factor_string[3])
    userAll.append(factor_string[0])
    sex.append(factor_string[5])
    age.append(factor_string[4])

#divide by ID

count = len(fence)
    
for i in range(count -1):
    if not userID:
        cur_time.append(time[i+1])
        cur_loc.append(fence[i+1])
        wr_sex.append(sex[i+1])
        wr_age.append(age[i+1])
        wr_zone.append(zone[i+1])
        prev_time.append(time[i])
        prev_loc.append(fence[i])

        time_log.append(log[i])
        userID.append(userAll[i])   
    elif (fence[i] != fence[i+1]):
        cur_time.append(time[i+1])
        cur_loc.append(fence[i+1])
        wr_sex.append(sex[i+1])
        wr_age.append(age[i+1])
        wr_zone.append(zone[i+1])
        prev_time.append(time[i])
        prev_loc.append(fence[i])

        time_log.append(log[i])
        userID.append(userAll[i])
        

 
#print initial state

        
#print  
for i in range(len(cur_time)) :
    remaining = int(cur_time[i]) - int(prev_time[i])
    fout.write(userID[i]+ '\t'+ time_log[i] + '\t '+wr_zone[i] + '\t' +  cur_loc[i] + '\t'+ wr_age[i] + '\t' + wr_sex[i] + '\t'+  str(remaining) + '\n')

fin.close()
fout.close()

