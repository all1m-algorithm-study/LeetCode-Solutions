import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Solution {
    private String gen_fizzBuzz(int v) {
        if (v % 3 == 0 && v % 5 == 0) {
            return "FizzBuzz";
        } else if (v % 3 == 0) {
            return "Fizz";
        } else if (v % 5 == 0) {
            return "Buzz";
        } else {
            return Integer.toString(v);
        }
    }

    public List<String> fizzBuzz(int n) {
        return IntStream.range(1, n + 1)
                .mapToObj(this::gen_fizzBuzz)
                .collect(Collectors.toList());
    }
}