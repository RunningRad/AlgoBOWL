import random

acceptable_edge_count = 10**5
current_edge_count = (10**5) + 1

while current_edge_count > acceptable_edge_count:
    current_edge_count = 0
    n = random.randint(2, 10**3)
    #n = 20
    #clear file
    with open('gen_input.txt', 'w') as file:
        pass

    #write edge lines to file
    with open('gen_input.txt', 'w') as file:
        file.write(str(n)+'\n')
        for node in range(1, n+1):
            edge_list = []
            m = random.randint(0, n-1)
            current_edge_count += m
            file.write(str(m)+' ')
            while len(edge_list) < m:
                edge = random.randint(1, n)
                if edge != node and edge not in edge_list:
                    edge_list.append(edge)
            for edge in edge_list:
                file.write(str(edge) + ' ')
            file.write('\n')
                
                    