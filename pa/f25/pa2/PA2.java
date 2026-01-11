// PA2.java skeleton code
import java.util.*;
import java.io.*;

public class PA2 {

    // object for each usage period
    static class Period {
        int left, right, height;
        String deviceName;

        Period(String deviceName, int left, int right, int height) {
            this.deviceName = deviceName;
            this.left = left;
            this.right = right;
            this.height = height;
        }

        public String toString(){
            return (deviceName + " " + left + " " + right + " " + height);
        }
    }

    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        List<String> names = new ArrayList<>();
        List<Period> periods = new ArrayList<>();

        //Read in d and c
        int d = scanner.nextInt();
        int u = scanner.nextInt();
        scanner.nextLine();

        /* Read in the names */
        for(int i=0; i<d; i++){
            names.add(scanner.nextLine());
        }

        // Read input
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine().trim();
            if (line.isEmpty()) continue;

            String[] parts = line.split("\\s+");
            if (parts.length != 4) continue;

            String name = parts[0];
            int left = Integer.parseInt(parts[1]);
            int right = Integer.parseInt(parts[2]);
            int height = Integer.parseInt(parts[3]);

            periods.add(new Period(name, left, right, height));
        }


        /* SOLUTION (AT LEAST PART OF IT) GOES HERE */


        /* Print input back to you. Make sure to delete this */
        System.out.println(d + " " + u);
        for(String name : names) System.out.println(name);
        for(Period period : periods) System.out.println(period);


    }
}
