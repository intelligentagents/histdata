import subprocess

from models import Commit

commits = Commit.objects.all()

repo_path = 'D:/Wally/UFAL/Refactoring/git/sdk'

asm_path = 'D:/Wally/UFAL/Refactoring/git/smell-platform/lib/asm-5.0_BETA.jar'
commons_path = 'D:/Wally/UFAL/Refactoring/git/smell-platform/lib/commons-io-2.2.jar'
jaxen_path = 'D:/Wally/UFAL/Refactoring/git/smell-platform/lib/jaxen-1.1.1.jar'
jcommander_path = 'D:/Wally/UFAL/Refactoring/git/smell-platform/lib/jcommander-1.27.jar'
pmd_path = 'D:/Wally/UFAL/Refactoring/git/smell-platform/lib/pmd-5.1.2.jar'

source_path = 'D:/Wally/UFAL/Refactoring/git/smell-platform/src'

command = 'git -C "'+repo_path+'" diff-tree --no-commit-id --name-only -r '

#compile java files
c = 'javac -cp "'+ pmd_path +'" '+ source_path +'/br/ufal/sapiens/refactoring/metrics/pmd/GodClassRule.java'
subprocess.check_output(c, shell=True)
c = 'javac -cp "'+ pmd_path +'" '+ source_path +'/br/ufal/sapiens/refactoring/metrics/pmd/PMDRun.java'
subprocess.check_output(c, shell=True)

for commit in commits:	
	c = command + commit.snapshot
	changed_files_list = subprocess.check_output(c, shell=True).split('\n')
	for file_path in changed_files_list:
		if '.java' in file_path:
			#gets old file from repo
			c = 'git -C "'+repo_path+'" checkout '+commit.snapshot+' ' + file_path
			subprocess.check_output(c, shell=True)									
			file = repo_path + '/' + file_path
			
			#execute java files
			c = 'java -classpath "'+asm_path+';'+commons_path+';'+jaxen_path+';'+jcommander_path+';'+pmd_path+';'+source_path+'" br.ufal.sapiens.refactoring.metrics.pmd.PMDRun ' + file			
			subprocess.check_output(c, shell=True)
			
			#insert values on database
			
			#gets back newest version of file
			c = 'git -C "'+repo_path+'" checkout -- '+file_path		
			subprocess.check_output(c, shell=True)
		break
	break