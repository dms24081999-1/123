import unittest
import subprocess

def test_sample_single_word():
    inf=open('in.txt','rb')
    inputdata=inf.read()
    inf.close()

    otf=open('out.txt','rb')
    outputdata=otf.read()
    otf.close()
    
    run=subprocess.Popen(["python", "run.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    grep_stdout =run.communicate(input=inputdata)[0]
    print(grep_stdout.decode())
    print(run.returncode)
    assert bytes(grep_stdout.decode(),'utf-8')==outputdata
    
    
def test_sample_single_word2():
    inf=open('in.txt','rb')
    inputdata=inf.read()
    inf.close()

    otf=open('out.txt','rb')
    outputdata=otf.read()
    otf.close()
    
    run=subprocess.Popen(["python", "run1.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    grep_stdout =run.communicate(input=inputdata)[0]
    print(grep_stdout.decode())
    print(run.returncode)
    assert bytes(grep_stdout.decode(),'utf-8')==outputdata
