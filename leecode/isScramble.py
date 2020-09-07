class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        """
            给定一个字符串 s1，我们可以把它递归地分割成两个非空子字符串，从而将其表示为二叉树。

            下图是字符串 s1 = "great" 的一种可能的表示形式。

                great
            /    \
            gr    eat
            / \    /  \
            g   r  e   at
                    / \
                    a   t
            在扰乱这个字符串的过程中，我们可以挑选任何一个非叶节点，然后交换它的两个子节点。

            例如，如果我们挑选非叶节点 "gr" ，交换它的两个子节点，将会产生扰乱字符串 "rgeat" 。

                rgeat
            /    \
            rg    eat
            / \    /  \
            r   g  e   at
                    / \
                    a   t
            我们将 "rgeat” 称作 "great" 的一个扰乱字符串。

            同样地，如果我们继续交换节点 "eat" 和 "at" 的子节点，将会产生另一个新的扰乱字符串 "rgtae" 。

                rgtae
            /    \
            rg    tae
            / \    /  \
            r   g  ta  e
                / \
                t   a
            我们将 "rgtae” 称作 "great" 的一个扰乱字符串。

            给出两个长度相等的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。

            示例 1:

            输入: s1 = "great", s2 = "rgeat"
            输出: true
            示例 2:

            输入: s1 = "abcde", s2 = "caebd"
            输出: false

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/scramble-string
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not s1 or not s2 or s1 == s2:
            return True
        
        # s1和s2是不是互相互为全排列
        if sorted(s1) != sorted(s2):
            return False
        
        # 二分查找
        ll = len(s1)
        for i in range(1,ll):
            # 二叉树交换节点必然是节点的所有叶子节点全交换
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]):
                return True
            elif self.isScramble(s1[:i],s2[ll-i:]) and self.isScramble(s1[i:],s2[:ll-i]):
                return True

        return False
    
    def _isScramble_eg(self, s1: str, s2: str) -> bool:
        def add(d, ch):
            d[ch] = d.get(ch, 0) + 1
            if d[ch] == 0:
                del d[ch]

        def remove(d, ch):
            d[ch] = d.get(ch, 0) - 1
            if d[ch] == 0:
                del d[ch]

        def check(i, j, k, l):
            if j - i < 2:
                return True

            to_try = []
            d1 = {}
            d2 = {}
            for m in range(j - i):
                add(d1, s1[i+m])
                add(d2, s1[i+m])
                remove(d1, s2[k+m])
                remove(d2, s2[l-m])

                if len(d1) == 0:
                    to_try.append(((i, i + m, k, k + m), (i + m + 1, j, k + m + 1, l)))
                if len(d2) == 0:
                    to_try.append(((i, i + m, l - m, l), (i + m + 1, j, k, l - m - 1)))

            for _1, _2 in to_try:
                if check(*_1) and check(*_2):
                    return True
            return False

        def assume():  # check whether s1 and s2 contain the same set of characters
            if len(s1) != len(s2):
                return False

            d = {}
            for ch1, ch2 in zip(s1, s2):
                if ch1 == ch2:
                    continue
                add(d, ch1)
                remove(d, ch2)
            return len(d) == 0

        if not assume():
            return False
        n = len(s1)
        return check(0, n - 1, 0, n - 1)