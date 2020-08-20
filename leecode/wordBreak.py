from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
            给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

            说明：

            拆分时可以重复使用字典中的单词。
            你可以假设字典中没有重复的单词。
            示例 1：

            输入: s = "leetcode", wordDict = ["leet", "code"]
            输出: true
            解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
            示例 2：

            输入: s = "applepenapple", wordDict = ["apple", "pen"]
            输出: true
            解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
                 注意你可以重复使用字典中的单词。
            示例 3：

            输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
            输出: false

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/word-break
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not s  or not wordDict:
            return False
        pos = [False] * (len(s)+1)
        for l in range(len(s)):
            if l == 0 or pos[l]:
                for r in range(l+1,len(s)+1):
                    print(s[l:r])
                    if s[l:r] in wordDict:
                        
                        pos[r] = True
        
        return pos[-1]

    def _wordBreak_eg(self, s: str, wordDict: List[str]) -> bool:
        Start_dict = {}
        for word in wordDict:
            if word[0] not in Start_dict:
                Start_dict[word[0]] = [word,]
            else:
                Start_dict[word[0]].append(word)
        
        # for k in Start_dict.keys():
        #     list_k = copy.deepcopy(Start_dict[k])
        #     len_list_k = [(i, len(word)) for i, word in enumerate(list_k)]
        #     len_list_k.sort(key=itemgetter(1))
        #     Start_dict[k] = [list_k[item[0]] for item in len_list_k[::-1]]
        #     print(Start_dict[k] )
        
        tag = [True] * (len(s) + 1)

        def inner(remain: str, start: int):
            if len(remain) == start:
                return True
            if remain[start] in Start_dict:
                for w in Start_dict[remain[start]]:
                    if len(w) <= (len(remain) - start) and tag[start + len(w)] and remain[start:start + len(w)] == w:
                        if inner(remain, start + len(w)):
                            return True
                        else:
                            tag[start + len(w)] = False

            return False

        return inner(s, 0)
