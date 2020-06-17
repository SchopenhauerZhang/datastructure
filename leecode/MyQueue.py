class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        使用栈实现队列的下列操作：

        push(x) -- 将一个元素放入队列的尾部。
        pop() -- 从队列首部移除元素。
        peek() -- 返回队列首部的元素。
        empty() -- 返回队列是否为空。
         

        示例:

        MyQueue queue = new MyQueue();

        queue.push(1);
        queue.push(2);  
        queue.peek();  // 返回 1
        queue.pop();   // 返回 1
        queue.empty(); // 返回 false

        来源：力扣（LeetCode）
        链接：https://leetcode-cn.com/problems/implement-queue-using-stacks
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        self.stack_a = list()
        self.stack_b = list()


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if len(self.stack_b):
            
            while len(self.stack_b):
                data = self.stack_b.pop()
                self.stack_a.append(data)
                

        self.stack_a.append(x)



    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if  len(self.stack_b):
            return self.stack_b.pop()
        if  len(self.stack_a):
            
            while len(self.stack_a):
                data = self.stack_a.pop()
                self.stack_b.append(data)
            
        return self.stack_b.pop() if len(self.stack_b) else False
            




    def peek(self) -> int:
        """
        Get the front element.
        """
        if  len(self.stack_b):
            return self.stack_b.pop()
        if  len(self.stack_a):
        
            while len(self.stack_a):
                data = self.stack_a.pop()
                self.stack_b.append(data)
                
        data = self.stack_b.pop()
        self.stack_b.append(data)
        return data


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return  not len(self.stack_a) and not len(self.stack_b)



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()