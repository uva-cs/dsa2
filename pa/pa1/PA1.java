// PA1 Skeleton Code
// DSA2, spring 2026

// This code will read in the input, and put the values into lists.  It is up
// to you to properly represent this as a graph -- this code only reads in the
// input properly.


import java.util.*;

class Pair {
	public String s, t;
	Pair(String s, String t) { this.s=s; this.t=t; }
	public String toString() { return s + "->" + t; }
}

public class PA1 {

	public static void main(String[] args) {

		Scanner stdin = new Scanner(System.in);
		int test_cases = stdin.nextInt();

		for ( int i = 0; i < test_cases; i++ ) {
			
			// read in n, e, and q
			int n = stdin.nextInt();
			int e = stdin.nextInt();
			int q = stdin.nextInt();

			// create the list of nodes
			ArrayList<String> nodes = new ArrayList<String>();
			for ( int j = 0; j < n; j++ )
				nodes.add("v"+j);

			// read in the edges
			ArrayList<Pair> edges = new ArrayList<Pair>();
			for ( int j = 0; j < e; j++ )
				edges.add(new Pair(stdin.next(),stdin.next()));

			// read in the queries
			ArrayList<Pair> queries = new ArrayList<Pair>();
			for ( int j = 0; j < e; j++ )
				queries.add(new Pair(stdin.next(),stdin.next()));

			System.out.println("test case " + i + ":");
			System.out.println("there are " + n + " nodes, " + e + " edges, and " + q + " queries");
			System.out.println("the nodes are: " + nodes);
			System.out.println("the edges are: " + edges);
			System.out.println("the queries are: " + queries);
			System.out.println("");

			// YOUR CODE HERE (or called from here)

		}
	}
}
