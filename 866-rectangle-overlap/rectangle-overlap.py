class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        #rec1[x1,y1,x2,y2]=[0,1,2,3]
        #rec2[x1,y1,x2,y2]=[0,1,2,3]
        
        if rec1[2]<=rec2[0] or rec2[2] <= rec1[0]:
            return False
        if rec1[3]<=rec2[1] or rec2[3]<=rec1[1]:
            return False
        
        return True