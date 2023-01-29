class Solution {
    List<int[]>[] graph;
    boolean[] vis;
    int[] dis, prev;

    public int networkDelayTime(int[][] times, int n, int k) {
        graph = new ArrayList[n + 1];
        PriorityQueue<int[]> queue = new PriorityQueue<>((a, b) -> (a[1] - b[1]));
        // graph[0] = new ArrayList<>();
        // graph[0].add(new int[] { -2, 5 });

        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int[] arr : times) {
            int src = arr[0], end = arr[1], weight = arr[2];
            graph[src].add(new int[] { end, weight });
        }
        // Graph-array has no List at index 0=> ie never use graph[0]
        // Those edges that have no connecting nodes will show null exeption too
        // System.out.println(graph[2]);

        // Dijikstra's Algo to find all the minimum sum = Answer

        int inf = Integer.MAX_VALUE;
        int ans = 0;
        vis = new boolean[n + 1];
        dis = new int[n + 1];
        prev = new int[n + 1];
        Arrays.fill(prev,-1);
        for (int i = 0; i <= n; i++) {
            if (i != k) dis[i] = inf;
        }

        // vis[k] = true;
        queue.add(new int[] { k, 0 });

        while (!queue.isEmpty()) {
            int[] arr = queue.poll();
            int curr = arr[0], itsDis = arr[1];
             vis[curr]=true;
            if (itsDis > dis[curr]) continue;

            for (int[] node : graph[curr]) {
                int next = node[0];
                int newDistance = dis[curr] + node[1];
                if (!vis[next] && dis[next] > newDistance) {
                    // vis[next] = true;
                    prev[next] = curr;
                    dis[next] = newDistance;
                    queue.add(new int[] { next, newDistance });
                }
            }
        }

        System.out.println(Arrays.toString(dis));
        System.out.println(Arrays.toString(prev));
        for (int i = 1; i <= n; i++) {
            ans = Math.max(ans, dis[i]);
        }

        return ans == Integer.MAX_VALUE ? -1 : ans;
    }
}
