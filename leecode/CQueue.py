class CQueue:

    def __init__(self):
        """
            用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

             

            示例 1：

            输入：
            ["CQueue","appendTail","deleteHead","deleteHead"]
            [[],[3],[],[]]
            输出：[null,null,3,-1]
            示例 2：

            输入：
            ["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
            [[],[],[5],[2],[],[]]
            输出：[null,-1,null,null,5,2]

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        self._pre = []
        self._next = []


    def appendTail(self, value: int) -> None:
        if not self._next:
            self._pre.append(value)
        else:
            while self._next:
                self._pre.append(self._next.pop())
            self._pre.append(value)

    def deleteHead(self) -> int:
        if not self._pre and not self._next:
            return -1
        if not self._pre and  self._next:
            return self._next.pop()
        while self._pre:
            self._next.append(self._pre.pop())
        return self._next.pop()



    def __init__eg(self):
        self.queue = collections.deque()

    def appendTail_eg(self, value: int) -> None:
        self.queue.append(value)

    def deleteHead_eg(self) -> int:
        return self.queue.popleft() if self.queue else -1


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()