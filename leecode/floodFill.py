class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。

        给你一个坐标 (sr, sc) 表示图像渲染开始的像素值（行 ，列）和一个新的颜色值 newColor，让你重新上色这幅图像。

        为了完成上色工作，从初始坐标开始，记录初始坐标的上下左右四个方向上像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他们对应四个方向上像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为新的颜色值。

        最后返回经过上色渲染后的图像。

        示例 1:

        输入: 
        image = [[1,1,1],[1,1,0],[1,0,1]]
        sr = 1, sc = 1, newColor = 2
        输出: [[2,2,2],[2,2,0],[2,0,1]]
        解析: 
        在图像的正中间，(坐标(sr,sc)=(1,1)),
        在路径上所有符合条件的像素点的颜色都被更改成2。
        注意，右下角的像素没有更改为2，
        因为它不是在上下左右四个方向上与初始点相连的像素点。
        注意:

        image 和 image[0] 的长度在范围 [1, 50] 内。
        给出的初始点将满足 0 <= sr < image.length 和 0 <= sc < image[0].length。
        image[i][j] 和 newColor 表示的颜色值在范围 [0, 65535]内。

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/flood-fill
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        pass

    def _floodFill(self, image: list, sr: int, sc: int, newColor: int) -> list:
        if len(image) ==1:
            if image[sr][sc] and image[sr][sc] != newColor:
                image[sr][sc] = newColor
            return image  
         
        def fill():
            pass
        def is_valiid(images,x,y):
            return x >=0 and y >= 0 and x < len(image) and y< len(images[x])

        def iter_fill(images,srs,scs,newColors,color):
            if not is_valiid(images,srs,scs):
                return 
            if images[srs][scs] != color:
                return 
            if images[srs][scs] == -1:
                return 
            images[srs][scs] = -1

            #self.iter_fill(images,srs-1,scs-1,newColors)
            iter_fill(images,srs-1,scs,newColors,color)
            #self.iter_fill(images,srs-1,scs+1,newColors)
            iter_fill(images,srs,scs-1,newColors,color)
            iter_fill(images,srs,scs+1,newColors,color)
            #self.iter_fill(images,srs+1,scs+1,newColors)
            iter_fill(images,srs+1,scs,newColors,color)
            #self.iter_fill(images,srs+1,scs-1,newColors)
            images[srs][scs] = newColor
            return 

        return iter_fill(image,sr,sc,newColor,image[sr][sc])

    def _floodFill(self, images: list, sr: int, sc: int, newColor: int) -> list:
        n_rows = len(images)
        n_cols = len(images[0])
        old_color = images[sr][sc]

        visited = set()

        def dfs(i0, j0):
            images[i0][j0] = newColor
            neighbors = (
                (i, j) for i, j in ((i0 - 1, j0), (i0 + 1, j0), (i0, j0 - 1), (i0, j0 + 1))
                if 0 <= i < n_rows and 0 <= j < n_cols and images[i][j] == old_color
            )
            for i, j in neighbors:
                if (i, j) not in visited:
                    visited.add((i, j))
                    dfs(i, j)

        visited.add((sr, sc))
        dfs(sr, sc)
        return images
    


