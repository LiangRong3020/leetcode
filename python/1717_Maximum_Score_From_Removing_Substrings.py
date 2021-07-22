class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        score = 0
        if x >= y:
            max_s = 'ab'
            max_v = x
            min_s = 'ba'
            min_v = y
        else:
            max_s = 'ba'
            max_v = y
            min_s = 'ab'
            min_v = x
        stack_ = [s[0]]
        pre = s[0]
        for s_ in s[1:]:
            if (pre + s_) == max_s:
                score += max_v
                stack_.pop()
                pre = stack_[-1] if len(stack_) > 0 else ''
            else:
                pre = s_
                stack_.append(s_)
        if not stack_:
            return score
        new_stack_ = [stack_[0]]
        pre = stack_[0]
        for s_ in stack_[1:]:
            if (pre + s_) == min_s:
                score += min_v
                new_stack_.pop()
                pre = new_stack_[-1] if len(new_stack_) > 0 else ''
            else:
                pre = s_
                new_stack_.append(s_)
        return score
