class Solution {
public:
    double findMedianSortedArrays(std::vector<int>& nums1, std::vector<int>& nums2) {
        std::cout << "test" << std::endl; 

        return 0;
        
		// Solution with built-in functions that doesn't satisfy O(m + n) runtime complexity
		/*nums1.insert( nums1.end(), nums2.begin(), nums2.end() );
        sort(nums1.begin(), nums1.end());

        if(nums1.size() % 2 == 0) 
        {
            float answer =  (((float) nums1[nums1.size() / 2 ] + (float) nums1[(nums1.size() / 2) - 1]) / 2);
            return answer;
        } else 
        {
            return nums1[nums1.size() / 2];
        }

        return 0;*/
    }
};
