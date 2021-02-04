import os, datetime, pickle, pytz
from collections import defaultdict

class point_calculator:
    def __init__(self):
        self.parsed_logs = []
        with open('problems_info', 'rb') as f:
            self.problems_info = pickle.load(f)

    def parse_git_log(self):
        git_logs = os.popen("git log --pretty=format:\"# %an | %cd\" --name-status --reverse").read()
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

        contents = []
        contents.append("### (Event 1) 가장 꾸준히 기여한 사람")
        contents.append("| # | User Name | Points |")
        contents.append("| :---: | :---: | :---: |")
        for i, participant in enumerate(participants, 1):
            contents.append(f"| {i} | {participant} | {len(dic[participant])} |")

        return "\n".join(contents)

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

        contents = []
        contents.append("### (Event 2) 모든 난이도에 가장 많이 기여한 사람")
        contents.append("| # | User Name | Points |")
        contents.append("| :---: | :---: | :---: |")
        for i, participant in enumerate(participants, 1):
            contents.append(f"| {i} | {participant} | {dic[participant]} |")
        
        return "\n".join(contents)

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

        contents = []
        contents.append("### (Event 3) Medium, Hard 난이도에 가장 많이 기여한 사람")
        contents.append("| # | User Name | Points |")
        contents.append("| :---: | :---: | :---: |")
        for i, participant in enumerate(participants, 1):
            contents.append(f"| {i} | {participant} | {dic[participant]} |")
        
        return "\n".join(contents)


def get_current_time():
    date_format = "**%Y년 %m월 %d일 %H시 %M분**"
    now = datetime.datetime.now(pytz.timezone("Asia/Seoul"))
    return now.strftime(date_format)

def get_contents():
    calculator = point_calculator()
    calculator.parse_git_log()

    contents = []
    contents.append("## Ranking")
    contents.append(f"{get_current_time()}에 마지막으로 업데이트된 순위입니다.\n")

    contents.append(calculator.event1() + "\n")
    contents.append(calculator.event2() + "\n")
    contents.append(calculator.event3())

    return "\n".join(contents)

if __name__ == "__main__":
    print(get_contents())