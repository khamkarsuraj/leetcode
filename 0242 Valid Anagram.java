class Solution {
    public boolean isAnagram(String s, String t) {
        //Approach 2: Using counter
        int[] counter = new int[26];

        for(int i=0; i<s.length(); i++) {
            counter[s.charAt(i) - 'a']++;
        }

        for(int i=0; i<t.length(); i++) {
            counter[t.charAt(i) - 'a']--;
        }

        for(int i=0; i<26; i++) {
            if (counter[i] != 0) {
                return false;
            }
        }

        return true;

        //Approach 1: Using HashMap
    }
}
