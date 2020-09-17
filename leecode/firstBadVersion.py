# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):

        """
        你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

        假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

        你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

        示例:

        给定 n = 5，并且 version = 4 是第一个错误的版本。

        调用 isBadVersion(3) -> false
        调用 isBadVersion(5) -> true
        调用 isBadVersion(4) -> true

        所以，4 是第一个错误的版本。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/first-bad-version
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        :type n: int
        :rtype: int
        """
        if n == 1 or isBadVersion(1):
            return 1
        if n == 2:
            return 1 if isBadVersion(1) else 2
        l,r=1,n
        mid = int((l+r)//2)
        l_i = isBadVersion(mid)
        r_i = isBadVersion(mid+1)
        while not (l_i == False and r_i == True ):
        
            
            if l_i == False and r_i == False:
                l = mid
                mid = (mid+r)//2
            if l_i == True and r_i == True:
                r = mid
                mid = (mid+l) //2
    
            l_i = isBadVersion(mid)
            r_i = isBadVersion(mid+1)
        return mid+1
        
    def firstBadVersion_eg(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l <= r:
            m = l+(r-l) // 2
            if isBadVersion(m) and not isBadVersion(m - 1):
                return m
            elif isBadVersion(m):
                r = m - 1
            else:
                l = m + 1
            
