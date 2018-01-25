f = open('AviationData.txt', 'r')
data = f.read()
aviation_data = data.split('\n')

aviation_list=[]
for line in aviation_data:
    aviation_list.append(line.split(" | "))
    
lax_code = []

for row in aviation_list:
    for cell in row:
        if cell=='LAX94LA336':
            lax_code = row
            
print (lax_code)