// PA1 (fall 2026) Python skeleton code
//
// This file shows how to read and parse the input, which is provided via
// standard input

import java.util.*;

class Edge {
	public int available_capacity, total_capacity;
	public String start_node, end_node;

	Edge(Scanner stdin) {
		start_node = stdin.next();
		end_node = stdin.next();
		available_capacity = stdin.nextInt();
		total_capacity = stdin.nextInt();
	}

	public String toString() {
		return "('" + start_node + "', '" + end_node + "', " + available_capacity +
			", " + total_capacity + ")";
	}
}

public class PA1 {
	static ArrayList<String> nodes = new ArrayList<String>();
	static ArrayList<Edge> edges = new ArrayList<Edge>();
	static String start_node, end_node;

	public static void main (String[] args) {
		Scanner stdin = new Scanner(System.in);
		Set<String> nodeset = new HashSet<String>();
		int num_edges = stdin.nextInt();
		start_node = stdin.next();
		end_node = stdin.next();
		for ( int i = 0; i < num_edges; i++ ) {
			Edge e = new Edge(stdin);
			nodeset.add(e.start_node);
			nodeset.add(e.end_node);
			edges.add(e);
		}
		nodes.addAll(nodeset);

		// REMOVE THESE LINES BEFORE SUBMISSION
		// any extra output will cause the program to be marked incorrect
		System.out.println("Start node is " + start_node + ", end node is " + end_node);
		System.out.println("The list of " + nodes.size() + " nodes: " + nodes);
		System.out.println("The list of " + edges.size() + " edges: " + edges);
	}
}
