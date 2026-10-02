// PA2 Skeleton Code
// DSA2, fall 2026

// This code will read in the input, and put the values into variables and an array.

import java.util.*;

public class PA2 {

	// this will read in the input
	public static void main(String[] args) {
		Scanner stdin = new Scanner(System.in);

		// how many test cases in the file?
		int test_cases = stdin.nextInt(); // max of 10^5 test cases per file

		for ( int i = 0; i < test_cases; i++ ) {

			// read in the data for the test case
			int m = stdin.nextInt(); // number of miles (int)
			int p = stdin.nextInt(); // number of plows (int)
			long[] times = new long[m]; // times can be longs
			for ( int j = 0; j < m; j++ )
				times[j] = stdin.nextLong();

			// print out the values read in -- this has to be deleted prior to submission!
			System.out.println(m+" "+p);
			for ( long x: times )
				System.out.print(x + " ");
			System.out.println("\n");
		}
	}

}
