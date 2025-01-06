class Solution {
    public String mergeAlternately(String word1, String word2) {
        int word1length = word1.length();
        int word2length = word2.length();
        int j = 0;
        char[] result = new char[word1length + word2length];
        for (int i = 0; i < word1length || i < word2length; i++) {
            if (i < word1length)
                result[j++] = word1.charAt(i);
            if (i < word2length)
                result[j++] = word2.charAt(i);
        }
        return new String(result);
    }
}