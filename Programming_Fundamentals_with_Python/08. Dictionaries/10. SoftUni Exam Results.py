class JudgeStats:
    def __init__(self):
        self.users = {}
        self.submissions = {}

    def new_submission(self, user, lang, pts):
        if user not in self.users:
            self.users[user] = pts
        else:
            if self.users[user] < pts:
                self.users[user] = pts

        if lang not in self.submissions:
            self.submissions[lang] = 1
        else:
            self.submissions[lang] += 1

    def ban(self, user):
        self.users.pop(user)

    def status(self):
        print('Results:')
        for student, pts in dict(sorted(self.users.items(), key=lambda x: (-x[1], x[0]))).items():
            print(f'{student} | {pts}')

        print('Submissions:')
        for language, total_subm in dict(sorted(self.submissions.items(), key=lambda x: (-x[1], x[0]))).items():
            print(f'{language} - {total_subm}')


judge_statistics = JudgeStats()

submission = input()
while 'exam finished' not in submission:
    submission = submission.split('-')
    if len(submission) == 2:
        judge_statistics.ban(submission[0])
    else:
        username, lang, points = submission
        judge_statistics.new_submission(username, lang, int(points))

    submission = input()

judge_statistics.status()
