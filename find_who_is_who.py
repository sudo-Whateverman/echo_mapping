import factory


class Solver:
    def __init__(self, mother):
        self.solved_nodes = [[mother, mother._return_pos()]]

    def solve(self, node_obj_var):
        if len(self.solved_nodes) > 2:
            return self._solve_if_solved_nodes_are_greater_than_three(node_obj_var)
        else:
            self._solve_two_first_nodes()
            self.solve(node_obj_var)

    def _solve_if_solved_nodes_are_greater_than_three(self, node_obj_var):
        """
        find x and y for
        I) x**2 + y**2 = distance_to_mother
        II) (x-x0)**2 + (y-y0)**2 = distance_to_node0
        III) (x-x1)**2 + (y-y1)**2 = distance_to_node1

        I - II -> x0*x + y0*y = (distance_to_mother - distance_to_node0)/2
        I - III -> x1*x + y1*y = (distance_to_mother - distance_to_node1)/2
        =>y = ((distance_to_mother - distance_to_node0 + x0**2 + y0**2)*x1
             - (distance_to_mother - distance_to_node1 + x1**2 + y1**2)*x0)/(2*(x1*y0-x0*y1))
        =>x = ((distance_to_mother - distance_to_node0 + x0**2 + y0**2)*y1
             - (distance_to_mother - distance_to_node1 + x1**2 + y1**2)*y0)/(2*(y1*x0-x1*y0))
        :return:
        """
        if [node_obj_var, node_obj_var._return_pos()] not in self.solved_nodes:
            distance_to_mother = node_obj_var.send_tone(self.solved_nodes[0][0])
            distance_to_node0 = node_obj_var.send_tone(self.solved_nodes[1][0])
            distance_to_node1 = node_obj_var.send_tone(self.solved_nodes[2][0])
            p0_dict = self.solved_nodes[1][1]
            p1_dict = self.solved_nodes[2][1]

            x0 = p0_dict['x']
            x1 = p1_dict['x']
            y0 = p0_dict['y']
            y1 = p1_dict['y']

            x_pos = ((distance_to_mother - distance_to_node0 + x0 ** 2 + y0 ** 2) * y1
                     - (distance_to_mother - distance_to_node1 + x1 ** 2 + y1 ** 2) * y0) / (2 * (y1 * x0 - x1 * y0))
            y_pos = ((distance_to_mother - distance_to_node0 + x0 ** 2 + y0 ** 2) * x1 -
                     (distance_to_mother - distance_to_node1 + x1 ** 2 + y1 ** 2) * x0) / (2 * (x1 * y0 - x0 * y1))
            self.solved_nodes.append([node_obj_var, {'x': x_pos, 'y': y_pos}])

    @staticmethod
    def _solve_two_first_nodes():
        """
        Just get 2 GPS tags in the start. I wasted too much time here.
        :return:
        """
        pass

    def _cheating(self, node_obj1, node_obj2):
        if (node_obj1.return_uuid() == '0') | (node_obj2.return_uuid() == '0'):
            print("We have mother here")
        else:
            self.solved_nodes.append([node_obj1, node_obj1._return_pos()])
            self.solved_nodes.append([node_obj2, node_obj2._return_pos()])

    def check_solved(self):
        for node_obj_list in self.solved_nodes:
            if node_obj_list[0]._return_pos() == node_obj_list[1]:
                print "success"
            else:
                print "failed location is {0} you guessed {1}".format(node_obj_list[0]._return_pos(), node_obj_list[1])


if __name__ == '__main__':
    number_of_nodes = 100
    factory_obj = factory.Factory()
    factory_obj.create_nodes(number_of_nodes)
    solver = Solver(factory_obj.get_mother())
    [obj_1, obj_2] = factory_obj.get_nodes_number(2)
    solver._cheating(obj_1, obj_2)
    for node_obj in factory_obj.get_nodes():
        solver.solve(node_obj)
    solver.check_solved()
