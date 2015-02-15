#! /usr/bin/python

import os, sys, glob, time, subprocess, signal
import popen2

subdirectories = ['first', 'second', 'third', 'fourth', 'fifth']
formats = {'first':'line', 'second':'line', 'third':'file', 'fourth':'file', 'fifth':'file'}# if a program has single liner input and output, we put all test cases in single file. Otherwise, we have a file for test and associated file with results

class ExperimentError(Exception):
    def __init__(self, command, output):
        self.command = command
        limit = 10000
        if(len(output) > limit):
          self.output = output[:limit/2] + "\n\n...TRUNCATED...\n\n" + output[-limit/2:]
        else:
          self.output = output
    def __str__(self):
        return "ExperimentError:" + `self.command`

def run_command(command_string, input_string="", max_lines=0, verbose=False, echo=True, throw_exception=True, return_valgrind_output=False, user_program=False):
    if echo:
        print "executing:", command_string
    obj = popen2.Popen4(command_string)
    output = ""
    valgrind_output = ""

    obj.tochild.write(input_string)
    obj.tochild.close()
    valgrind_prefix = "==%d==" % obj.pid
    maxSleep = 20
    if user_program: #program may have an infinite loop        
        while maxSleep>0:
            time.sleep(0.25)
            maxSleep-=1            
            if obj.poll()!=-1:
                break
        if maxSleep==0 and obj.poll()==-1:
            os.kill(obj.pid, signal.SIGKILL)
            print command_string, " taking longer than expected. Killed."
            return ""
        
    line = obj.fromchild.readline()
    while (line):
        if verbose == 1:
            print line,
        if line.startswith(valgrind_prefix):
            valgrind_output += line
        output += line
        line = obj.fromchild.readline()
    exit_status = obj.wait()

    if(max_lines != 0):
        lines = output.split("\n");
        output = string.join(lines[-max_lines:], "\n")

    if throw_exception and exit_status != 0:
        raise ExperimentError(command_string, output)

    if return_valgrind_output:
        return valgrind_output
    else:
        return output

def compare_string_file(ref_file, test_string, show_difference=False):
    test_list=test_string.split("\n")    
    fd = open(ref_file)
    i=0
    flag=True
    for line in fd:        
        if i<len(test_list):
            if line.strip()!=test_list[i].strip():            
                flag=False
        elif len(line.strip())>0:
            print "Output missing: ", line
            flag=False
        i+=1
    
    fd.close()
    while(i<len(test_list)):
        if len(test_list[i].strip())==0:
            i+=1
            continue
        print "Extra output: ", test_list[i]
        i+=1
        flag=False
    return flag

def compare_string(ref, test):
    ref = ref.strip()
    test = test.strip()

    if(ref==test):
        return True
    if(ref==test.lower()):
        print "%s and %s are in different case. Please print your output in correct case."%(ref, test)
    return False


def make_executable(dirname):
    if os.path.isfile('Makefile') or os.path.isfile('makefile'):
        run_command("make clean", verbose=False)
        run_command("make", verbose=True)
    else:
        print "No Makefile found in", dirname
        print "Please submit a Makefile to receive full grade."
        run_command("gcc -o %s *.c *.h"%(dirname), verbose=False)


def file_grade(dirname):
    print "Grading", dirname
    prevdir = os.getcwd()
    os.chdir(dirname)
    make_executable(dirname)
    if not os.path.isfile(dirname):
        print "Executable %s missing. Please check the compilation output."%(dirname)
        return
    for testfile in sorted(os.listdir(".")):
        if os.path.isdir(testfile) or not testfile.startswith("test"):
            continue
        resultfile = "result"+testfile[4:len(testfile)]
        if not os.path.isfile(resultfile):
            print "Found a test file %s. But, no associated result file."%(testfile)
            continue
        print "Found a test file %s. The output will be compared to %s."%(testfile, resultfile)
        ret = run_command("./%s %s"%(dirname, testfile), user_program=True)
        if compare_string_file(resultfile, ret, show_difference=True):
            print "The output is correct for input file %s."%(testfile) 
        else:
            print "The output is not correct for input file %s."%(testfile)
        print ""
    print ""
    os.chdir(prevdir)
    
    
def single_grade(dirname):
    print "Grading", dirname
    prevdir = os.getcwd()
    os.chdir(dirname)
    make_executable(dirname)
    if not os.path.isfile(dirname):
        print "Executable %s missing. Please check the compilation output."%(dirname)
        return
    if not os.path.isfile("test.txt"):
        print "Expecting the test cases in test.txt. Not found."
        return
    else:
        print "Using test.txt for grading."
        
    fd = open("test.txt")
    state = 0
    for line in fd:
        if state==0:
            inputline = line
            state = 1
        else:
            outputline = line
            state = 0
            ret = run_command("./%s %s"%(dirname, inputline.strip()), user_program=True)
            print "Your program generated %s. The correct answer is %s."%(ret.strip(), outputline.strip())
            if compare_string(outputline, ret):
                print "The output is correct for input %s."%(inputline.strip())	
            else:
                print "The output is not correct for input %s."%(inputline.strip())
    fd.close()    
    print ""
    os.chdir(prevdir)
    

def global_grade(dirname):
    target = len(subdirectories)
    for subdir in subdirectories:
        if not os.path.isdir(os.path.join(subdir)):
            continue        
        print subdir, " found!"
        if subdir in formats and formats[subdir]=='line':
            single_grade(subdir)
        elif subdir in formats and formats[subdir]=='file':
            file_grade(subdir)
        
            
if __name__ == '__main__':
    basepath = "pa1"   
    tarmode = False #by default check the directory
    
    if len(sys.argv)>1:        
        if sys.argv[1].strip()=='tar':
            tarmode=True    
    
    if tarmode==False:
        if not os.path.isdir(basepath):
            print "pa1 is not presnt in this directory."
            sys.exit(1)
        else:
            print "Grading the content of pa1."
            os.chdir(basepath)
            global_grade(basepath)        
    else:
        prevdir = os.getcwd()
        if not os.path.exists("pa1.tar"):
            print "Expecting pa1.tar in current directory. Current directory is %s"%(prevdir)        
            print "Please make sure you created pa1.tar in the right directory"
            sys.exit(1)
        if os.path.exists("obj_temp"):
            print "Deleting the directory obj_temp."
            run_command("rm -rf obj_temp", verbose=False)
        run_command("mkdir obj_temp", verbose=False)
        os.chdir("obj_temp")
        run_command("tar -xvf ../pa1.tar")
        if os.path.isdir("pa1"):
            os.chdir("pa1")
            global_grade("pa1")
        else:
            print "There is not directory named pa1 in pa1.tar."
            print "Please check your tar file."
        os.chdir(prevdir)
