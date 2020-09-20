class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        """
            你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度。若值为0则表示水域。由垂直、水平或对角连接的水域为池塘。池塘的大小是指相连接的水域的个数。编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。

            示例：

            输入：
            [
            [0,2,1,0],
            [0,1,0,1],
            [1,1,0,1],
            [0,1,0,1]
            ]
            输出： [1,2,4]
            提示：

            0 < len(land) <= 1000
            0 < len(land[i]) <= 1000

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/pond-sizes-lcci
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
            超出时间限制
        """
        if not land or  (len(land) == 1 and len(land[0])==1):
            return []
        def iter_land(i,j):
            if i <0 or j < 0 or i >= _c or j >= _r:
                return 0
            if [i,j] in _used:
                return 0
            _used.append([i,j])
            if land[i][j] == 0:
                # 小心死循环
                land[i][j] = -1
                x = 1+iter_land(i-1,j)+iter_land(i-1,j-1)+iter_land(i,j-1)+iter_land(i+1,j)+iter_land(i,j+1)+iter_land(i+1,j+1)+iter_land(i-1,j+1)+iter_land(i+1,j-1)
                return x
            
            return 0

        _used = []
        _r,_c = len(land[0]),len(land)
        res = []
        for i in range(_c):
            for j in range(_r):
                x = iter_land(i,j)
                if  x != 0:
                    res.append(x)

        return sorted(res)
    
    def pondSizes_16_19_eg(self, land: List[List[int]]) -> List[int]:
        
        res =[]
        m=len(land)
        n=len(land[0])
        size=[0]
        def dfs(i,j):
            if i<0 or j<0 or i>m-1 or j>n-1:
                return
            if land[i][j]!=0:
                return
            if land[i][j]==0:
                land[i][j]=-1
                size[0]+=1
                dfs(i-1,j)
                dfs(i,j-1)
                dfs(i+1,j)
                dfs(i,j+1)
                dfs(i-1,j-1)
                dfs(i+1,j+1)
                dfs(i-1,j+1)
                dfs(i+1,j-1)
        for i in range(m):
            for j in range(n):
                if land[i][j]==0:
                    dfs(i,j)
                    res.append(size[0])
                    size[0]=0
        res.sort()
        return res
    
    def pondSizes_eg(self, land: List[List[int]]) -> List[int]:
        d = {}
        L = 0
        con = []
        m, n = len(land), len(land[0])
        for ii in range(m):
            for jj in range(n):
                if land[ii][jj]==0:
                    if jj>0 and land[ii][jj-1]==0:
                        d[(ii, jj)] = d[(ii, jj-1)]
                    if ii>0 and jj>0 and land[ii-1][jj-1]==0:
                        if ((ii, jj) in d):
                            if d[(ii,jj)]<d[(ii-1,jj-1)]:
                                con.append([d[(ii,jj)],d[(ii-1,jj-1)]])
                            elif d[(ii,jj)]>d[(ii-1,jj-1)]:
                                con.append([d[(ii-1,jj-1)],d[(ii,jj)]])
                        else:
                            d[(ii, jj)] = d[(ii-1, jj-1)]
                    if ii>0 and land[ii-1][jj]==0:
                        if ((ii, jj) in d):
                                if d[(ii,jj)]<d[(ii-1,jj)]:
                                    con.append([d[(ii,jj)],d[(ii-1,jj)]])
                                elif d[(ii,jj)]<d[(ii-1,jj)]:
                                    con.append([d[(ii-1,jj)],d[(ii,jj)]])
                        else:
                            d[(ii, jj)] = d[(ii-1, jj)]
                    if ii>0 and jj+1<n and land[ii-1][jj+1]==0:
                        if ((ii, jj) in d):
                            if d[(ii,jj)]<d[(ii-1,jj+1)]:
                                con.append([d[(ii,jj)],d[(ii-1,jj+1)]])
                            elif d[(ii,jj)]>d[(ii-1,jj+1)]:
                                con.append([d[(ii-1,jj+1)],d[(ii,jj)]])
                        else:
                            d[(ii, jj)] = d[(ii-1, jj+1)]
                    if (ii,jj) not in d:
                        d[(ii, jj)] = L
                        L = L + 1
        con.sort()
        d3 = {}
        ind = 0
        for one in con:
            if one[0] in d3:
                if one[1] not in d3:
                    d3[one[1]] = d3[one[0]]
            elif (one[1] not in d3):
                d3[one[0]] = ind
                d3[one[1]] = d3[one[0]]
                ind += 1
            else:
                d3[one[0]] = d3[one[1]]
        for ii in range(L):
            if ii not in d3:
                d3[ii] = ind
                ind += 1
        ans = [0]*ind
        for ii in d:
            ans[d3[d[ii]]] += 1
        ans.sort()
        return ans
