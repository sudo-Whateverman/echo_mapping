import uuid
import node


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class Factory:
    def __init__(self):
        self.nodes = {}

    def create_node(self):
        node_var = node.SingleNode(self)
        self.nodes[node_var.return_uuid()] = node_var

    def create_mother_node(self):
        node_var = node.MainNode(self)
        self.nodes[node_var.return_uuid()] = node_var

    @staticmethod
    def get_uuid():
        return str(uuid.uuid4())

    def create_nodes(self, number_of_instances):
        self.create_mother_node()
        for i in range(number_of_instances):
            self.create_node()

    def get_nodes(self):
        return [node_var for uuid_num, node_var in self.nodes.items()]

    def get_nodes_number(self, number_):
        a = [node_var for uuid_num, node_var in self.nodes.items()]
        return a[:number_]

    def get_mother(self):
        for uuid_num, node_obj in self.nodes.items():
            if uuid_num == '0':
                return node_obj

