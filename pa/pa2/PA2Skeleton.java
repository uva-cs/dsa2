// DSA2 PA2 skeleton code

// This code shows how to read in the input in the format described at:
// https://uva-cs.github.io/dsa2/pa/pa2/

import java.util.Scanner;

public class PA2Skeleton {
	public static void main(String[] args) {
		Scanner stdin = new Scanner(System.in);
		int cases = stdin.nextInt(); // how many test cases are in the file
		for ( int i = 0; i < cases; i++ ) {
			int result; // how many test cases are in the file
			int size = stdin.nextInt(); // how many not-so-ordered books are in this particular test case
			int[] shelf = new int[size];
			for ( int j = 0; j < size; j++ )
				shelf[j] = stdin.nextInt();

			// The shelf of not-so-ordered book numbers is in the `shelf` variable

			// Do something here.

			System.out.println(result); // the only output is one integer printed per test case
		}
		
	}
}