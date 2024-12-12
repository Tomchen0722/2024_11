#這範例必需使用.py檔案執行，不可使用.ipynb
#建立多個程序
import multiprocessing
import os


def do_this(what):
    whoami(what)


def whoami(what):
    print("Process %s says: %s" % (os.getpid(), what))


if __name__ == "__main__":
    whoami("I'm the main program")
    for n in range(4):
        p = multiprocessing.Process(target=do_this, args=("I'm function %s" % n,))
        p.start()