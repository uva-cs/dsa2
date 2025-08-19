// PA1 Skeleton Code
// DSA2, spring 2025

// This code will read in the input, and put the values into lists.  It is up
// to you to properly represent this as a graph -- this code only reads in the
// input properly.


import java.util.*;

class Node implements Comparable<Node> {
	// a node in the graph
	public int x, y;
	public Node(int _x, int _y) {
		x=_x;y=_y;
	}
    public int compareTo(Node other) {
        if (this.x != other.x) return Integer.compare(this.x, other.x);
        return Integer.compare(this.y, other.y);
    }
}

class Edge implements Comparable<Edge> {
	// The edge goes from (x1,y1) to (x2,y2), and has weight (cost) w
	// Note that the edges are bi-directional, and this only represents it in one direction
	public int x1, y1, x2, y2, w;
	public Edge(int _x1, int _y1, int _x2, int _y2, int _w) {
		x1=_x1; y1=_y1; x2=_x2; y2=_y2; w=_w;
	}
    public int compareTo(Edge other) {
        if (this.x1 != other.x1) return Integer.compare(this.x1, other.x1);
        if (this.y1 != other.y1) return Integer.compare(this.y1, other.y1);
        if (this.x2 != other.x2) return Integer.compare(this.x2, other.x2);
        if (this.y2 != other.y2) return Integer.compare(this.y2, other.y2);
        return Integer.compare(this.w, other.w);
    }
}

class TestCase {
	// a test case, which is two nodes
	public Node from, to;
	public TestCase(int x1, int y1, int x2, int y2) {
		from = new Node(x1,y1);
		to = new Node(x2,y2);
	}
}


public class PA1 {
	static int s, m, h;
	static ArrayList<Edge> side_road_edges, main_road_edges, highway_edges;
	static ArrayList<Node> side_road_nodes, main_road_nodes, highway_nodes, all_nodes;


	// output() function -- given a list of coordinates (as an ArrayList of
	// Node objects) and the(integer) distance, this function will output the
	// result in the correct format for the auto-grader
	public static void output(ArrayList<Node> path, int dist) {
		System.out.println(dist);
		System.out.println(path.size());
		for ( Node n: path )
			System.out.println(n.x + " " + n.y);
		System.out.println();
	}


	// this will read in the input
	static void read_input() {
		Scanner stdin = new Scanner(System.in);

		// Read in the values for the number of side roads, main roads, and highways
		s = stdin.nextInt();
		m = stdin.nextInt();
		h = stdin.nextInt();

		// Read in the side road edges
		side_road_edges = new ArrayList<Edge>();
		for ( int i = 0; i < s; i++ )
			side_road_edges.add(new Edge(stdin.nextInt(),stdin.nextInt(),stdin.nextInt(),stdin.nextInt(),stdin.nextInt()));
		Collections.sort(side_road_edges);

		// Read in the main road edges
		main_road_edges = new ArrayList<Edge>();
		for ( int i = 0; i < m; i++ )
			main_road_edges.add(new Edge(stdin.nextInt(),stdin.nextInt(),stdin.nextInt(),stdin.nextInt(),stdin.nextInt()));
		Collections.sort(main_road_edges);

		// Read in the highway edges
		highway_edges = new ArrayList<Edge>();
		for ( int i = 0; i < h; i++ )
			highway_edges.add(new Edge(stdin.nextInt(),stdin.nextInt(),stdin.nextInt(),stdin.nextInt(),stdin.nextInt()));
		Collections.sort(highway_edges);

		// Read in how many test cases there will be
		int num_test_cases = stdin.nextInt();

		// Read in each test case
		ArrayList<TestCase> test_cases = new ArrayList<TestCase>();
		for ( int i = 0; i < num_test_cases; i++ )
			test_cases.add(new TestCase(stdin.nextInt(),stdin.nextInt(),stdin.nextInt(),stdin.nextInt()));

		// Generate the lists of the nodes of the various graphs
		Set<Node> side_road_nodes_set = new HashSet<Node>();
		Set<Node> main_road_nodes_set = new HashSet<Node>();
		Set<Node> highway_nodes_set = new HashSet<Node>();
		Set<Node> all_nodes_set = new HashSet<Node>();
		for ( Edge e: side_road_edges ) {
			side_road_nodes_set.add(new Node(e.x1,e.y1));
			side_road_nodes_set.add(new Node(e.x2,e.y2));
			all_nodes_set.add(new Node(e.x1,e.y1));
			all_nodes_set.add(new Node(e.x2,e.y2));
		}
		for ( Edge e: main_road_edges ) {
			main_road_nodes_set.add(new Node(e.x1,e.y1));
			main_road_nodes_set.add(new Node(e.x2,e.y2));
			all_nodes_set.add(new Node(e.x1,e.y1));
			all_nodes_set.add(new Node(e.x2,e.y2));
		}
		for ( Edge e: highway_edges ) {
			highway_nodes_set.add(new Node(e.x1,e.y1));
			highway_nodes_set.add(new Node(e.x2,e.y2));
			all_nodes_set.add(new Node(e.x1,e.y1));
			all_nodes_set.add(new Node(e.x2,e.y2));
		}
		side_road_nodes = new ArrayList<Node>(side_road_nodes_set);
		Collections.sort(side_road_nodes);
		main_road_nodes = new ArrayList<Node>(main_road_nodes_set);
		Collections.sort(main_road_nodes);
		highway_nodes = new ArrayList<Node>(highway_nodes_set);
		Collections.sort(highway_nodes);
		all_nodes = new ArrayList<Node>(all_nodes_set);
		Collections.sort(all_nodes);
	}


	/*
	 * At this point, the data structures are as follows.  You may not need
	 * all of these in your code.
	 *
	 * - ints `s`, `m`, and `h` contain the (integer) number of side road
	 *   edges, main road edges, and highway edges, respectively
	 *
	 * - Edge data structures:
	 *   - `side_road_edges` contains a list of Edge objects that represent
	 *     the edges of the side roads.  All values are integers.  This list
	 *     is sorted.  Note that this only has the edges in one direction,
	 *     but they are bi-directional edges.
	 *   - `main_road_edges` has the edges for the main roads, in the same
	 *     form as the edges for the side roads
	 *   - `highway_edges` has the edges for the main roads, in the same form
	 *     as the edges for the side roads
	 *
	 * - Node data structures:
	 *   - `side_road_nodes` contain all the nodes that connect to a side road
	 *     as an ArrayList of Nodes; this list is sorted
	 *   - `main_road_nodes` contain all the nodes that connect to a main road
	 *     as an ArrayList of Nodes; this list is sorted
	 *   - `highway_nodes` contain all the nodes that connect to a highway as
	 *     an ArrayList of Nodes; this list is sorted
	 *   - `all_nodes` contain all the nodes in the graph as an ArrayList of
	 *     Nodes; this list is sorted
	 *
	 * - Test case data structures:
	 *   - `num_test_cases` is how many test cases there are
	 *   - `test_cases` is the test cases themselves, as a list of TestCase
	 *     objects.  The tuples in this list are in the order they occur in
	 *     the input file.
	 */


	public static void main(String[] args) {
		read_input();
		System.out.println("Hello, world");

		// YOUR CODE HERE (or called from here)
	}

}
