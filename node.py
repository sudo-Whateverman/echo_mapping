import random


class SingleNode:
    def __init__(self, the_factory):
        self.position = {'x': random.randint(1, 100), 'y': random.randint(1, 100)}
        self.factory = the_factory
        self.id_num = self.factory.get_uuid()
        self.relative_pos_dict = {}

    def __str__(self):
        return str(self.position)

    def _calculate_propagation(self, yourpos):
        return (self.position['x'] - yourpos['x']) ** 2 + (self.position['y'] - yourpos['y']) ** 2

    def _return_pos(self):
        return self.position

    def return_uuid(self):
        return str(self.id_num)

    def send_tone(self, node_var):
        yourposition = node_var._return_pos()
        your_id = node_var.return_uuid()
        if your_id != self.id_num:
            distance_to_node = self._calculate_propagation(yourposition)
            self.relative_pos_dict[your_id] = distance_to_node
            return distance_to_node
        else:
            return 0

    def send_loud_tone(self):
        for node in self.factory.get_nodes():
            self.send_tone(node)

    def get_distances(self):
        return [{uuid_var: pos} for uuid_var, pos in self.relative_pos_dict.items()]


class MainNode(SingleNode):
    def __init__(self, the_factory):
        SingleNode.__init__(self, the_factory)
        self.position = {'x': 0, 'y': 0}
        self.factory = the_factory
        self.id_num = '0'
        self.relative_pos_dict = {}
