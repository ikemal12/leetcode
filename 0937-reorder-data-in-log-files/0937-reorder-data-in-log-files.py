class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_log, digit_log = [], []
        for i, log in enumerate(logs):
            vals = log.split(" ")
            if vals[1][0].isdigit():
                digit_log.append(log)
            else:
                letter_log.append([" ".join(vals[1:]), vals[0], i])
        
        res = []
        for log in sorted(letter_log):
            res.append(logs[log[2]])
        return res + digit_log