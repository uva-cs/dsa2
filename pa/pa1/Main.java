/**
 * CS3100 - Fall 2024 - Programming Assignment 1
 *********************************
 * Collaboration Policy: You may discuss the problem and the overall
 * strategy with up to 4 other students, but you MUST list those people
 * in your submission under collaborators.  You may NOT share code,
 * look at others' code, or help others debug their code.  Please read
 * the syllabus carefully around coding.  Do not seek published or online
 * solutions for any assignments. If you use any published or online resources
 * (which may not include solutions) when completing this assignment, be sure to
 * cite them. Do not submit a solution that you are unable to explain orally to a
 * member of the course staff.
 **************************************/

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        int numCities = 0;
        int start = 0;
        int end = 0;
        List<String> capacities = new ArrayList<>();
        List<String> loads = new ArrayList<>();
        int i = 0;
        try (BufferedReader br = new BufferedReader(new FileReader("example.txt"))) {
            String line;
            boolean capacitiesDone = false;
            while ((line = br.readLine()) != null) {
                if (i == 0)
                    numCities = Integer.parseInt(line);
                else if (i == 1)
                    start = Integer.parseInt(line);
                else if (i == 2)
                    end = Integer.parseInt(line);
                else if (line.equals("---"))
                    capacitiesDone = true;
                else if (!capacitiesDone)
                    capacities.add(line.trim());
                else
                    loads.add(line.trim());
                i++;
            }

            // Call method and print the result
            Long startT = System.currentTimeMillis();
            FedUps f = new FedUps();
            List<Integer> output = f.compute(numCities, capacities, loads, start, end);
            Long endT = System.currentTimeMillis();
            for (Integer city : output)
                System.out.println(city);
            System.out.println("time: " + ((endT - startT) / 1000.0));
        } catch (Exception e) {
            e.printStackTrace();
            System.err.println("Error occurred when reading file");
        }
    }
}
