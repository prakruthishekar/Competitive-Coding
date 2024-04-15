
import java.util.Arrays;
public class MinimumFlips {
    public static int minimumFlips(String target) {
        // Start with the assumption that the initial character is '0'.
        char lastChar = '0';
        int flips = 0;

        for (int i = 0; i < target.length(); i++) {
            // Only when the current character is different from the last flipped character
            // we need to perform a flip.
            if (target.charAt(i) != lastChar) {
                flips++;
                // Update the last flipped character to the current one
                lastChar = target.charAt(i);
            }
        }

        return flips;
    }

    public static void main(String[] args) {
        String target = "1010";
        int minFlips = minimumFlips(target);
        System.out.println("Minimum flips required: " + minFlips); // Output should still be 3
    }
}
