import java.util.List;
import java.util.LinkedList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Collections;

public class L743 {
    public static List<int[]>[] buildGraph(int[][] edges, int nVertices){
        // graph: an array of linked list. 
        List<int[]>[] graph = new LinkedList[nVertices+1];
        for (int i = 1; i < nVertices+1; i++) {
            graph[i] = new LinkedList<>();
        }
        for (int[] edge: edges){
            int from = edge[0];
            int to = edge[1];
            int weight = edge[2];
            graph[from].add(new int[]{to, weight});
        }

        return graph;
    }

    public static Integer[] dijkstra(int start, List<int[]>[] graph, int nVertices){
        // a table to record the shortest distance to start
        Integer [] shortest = new Integer[nVertices+1];
        Arrays.fill(shortest, Integer.MAX_VALUE);
        shortest[start] = 0;

        // a priority queue to store the potential shortest distances
        class Distance {
            int id;
            int toStart; // distance to start
            public Distance(int id, int toStart){
                this.id = id;
                this.toStart = toStart;
            }
        };
        PriorityQueue<Distance> queue = new PriorityQueue<>(
            (dist1, dist2) -> {
                return dist1.toStart - dist2.toStart;
            }
        );
        queue.offer(new Distance(start, 0));

        while (!queue.isEmpty()){
            Distance dist = queue.poll();

            // if there is already a known shorter path, continue
            if (shortest[dist.id] < dist.toStart){
                continue;
            }

            // load adjacent nodes' distances to the queue
            for (int[] edge:graph[dist.id]){
                int adjacent = edge[0];
                int weight = edge[1];

                // see if the path (start -> ...-> dist.id -> adjacent) will be shorter
                int adjacentToStart = shortest[dist.id] + weight;

                // if it is, update shortest path and put adjacent into queue
                if (adjacentToStart < shortest[adjacent]){
                    shortest[adjacent] = adjacentToStart;
                    queue.offer(new Distance(adjacent, adjacentToStart));
                } 
            }
        }

        return shortest;
    }

    public static int networkDelayTime(int[][] times, int n, int k) {
        List<int[]>[] network = buildGraph(times, n); // [[[to1, weight1],..]..]
        Integer[] shortest = dijkstra(k, network, n);
        int maxDelay = Collections.max(Arrays.asList(shortest).subList(1, n+1));
        return (maxDelay != Integer.MAX_VALUE)?maxDelay:-1;
    }

    public static void main(String[] args) {
        int[][] times = {{2,1,1},{2,3,1},{3,4,1}};
        int ans = networkDelayTime(times, 4, 2);
        System.out.println(ans);
    }
}
