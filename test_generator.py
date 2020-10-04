import unittest
import subprocess

def test_sample_single_word():
    run=subprocess.Popen(["python3", "run.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    grep_stdout =run.communicate(input=b'one\ntwo\nthree\nfour\n')[0]
    print(grep_stdout.decode())
    print(run.returncode)
    assert 0==1
