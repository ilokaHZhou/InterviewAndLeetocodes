import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public String reverseVowels(String s) {
        Set<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));

        char[] charArray = s.toCharArray();
        int i = 0;
        int j = charArray.length - 1;

        while (i < j) {
            if (!vowels.contains(charArray[i]))
                i++;
            else if (!vowels.contains(charArray[j]))
                j--;
            else {
                char temp = charArray[i];
                charArray[i] = charArray[j];
                charArray[j] = temp;
                i++;
                j--;
            }
        }
        return new String(charArray);
        
    }
}