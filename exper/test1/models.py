# -*- coding: utf-8 -*-
from django.db import models
import pygit2
from pygit2 import Repository
# 测试用的用户类，用于用户与 git 的交互；包含 userId, working_directory
class user(models.Model):
    userId = models.CharField(max_length=30, primary_key=True)
    working_directory = models.CharField(max_length=90)
    def __unicode__(self):
        return self.working_directory

# 以下是测试代码，负责git端的通信和互操作
# 创建 git 目录
def _createDir_(dir_name):
    local_dir = '/home/bob/WorkSpace/' + dir_name
    print("Hello,", local_dir)
    pygit2.init_repository(local_dir, False)
# 显示最新的提交记录
def _show_HEAD_commit_(dir):
    repo = Repository(dir)
    commit = repo[repo.head.target]
    commit.message
# 加载查看工作目录
def _check_(dir):
    repo = Repository(dir + '.git')
    print("Path to the git repository is:", repo.path)
    if not repo.is_bare:
        print("Working directory of the repository is", repo.workdir)
    return repo
# git log 查看git日志
def _log_(dir):
    repo = _check_(dir)
    last = repo[repo.head.target]
    for commit in repo.walk(last.id, pygit2.GIT_SORT_TIME):
        print(commit.message)
# 创建新文件
# def _new_(dir,wenjian)
def __(dir)

# Create your models here.
