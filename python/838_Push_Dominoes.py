class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        dominoes_count = len(dominoes)

        last_push = -1
        push_label = 'None'

        finnal_state = ''
        for i in range(dominoes_count):
            now_domino = dominoes[i]
            if now_domino == '.' and push_label in ('L', 'None'):
                j = i + 1
                not_Decide = True
                while j < dominoes_count:
                    if dominoes[j] == 'R':
                        break
                    elif dominoes[j] == 'L':
                        finnal_state += 'L'
                        not_Decide = False
                        break

                    j += 1
                if not_Decide:
                    finnal_state += now_domino


            elif now_domino == '.' and push_label == 'R':
                j = i + 1
                not_Decide = True
                while j < dominoes_count:
                    if dominoes[j] == 'R':
                        finnal_state += 'R'
                        not_Decide = False
                        break
                    elif dominoes[j] == 'L':
                        right_distinct = i - last_push
                        left_distinct = j - i

                        if right_distinct > left_distinct:
                            finnal_state += 'L'
                            not_Decide = False
                            break
                        elif left_distinct > right_distinct:
                            finnal_state += 'R'
                            not_Decide = False
                            break
                        else:
                            finnal_state += '.'
                            not_Decide = False
                            break
                    j += 1

                if not_Decide:
                    finnal_state += 'R'


            else:
                finnal_state += now_domino
                last_push = i
                push_label = now_domino

        return finnal_state