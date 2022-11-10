import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.PriorityQueue;

public class L1514 {

    public static List<double[]>[] buildGraph(int[][] edges, double[] succProb, int nVertices) {
        List<double[]>[] graph = new LinkedList[nVertices];
        for (int i = 0; i < nVertices; i++) {
            graph[i] = new LinkedList<>();
        }

        for (int i = 0; i < edges.length; i++){
            int[] edge = edges[i];
            double weight = Math.log(succProb[i]);
            
            // add two edges
            int from = edge[0];
            int to = edge[1];
            graph[from].add(new double[]{(double)to, weight});
            graph[to].add(new double[]{(double)from, weight});
        }

        return graph;
    }

    public static double maxProbability(int n, int[][] edges, double[] succProb, int start, int end) {
        List<double[]>[] graph = buildGraph(edges, succProb, n);

        double[] highestProb = new double[n];
        Arrays.fill(highestProb, -Double.MAX_VALUE);
        highestProb[start] = 0; // log(1) = 0

        class LogProb {
            int id;  // id of node
            double fromStart;
            LogProb(int id, double logProbFromStart){
                this.id = id;
                this.fromStart = logProbFromStart;
            }
        }
        // put node with higher probability to the front
        PriorityQueue<LogProb> queue = new PriorityQueue<>(
            (prob1, prob2) -> {
                return Double.compare(prob2.fromStart, prob1.fromStart);
            }
        );
        queue.offer(new LogProb(start, 0));
        
        while (!queue.isEmpty()) {
            LogProb prob = queue.poll();
            
            // if the probability to end is already the highest in the queue, return
            // as there will be no other ways to increase it
            if (prob.id == end){
                return Math.exp(highestProb[prob.id]);
            }

            // if a higher probabiltiy is already known, continue 
            if (prob.fromStart <  highestProb[prob.id]) {
                continue;
            }

            for (double[] adjacent: graph[prob.id]){
                int id = (int)adjacent[0];
                double weight = adjacent[1];

                // see if start -> prob.id -> id creates a more probable path
                double newProb = highestProb[prob.id] + weight;
                if (newProb > highestProb[id]) {
                    highestProb[id] = newProb;
                    queue.offer(new LogProb(id, newProb));
                }
            }
        }
        return 0;
    }

    public static void main(String[] args) {
        int n = 3;
        int[][] graph = {{0, 1}, {1, 2}, {0, 2}};
        double[] succProb = {0.5, 0.5, 0.2};
        int start = 0;
        int end = 2;

        double ans = maxProbability(n, graph, succProb, start, end);
        System.out.println(ans);
    }

}