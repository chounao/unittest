# coding=utf-8
from framework.send_email import *
from framework.testreport import *


if __name__ == "__main__":
    runner, fp, fileName = testreport()
    runner.run(all_case())
    fp.close()
    # sendemail(fileName)
