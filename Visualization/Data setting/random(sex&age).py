import random

# make randomized samples for sex and age
a = input("input no: ")
f_name = "output_" + str(a) + '.txt'
ff_name = "output_" + str(a) + 'sa.txt'


fin = open(f_name,'r')
fout= open(ff_name,'w')
#informal spliting for showing index

time = []
loc = []
age = []
sex = []
userAll = []
userID = []
x = []
y = []
zone = []

line = fin.readline().strip().split("\t")

#read data from input file and slice it

while (1): 
    factor = fin.readline()
    factor_string = factor.strip().split("\t")
    if not factor: break
    
    if not userID :
        userID.append(factor_string[0])
    else :
        if userID[-1] != factor_string[0] :
            userID.append(factor_string[0])
     
    time.append(factor_string[1])
    userAll.append(factor_string[0])
    zone.append(factor_string[2])
    loc.append(factor_string[3])

userAll.append(0)
print(len(time))

for i in range(len(time)):
    if not sex:
        sex.append(random.randrange(0,2))
        age.append(random.randrange(0,9))
        
    if userAll[i] != userAll[i + 1] :
        sex.append(random.randrange(0,2))
        age.append(random.randrange(0,9))

    else:
        sex.append(sex[i])
        age.append(age[i])


    
        
# ID X Y Zone Age Sex
fout.write("userID\tLOC_X\tLOC_Y\tTimeStamp\tZone\tFence\tAge\tSex\n")

for i in range(len(time)):
    fout.write(userAll[i] + '\t'+ time[i] + '\t'+ zone[i] + '\t' + loc[i] + '\t'+ str(age[i]) + '\t' + str(sex[i]) + '\t\n')

print(len(userID))
fin.close()
fout.close()

