class Solution(object):

    def graph_step(self, graph_road, now, target, walk_path= []):

        path_= walk_path[:]
        path_ += [now]

        if now == target:
            return [path_]

        elif not now in graph_road:
            return []

        result_= []

        for s in graph_road[now]:
            if s in walk_path:
                continue

            tmp_result= self.graph_step(graph_road, s, target, path_)

            result_ += tmp_result

        return result_


    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """

        graph_road= {}

        for idx, val in enumerate(graph):
            if val == []:
                continue
            graph_road[idx]= val



        return self.graph_step(graph_road, 0, len(graph)-1)
