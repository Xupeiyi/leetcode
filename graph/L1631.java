import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.List;



public class L1631 {

    public static List<int[]> findAdjacents(int nRows, int nCols, int x, int y){
        ArrayList<int[]> adjacents = new ArrayList<>();

        for (int[] coord: new int[][] {{x-1, y}, {x+1, y}, {x, y-1}, {x, y+1}}){
            int newX = coord[0];
            int newY = coord[1];
            if ((0 <= newX && newX < nRows) && (0 <= newY && newY < nCols)){
                adjacents.add(coord);
            }
        }
        return adjacents;
    }

    public static int minimumEffortPath(int[][] heights) {
        int nRows = heights.length;
        int nCols = heights[0].length;

        // dp table
        int[][] shortest = new int[nRows][nCols];
        for (int[] row : shortest){
            Arrays.fill(row, Integer.MAX_VALUE);
        }
        shortest[0][0] = 0;

        // priority queue
        class Distance {
            int x;
            int y;
            int toStart; // distance to start
            public Distance(int x, int y, int toStart){
                this.x = x;
                this.y = y;
                this.toStart = toStart;
            }
        };
        PriorityQueue<Distance> queue = new PriorityQueue<>(
            (dist1, dist2) -> {
                return dist1.toStart - dist2.toStart;
            }
        );
        queue.offer(new Distance(0, 0, 0));

        // bfs
        while (!queue.isEmpty()){
            Distance dist = queue.poll();

            // if there already exists shorter path, continue
            if (shortest[dist.x][dist.y] < dist.toStart){
                continue;
            }

            // load adjacent nodes to the queue
            for (int[] adjacent:findAdjacents(nRows, nCols, dist.x, dist.y)){
                int x = adjacent[0], y = adjacent[1];

                // see if the path (start -> ...-> (dist.x, dist.y) -> adjacent) will be shorter
                int weight = Math.abs(heights[x][y] - heights[dist.x][dist.y]);
                int adjacentToStart = Math.max(shortest[dist.x][dist.y], weight);

                // if it is shorter, update shortest and add to queue
                if (adjacentToStart < shortest[x][y]) {
                    shortest[x][y] = adjacentToStart;
                    queue.offer(new Distance(x, y, adjacentToStart));
                }
            }
        }

        return shortest[nRows-1][nCols-1];
    }

    public static void main(String[] args) {
        int[][] heights = {
            {1, 1, 1},
            {3, 8, 1},
            {5, 3, 1}
        };
        int ans = minimumEffortPath(heights);
        System.out.println(ans);
    }
   
}
