from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
            输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。

             

            示例 1：

            输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
            输出：true
            解释：我们可以按以下顺序执行：
            push(1), push(2), push(3), push(4), pop() -> 4,
            push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
            示例 2：

            输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
            输出：false
            解释：1 不能在 2 之前弹出。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        # 压栈
        pushed_bk = []
        ll = len(pushed)
        r = 0
        for i in range(ll):
            pushed_bk.append(pushed.pop(0))
            while pushed_bk and pushed_bk[-1] == popped[r]:
                pushed_bk.pop()
                r += 1

        return True if not pushed_bk else False

    def _validateStackSequences_eg(self, pushed: List[int], popped: List[int]) -> bool:
        stack, i = [], 0
        for n in pushed:
            stack.append(n)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return not stack
    
    def _validateStackSequences_946(self, pushed: List[int], popped: List[int]) -> bool:
        """
            给定 pushed 和 popped 两个序列，每个序列中的 值都不重复，只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，返回 true；否则，返回 false 。

             

            示例 1：

            输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
            输出：true
            解释：我们可以按以下顺序执行：
            push(1), push(2), push(3), push(4), pop() -> 4,
            push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
            示例 2：

            输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
            输出：false
            解释：1 不能在 2 之前弹出。
             

            提示：

            0 <= pushed.length == popped.length <= 1000
            0 <= pushed[i], popped[i] < 1000
            pushed 是 popped 的排列。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/validate-stack-sequences
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        # pushed 是poped的全排列
        if not pushed or not popped or len(pushed) <= 2:
            return True
        _stack = []
        _pop_index = 0
        
        for data in pushed:
            # 栈只有2种：入栈和出栈,所以判断pushed向左还是向右
            if data == popped[_pop_index]:
                # 向左，数据匹配，继续出栈
                _pop_index += 1
                while _stack and _stack[-1] == popped[_pop_index]:
                    _stack.pop()
                    _pop_index += 1

            else:
                # 向右,数据不匹配，入栈
                _stack.append(data)
        print(_stack,_pop_index)
        return not _stack and _pop_index == len(popped)
    
    def _validateStackSequences_946_eg(self, pushed: List[int], popped: List[int]) -> bool:
        actual_pop_count = 0
        stack = []
        for num in pushed:
            stack.append(num)
            while stack and actual_pop_count < len(popped) and stack[-1] == popped[actual_pop_count]:
                stack.pop()
                actual_pop_count += 1
        
        return actual_pop_count == len(popped)


