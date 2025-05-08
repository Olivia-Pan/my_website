class Graph():
    def __init__(self, nodes, links):
        self.nodes = nodes
        self.links = links
        self.size = len(self.nodes)
        self.route_matrix = [[None] * self.size for _ in range(self.size)]
        self.edges_matrix = [[[] for _ in range(self.size)] for _ in range(self.size)]

    def get_time_matrix(self):
        size = self.size
        time_matrix = [[float('inf') for _ in range(size)] for _ in range(size)]
        for i in range(size):
            time_matrix[i][i] = 0
        
        for link in self.links:
            i = link.starting_node.num - 1
            j = link.ending_node.num - 1
            if link.time < time_matrix[i][j]:
                time_matrix[i][j] = link.time
                self.edges_matrix[i][j] = [link.get_pseudo_edge()]

        for k in range(size):
            for i in range(size):
                for j in range(size):
                    if time_matrix[i][j] > time_matrix[i][k] + time_matrix[k][j]:
                        time_matrix[i][j] = time_matrix[i][k] + time_matrix[k][j]
                        self.edges_matrix[i][j] = self.edges_matrix[i][k] + self.edges_matrix[k][j]
        return time_matrix

    


class Node():
    '''This class represent a single Node.'''
    """A single vertex in a graph"""

    def __init__(self, num, stop_IDs):
        # num: node number (1-16)
        # stops: a list of stop IDs within the area of the node
        self.num = num
        self.stop_IDs = stop_IDs
        self.visited = False
        self.label = 'node' + str(self.num)

    def is_connecting_node(self):
        if len(self.stop_IDs) > 1:
            return True
        return False
    
    def __str__(self):
        return 'node' + str(self.num)
    
    def was_visited(self):
        return self.visited 
    
    def get_label(self):
        return self.label
    

class Link():

    def __init__(self, shuttle_number, starting_node, ending_node, time):
        self.shuttle_number = shuttle_number
        self.starting_node = starting_node
        self.ending_node = ending_node
        self.time = time

    def get_pseudo_edge(self):
        return Edge(self.starting_node, self.ending_node, self.time)
    
    def __str__(self): 
        return str(self.starting_node.__str__() + '--' + str(self.time) +'-->' + self.ending_node.__str__())

class Edge():

    def __init__(self, starting_node, ending_node, time):
        self.starting_node = starting_node
        self.ending_node = ending_node
        self.time = time

    def __str__(self): 
        return str(self.starting_node.__str__() + '--' + str(self.time) +'-->' + self.ending_node.__str__())


class Bus():
    """A circular linked list for each bus"""
    def __init__(self, shuttle_number, nodes_in_order, times_in_order):
        self.shuttle_number = shuttle_number
        self.nodes_in_order = nodes_in_order
        self.times_in_order = times_in_order

    def get_links(self):
        """Return a list of all Link objects in that bus route."""
        links = []
        all_times = self.times_in_order
        all_nodes = self.nodes_in_order
        nodes_num = len(all_nodes)
        shuttle_number = self.shuttle_number
        for i in range(nodes_num-1):
            start = all_nodes[i]
            end = all_nodes[i+1]
            the_time = all_times[i]
            the_link = Link(shuttle_number, start, end, the_time)
            links.append(the_link)
        last_link = Link(shuttle_number, all_nodes[nodes_num-1], all_nodes[0], all_times[nodes_num-1])
        links.append(last_link)
        return links


def main():
    # nodes stores a list of Node object
    nodes = []
    node1 = Node(1, ['5024', '5528', '3512'])
    node2 = Node(2, ['2079', '5438', '5038'])
    node3 = Node(3, ['3750', '5174', '5039'])
    node4 = Node(4, ['4134', '4135', '4136'])
    node5 = Node(5, ['2780', '5178', '498'])
    node6 = Node(6, ['6159', '6160'])
    node7 = Node(7, ['1180', '1253'])
    node8 = Node(8, ['1042'])
    node9 = Node(9, ['5940'])
    node10 = Node(10, ['5992'])
    node11 = Node(11, ['2761'])
    node12 = Node(12, ['3529'])
    node13 = Node(13, ['4123'])
    node14 = Node(14, ['2019'])
    node15 = Node(15, ['5379'])
    node16 = Node(16, ['2630'])

    nodes.append(node1)
    nodes.append(node2)
    nodes.append(node3)
    nodes.append(node4)
    nodes.append(node5)
    nodes.append(node6)
    nodes.append(node7)
    nodes.append(node8)
    nodes.append(node9)
    nodes.append(node10)
    nodes.append(node11)
    nodes.append(node12)
    nodes.append(node13)
    nodes.append(node14)
    nodes.append(node15)
    nodes.append(node16)

    

    # link1 = Link(node1, node2, 2)
    # print(link1)


    all_stop_IDs = []
    for node in nodes:
        this_stop_IDs = node.stop_IDs
        for each in this_stop_IDs:
            if each not in all_stop_IDs:
                all_stop_IDs.append(each)

    # print(all_stop_IDs)
    # print(len(all_stop_IDs)) # 28 stops in total

    bus640 = Bus('640', [node1, node2, node3, node7, node10, node6, node8], [3, 6, 1, 4, 2, 1, 7])
    bus641 = Bus('641', [node14, node12, node3], [5, 8, 8])
    bus642 = Bus('642', [node1, node13, node5, node4, node7, node15, node2], [3, 5, 15, 1, 1, 2, 3])
    bus656 = Bus('656', [node16, node2], [10, float('inf')])
    bus663 = Bus('663', [node9, node6, node5], [1, 1, float('inf')])
    bus672 = Bus('672', [node12, node11, node4, node3], [4, 3, 1, float('inf')])

    all_buses = [bus640, bus641, bus642, bus656, bus663, bus672]

    all_links = []
    for bus in all_buses:
        links = bus.get_links()
        for link in links:
            all_links.append(link)
    # for each in all_links:
        # print(each)
    # print(len(all_links)) # 26 links in total of all buses

    my_graph = Graph(nodes, all_links)
    my_graph.get_time_matrix()
    
    try:
        total_time = 0
        start_node = int(input("Enter the starting node number: "))
        end_node = int(input("Enter the ending node number: "))
        if start_node < 1 or start_node > len(nodes) or end_node < 1 or end_node > len(nodes):
            print("Invalid node numbers. Please enter numbers between 1 and", len(nodes))
            return
        
        edges = my_graph.edges_matrix[start_node-1][end_node-1]
        for edge in edges:
            bus_to_take = None
            for bus in all_buses:
                links_of_this_bus = bus.get_links()
                for each_link in links_of_this_bus:
                    if (each_link.starting_node == edge.starting_node and 
                        each_link.ending_node == edge.ending_node and 
                        each_link.time == edge.time):
                        bus_to_take = each_link.shuttle_number
                        break
                if bus_to_take is not None:
                    break
        
            if bus_to_take is not None:
                print(str(edge) + ' bus' + str(bus_to_take))
                total_time += edge.time
            else:
                print(str(edge) + ' no bus found')
            
        print(f'Minimum time from node {start_node} to {end_node} is: {total_time} minutes.')
    except ValueError:
        print("Invalid input. Please enter valid integers for node numbers.")



if __name__ == '__main__':
    main()
    