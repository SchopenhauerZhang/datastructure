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
        
        if  len(self.stack_a):
            
            while len(self.stack_a):
                data = self.stack_a.pop()
                self.stack_b.append(data)
        if  len(self.stack_b):
            return self.stack_b.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        
        if  len(self.stack_a):
        
            while len(self.stack_a):
                data = self.stack_a.pop()
                self.stack_b.append(data)
        data = self.stack_b.pop(len(self.stack_b)-1)
        self.stack_b.append(data)
        while  len(self.stack_b):
            self.stack_a.append(self.stack_b.pop())
        
        return data


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return  not len(self.stack_a) and not len(self.stack_b)


    ###########________eg_______###############
    def __init__(self):
        self.queue_stack = []


    def push(self, x: int) -> None:

        #就是把数放在栈底就好了！
        tmp = []
        while self.queue_stack.__len__() > 0 :
            tmp.append(self.queue_stack.pop())

        self.queue_stack.append(x)

        while tmp.__len__() > 0:
            self.queue_stack.append(tmp.pop())
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.queue_stack.pop()


    def peek(self) -> int:
        return self.queue_stack[-1]
        """
        Get the front element.
        """


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.queue_stack.__len__() == 0:
            return True
        return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()