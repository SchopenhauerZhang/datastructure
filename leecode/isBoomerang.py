from typing import List
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        """
        回旋镖定义为一组三个点，这些点各不相同且不在一条直线上。

            给出平面上三个点组成的列表，判断这些点是否可以构成回旋镖。

             

            示例 1：

            输入：[[1,1],[2,3],[3,2]]
            输出：true
            示例 2：

            输入：[[1,1],[2,2],[3,3]]
            输出：fals

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/valid-boomerang
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
            三角形ABC的面积的公式:S=1/2[(x1y2-x2y1)+(x2y3-x3y2)+(x3y1-x1y3)]
        """
        x1, x2, x3 = points[0][0], points[1][0], points[2][0]
        y1, y2, y3 = points[0][1], points[1][1], points[2][1]
        
        return (x1*y2-x2*y1)+(x2*y3-x3*y2)+(x3*y1-x1*y3) != 0
    
    def _isBoomerang_eg(self, points: List[List[int]]) -> bool:
        if points[0]==points[1] or points[0]==points[2] or points[1]==points[2]:
            return False
        return (points[2][0]-points[0][0])*(points[2][1]-points[1][1])!=(points[2][0]-points[1][0])*(points[2][1]-points[0][1])
