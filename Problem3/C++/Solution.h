class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {

        std::unordered_map<char, char> substringMap;
        int longestSubstring = 0;
        int windowEnd = 0;

        // Loop through each char in test string
        for (int i = 0; i < s.length(); i++) {

            // Starts at current loop index, keeps extending until a repeat char occurs
            windowEnd = i;

            // Loop through each string in current window, adding each unique char to map
            while (windowEnd < s.length()) {

                // Ensure current char has 0 matches in the map
                if (substringMap.count(s[windowEnd]) != 1) 
                {
                    // Get current char, add it to hash map, increment the windowEnd
                    char current = s[windowEnd];
                    substringMap[current] = current;
                    windowEnd++;
                }
                // As soon as a character in the current window repeats, break out of the interior loop
                else
                    break;
            }

            // If the current map size is longer than the previous longest substring, update the total count
            if (substringMap.size() > longestSubstring)
                longestSubstring = substringMap.size();

            // Clear the hash map and reset the end position
            substringMap.clear();
            windowEnd = 0;

        }

        // Return longest string of un-repeated chars
        return longestSubstring;
    }
};