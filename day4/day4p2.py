import sys
file = open(sys.argv[1])

count = 0
for line in file:
    sections = line.strip().split(',')
    section1 = list(map(int,sections[0].split('-')))
    section2 = list(map(int, sections[1].split('-')))
    if section1[0] <= section2[0] and section1[1] >= section2[1]:
        count+=1
    elif section2[0] <= section1[0] and section2[1] >= section1[1]:
        count+=1
    

print(count)
    
