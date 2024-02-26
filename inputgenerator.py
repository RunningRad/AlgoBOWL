import random

#condition 3 parameters
acceptable_edge_count = 10**5
current_edge_count = (10**5) + 1

#check for condition 3
while current_edge_count > acceptable_edge_count:
    current_edge_count = 0

    #generate n
    n = 10000
    #clear file
    with open('gen_input.txt', 'w') as file:
        pass

    with open('gen_input.txt', 'w') as file:
        #write n
        file.write(str(n)+'\n')

        #generate edge lines
        for node in range(1, n+1):
            edge_list = []

            #get and write m_i
            m = 10
            current_edge_count += m
            file.write(str(m)+' ')

            #get valid edges
            while len(edge_list) < m:
                edge = random.randint(1, n)
                #ensure no-self edges
                if edge != node and edge not in edge_list:
                    edge_list.append(edge)

            #write edges to file
            for edge in edge_list:
                file.write(str(edge) + ' ')
            file.write('\n')
                
print(current_edge_count)