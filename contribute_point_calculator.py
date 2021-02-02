import os, datetime, pickle
from collections import defaultdict

class point_calculator:
    def __init__(self):
        self.parsed_logs = []
        with open('problems_info', 'rb') as f:
            self.problems_info = pickle.load(f)

    def parse_git_log(self):
        git_logs = os.popen("git log --pretty=format:\"# %cn | %cd\" --name-status --reverse").read()
        cur_committer = ""
        cur_time = ""
        for log in git_logs.split('\n'):
            if not log: continue
            if log[0] == "#":
                commitor, time = log.split(' | ')
                cur_committer = commitor[2:]
                t = datetime.datetime.strptime(time[:-6], "%a %b %d %H:%M:%S %Y")
                cur_time = str(t)
            else:
                stat, file = log.split()
                if "solutions/" not in file:
                    continue
                if stat == "A":
                    self.parsed_logs.append((cur_committer, cur_time, file))
                elif stat == "D":
                    for i in range(len(self.parsed_logs)):
                        if self.parsed_logs[i][-1] == file:
                            self.parsed_logs.pop(i)
                            break

    def print_logs(self):
        for committer, time, file in self.parsed_logs:
            print(committer, time, file)

    def event1(self):
        dic = defaultdict(set)
        for committer, time, _ in self.parsed_logs:
            dic[committer].add(time.split()[0])
        participants = list(dic.keys())
        participants.sort(key=lambda x: len(dic[x]), reverse=True)
        print("[event1] 가장 꾸준히 기여한 사람")
        for participant in participants:
            print(participant, ":", len(dic[participant]), "points")

    def event2(self):
        dic = defaultdict(int)
        vst = set()
        for committer, time, file in self.parsed_logs:
            _, number, name = file.split('/')
            fmt = name.split('.')[1]
            if fmt == "c":
                fmt = "cpp"
            fullname = number + "." + fmt
            if fullname not in vst:
                vst.add(fullname)
                dic[committer] += 1
        participants = list(dic.keys())
        participants.sort(key=lambda x: dic[x], reverse=True)
        print("[event2] 모든 난이도에 가장 많이 기여한 사람")
        for participant in participants:
            print(participant, ":", dic[participant], "points")

    def event3(self):
        dic = defaultdict(int)
        vst = set()
        for committer, time, file in self.parsed_logs:
            _, number, name = file.split('/')
            if self.problems_info[int(number)]['Difficulty'] == "Easy":
                continue
            fmt = name.split('.')[1]
            if fmt == "c":
                fmt = "cpp"
            fullname = number + "." + fmt
            if fullname not in vst:
                vst.add(fullname)
                dic[committer] += 1
        participants = list(dic.keys())
        participants.sort(key=lambda x: dic[x], reverse=True)
        print("[event3] Medium, Hard 난이도에 가장 많이 기여한 사람")
        for participant in participants:
            print(participant, ":", dic[participant], "points")


if __name__ == "__main__":
    calculator = point_calculator()
    calculator.parse_git_log()

    calculator.event1()
    print()
    calculator.event2()
    print()
    calculator.event3()