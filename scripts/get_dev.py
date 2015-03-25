import subprocess

from core.models import Commit, Developer

commits = Commit.objects.all()

command = 'git --git-dir=D:/Wally/UFAL/Refactoring/git/sdk/.git --no-pager show -s --format="%aN <%aE>" '

for commit in commits:
    c = command + commit.snapshot
    author_string = subprocess.check_output(c, shell=True).strip()
    author,created = Developer.objects.get_or_create(name=author_string)
    commit.developer = author
    commit.save()