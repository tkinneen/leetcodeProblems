# LeetCode Problem 207: Course Schedule
#
# There are a total of numCourses courses you have to take, labeled from 0 to 
#    numCourses - 1. You are given an array prerequisites where prerequisites[i] = 
#    [ai, bi] indicates that you must take course bi first if you want to take 
#    course ai.
#
# For example, the pair [0, 1], indicates that to take course 0 you have to first
#     take course 1. Return true if you can finish all courses. Otherwise, return 
#     false.

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Time: O(V + E) // Space: O(V + E)

        # Each course from 0 -> (n-1) will have an integer key representing it in our map
        # Use python list comprehension to initialize an empty prerequisite array for each one
        prereqMap = { i: [] for i in range(numCourses) }
        
        # Loop through the problem's prerequisites and build up the map
        for course, prerequisite in prerequisites:
            prereqMap[course].append(prerequisite)
        
        # This set behaves differently from typical graph sets.
        # We will put courses into it as we recurse into a single prerequisite progression, 
        #    and if we detect a duplicate then there is a cycle and the course can't be completed.
        # However when we've finished that check, we empty the courses up the recursion stack for 
        #    the next indepent check, because two courses could have the same prerequisite, and 
        #    if we left previous courses in the set we would see an invalid cycle.
        visitedSet = set()
        
        # 
        def dfs(course):

            # A prerequisite cycle has been detected, so all of the courses are NOT completable
            if course in visitedSet:
                return False
            
            # If the prerequisite array of the current course is empty, then it's automatically complete-able
            # This could occur naturally or because we already checked this course and emptied the array
            if prereqMap[course] == []:
                return True
            
            # This is a valid course, so add it to our visited set
            visitedSet.add(course)

            # Loop through the current course's prerequisites
            for prerequisite in prereqMap[course]:
                
                # Recurse into the next prerequisite, bubbling up any False values
                if not dfs(prerequisite):
                    return False
            
            # Each step through the recursion chain remove the current course from the visited set so we start fresh for the next course
            visitedSet.remove(course)
            
            # Because this course can be completed, empty its
            #    prerequisite array to prevent repeated future work
            prereqMap[course] = []

            return True
        
        # Because we can have two totally unconnected prerequisite graphs, we need to manually loop through 
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True