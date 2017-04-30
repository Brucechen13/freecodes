from collections import defaultdict

class Graph:
    '''
    存储输入输出之间的关联情况
    '''
    sort_key = None
    
    def __init__(self):
        self._input_of = defaultdict(set)
        self._consequence_of = defaultdict(set)
    
    def sorted(self, nodes, reverse = False):
        nodes = list(nodes)
        try:
            nodes.sort(key=sort_key, reverse = reverse)
        except TypeError:
            pass
        return nodes
    
    def add_edges(self, input_task, consequence_task):
        self._consequence_of[input_task].add(consequence_task)
        self._input_of[consequence_task].add(input_task)
    
    def remove_edges(self, input_task, consequece_task):
        self._consequence_of[input_task].remove(consequece_task)
        self._input_of[consequece_task].remoe(input_task)
        
    def input_of(self, task):
        '''
        返回输出文件关联的所有输入文件
        '''
        return self.sorted(self._input_of[task])
    
    def clear_input_of(self, task):
        '''
        清除之前加载的所有关联的输入文件
        在某个输入文件渲染完成后调用
        '''
        input_tasks = self._inputs_of.pop(task, ())
        for input_task in input_tasks:
            self._consequences_of[input_task].remove(task)      
    
    def tasks(self):
        return self.sorted(set(self._input_of).union(self._consequence_of))
    
    def edges(self):
        """
        返回所有关联的值
        """
        return [(a, b) for a in self.sorted(self._consequences_of)
                    for b in self.sorted(self._consequences_of[a])]    
    
    def immediate_consequences_of(self, task):
        """
        返回task对应的所有输出
        """
        return self.sorted(self._consequences_of[task])

    def recursive_consequences_of(self, tasks, include=False):
        """
        使用生成器迭代所有关联的task
        """
        def visit(task):
            visited.add(task)
            consequences = self._consequences_of[task]
            for consequence in self.sorted(consequences, reverse=True):
                if consequence not in visited:
                    yield from visit(consequence)
                    yield consequence

        def generate_consequences_backwards():
            for task in self.sorted(tasks, reverse=True):
                yield from visit(task)
                if include:
                    yield task

        visited = set()
        return list(generate_consequences_backwards())[::-1]
