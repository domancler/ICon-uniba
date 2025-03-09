import matplotlib.pyplot as plt


class SearcherGUI(object):
    def __init__(self, SearchClass, problem, fontsize=10,
                 colors={'selected':'red', 'neighbors':'blue', 'frontier':'green', 'goal': 'yellow'},
                 show_costs=True):
        self.problem = problem
        self.searcher = SearchClass(problem)
        self.problem.fontsize = fontsize
        self.colors = colors
        self.problem.show_costs = show_costs
        self.quitting = False

        fig, self.ax = plt.subplots()
        plt.ion() # interactive
        self.ax.set_axis_off()
        plt.subplots_adjust(bottom=0.15)
        step_butt = Button(plt.axes([0.1, 0.02, 0.2, 0.05]), "step")
        step_butt.on_clicked(self.step)
        fine_butt = Button(plt.axes([0.4, 0.02, 0.2, 0.05]), "fine step")
        fine_butt.on_clicked(self.finestep)
        auto_butt = Button(plt.axes([0.7, 0.02, 0.2, 0.05]), "auto search")
        auto_butt.on_clicked(self.autosearch)
        fig.canvas.mpl_connect('close_event', self.window_closed)
        self.ax.text(0.85, 0, '\n'.join(self.colors[a]+": "+a for a in self.colors))
        self.problem.show_graph(self.ax, node_color='white')
        self.problem.show_node(self.ax, self.problem.start, self.colors['frontier'])
        for node in self.problem.nodes:
            if self.problem.is_goal(node):
                self.problem.show_node(self.ax, node, self.colors['goal'])
        plt.show()
        self.click = 7 # bigger than any display!
        self.searcher.display(self.display)
        try:
            while self.searcher.frontier:
                path = self.searcher.search()
        except ExitToPython:
            print("GUI closed")
        else:
            print("No more solutions")

    def display(self, level, *args, **nargs):
        if self.quitting:
            raise ExitToPython()
        if level <= self.click: #step
            print(*args, **nargs)
            self.ax.set_title(f"Expanding: {self.searcher.path}", fontsize=self.problem.fontsize)
            if level == 1:
                self.show_frontier(self.colors['frontier'])
                self.show_path(self.colors['selected'])
                self.ax.set_title(f"Solution found: {self.searcher.path}", fontsize=self.problem.fontsize)
            elif level == 2: # what should be shown if node in multiple?
                self.show_frontier(self.colors['frontier'])
                self.show_path(self.colors['selected'])
                self.show_neighbors(self.colors['neighbors'])
            elif level == 3:
                self.show_frontier(self.colors['frontier'])
                self.show_path(self.colors['selected'])
            elif level == 4:
                self.show_frontier(self.colors['frontier'])

            # wait for a button click
            self.click = 0
            plt.draw()
            while self.click == 0 and not self.quitting:
                plt.pause(0.1)
            if self.quitting:
                raise ExitToPython()
            # undo coloring:
            self.ax.set_title("")
            self.show_frontier('while')
            self.show_neighbors('white')
            path_show: self.searcher.path
            while path_show.arc:
                self.problem.show_arc(self.ax, path_show.arc, 'black')
                self.problem.show_node(self.ax, path_show.end(), 'white')
                path_show = path_show.initial
            self.problem.show_node(self.ax, path_show.end(), 'white')
            if self.problem.is_goal(self.searcher.path.end()):
                self.problem.show_node(self.ax, self.searcher.path.end(), self.colors['goals'])
            plt.draw()

    def show_frontier(self, color):
        for path in self.searcher.frontier:
            self.problem.show_node(self.ax, path.end(), color)

    def show_path(self, color):
        """color selected path"""
        path_show = self.searcher.path
        while path_show.arc:
            self.problem.show_arc(self.ax, path_show.arc, color)
            self.problem.show_node(self.ax, path_show.end(), color)
            path_show = path_show.initial
        self.problem.show_node(self.ax, path_show.end(), color)

    def show_neighbors(self, color):
        for neigh in self.problem.neighbors(self.searcher.path.end()):
            self.problem.show_node(self.ax, neigh.to_node, color)

    def auto(self, event):
        self.click = 1
    def step(self, event):
        self.click = 2
    def finestep(self, event):
        self.click = 3
    def windows_closed(self, event):
        self.quitting = True


class ExitToPython(Exception):
    pass


# to demonstrate depth-first search:
# sdfs = SearcherGUI(Searcher, searchExample.tree_graph)

# delivery graph examples:
# sh = SearcherGUI(Searcher, searchExample.simp_delivery_graph)
# sha = SearcherGUI(AStarSearcher, searchExample.simp_delivery_graph)
# shac = SearcherGUI(AStarSearcher, searchExample.cyclic_simp_delivery_graph)
# shm = SearcherGUI(SearcherMPP, searchExample.cyclic_simp_delivery_graph)
# shb = SearcherGUI(DF_branch_and_bound, searchExample.simp_delivery_graph)

# The following is AI:FCA figure 3.15, and is useful to show branch&bound:
# shbt = SearcherGUI(DF_branch_and_bound, searchExample.tree_graph)
if __name__ == "__main__":
    print("Try e.g.: SearcherGUI(Searcher,searchExample.simp_delivery_graph)")
