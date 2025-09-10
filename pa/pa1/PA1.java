// PA1 Skeleton Code
// DSA2, fall 2025

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
		System.out.println("Hello, world");

		Scanner stdin = new Scanner(System.in);
		int test_cases = stdin.nextInt();

		for ( int i = 0; i < test_cases; i++ ) {
			// read in the weights for the different pathogen loads
			int wt = stdin.nextInt(), wf = stdin.nextInt(), wb = stdin.nextInt(), wc = stdin.nextInt();
			// read in the number of vertices and edges
			int v = stdin.nextInt(), e = stdin.nextInt();
			// read in the edges
			ArrayList<Pair> edges = new ArrayList<Pair>();
			for ( int j = 0; j < e; j++ )
				edges.add(new Pair(stdin.next(), stdin.next()));
			// read in the start node and node to print the pathogen load for
			String source = stdin.next(), node = stdin.next();

			/** At this point, the data strcutres are as follows:
			 * 
			 * The integers wt, wf, wb, and wc are the weights of the edges
			 * for tree, forward, back, and cross edges
			 * 
			 * The number of vertices and edges are in the integers v and e
			 * 
			 * The edges themselves are in an ArrayList of Pairs; printing it
			 * out might look like:
			 * [A->B, B->C, C->D, D->E, A->C, A->F, E->C, E->D, F->C, F->D]
			 * 
			 * The start node is in the String source, the node to print the
			 * pathogen load is in the String node
			 */

			// REMOVE THESE LINES from your final version -- this is just to
			// show the data read in
			System.out.println("\ntest case " + i + ":");
			System.out.println("weights (tree, forward, back, and cross): " + wt+" "+wf+" "+wb+" "+wc);
			System.out.println(v + " vertices and " + e + " edges");
			System.out.println("the edges themselves: " + edges);
			System.out.println("start node: " + source + ", node to print the pathogen load for: " + node);

		}

		// YOUR CODE HERE (or called from here)
	}

}
