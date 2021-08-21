class Maze():
    def __init__(self, m):
        self.map = m
        self.width = len(m[0])
        self.height = len(m)
    
    def build_reachable_score(self, start_x, start_y):
        initial_map = [[None for x in range(self.width)] for y in range(self.height)]
        initial_map[start_x][start_y] = 1
        
        q = [(start_x, start_y)]
        while q:
            cur_x, cur_y = q.pop(0)
            for i in [(1,0),(-1, 0), (0, -1), (0,1)]:
                n_x, n_y = cur_x + i[0], cur_y + i[1]
                if 0 <= n_x < self.height and 0 <= n_y < self.width:
                    if initial_map[n_x][n_y] is None:
                        initial_map[n_x][n_y] = initial_map[cur_x][cur_y] + 1
                        if self.map[n_x][n_y] == 1:
                            continue
                        q.append((n_x,n_y))
        return initial_map
def solution(map):
    maze = Maze(map)
    toward_maze = maze.build_reachable_score(0,0)
    forward_maze = maze.build_reachable_score(maze.height - 1,maze.width - 1)
    min_length = float('inf')
    #! first coordinator always height - important here

    for i in range(maze.height):
        for j in range(maze.width):
            if toward_maze[i][j] and forward_maze[i][j]:
                min_length = min(toward_maze[i][j] + forward_maze[i][j] - 1, min_length)
    return min_length