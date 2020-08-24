class MinStack:

    def __init__(self):
        """
        设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

        push(x) —— 将元素 x 推入栈中。
        pop() —— 删除栈顶的元素。
        top() —— 获取栈顶元素。
        getMin() —— 检索栈中的最小元素。
         

        示例:

        输入：
        ["MinStack","push","push","push","getMin","pop","top","getMin"]
        [[],[-2],[0],[-3],[],[],[],[]]

        输出：
        [null,null,null,null,-3,null,0,-2]

        解释：
        MinStack minStack = new MinStack();
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-3);
        minStack.getMin();   --> 返回 -3.
        minStack.pop();
        minStack.top();      --> 返回 0.
        minStack.getMin();   --> 返回 -2.

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/min-stack
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        initialize your data structure here.
        """
        self.stack = []


    def push(self, x: int) -> None:

        self.stack.append(x)

    def pop(self) -> None:
        return self.stack.pop()


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return min( self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.minStack=[]


    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.minStack)==0:
            self.minStack.append(x)
        else:
            if self.minStack[-1]>=x:
                self.minStack.append(x)

    def pop(self) -> None:
        if self.minStack[-1] == self.stack[-1]:
            self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]