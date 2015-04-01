import subprocess, traceback

from models import Commit, Metrics

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
	entities = commit.get_entities_by_commit(commit)		

	c = command + commit.snapshot
	changed_files_list = subprocess.check_output(c, shell=True).split('\n')		
	for file_path in changed_files_list:
		if '.java' in file_path:
			try:
				#gets old file from repo
				c = 'git -C "'+repo_path+'" checkout '+commit.snapshot+' ' + file_path
				subprocess.check_output(c, shell=True)									
				file = repo_path + '/' + file_path
				
				#execute java files
				c = 'java -classpath "'+asm_path+';'+commons_path+';'+jaxen_path+';'+jcommander_path+';'+pmd_path+';'+source_path+'" br.ufal.sapiens.refactoring.metrics.pmd.PMDRun ' + file
				metrics = subprocess.check_output(c, shell=True).split(' (')[-1].replace(')\r\n', '').split(', ')				
				
				#insert values on database							
				entity_file = file_path.replace('.java', '').replace('.', '/')
				for entity in entities:
					if entity in entity_file:
						if len(metrics) > 1:						
							metric, created = Metrics.objects.get_or_create(commit_obj=commit, entity_name=file_path, atfd=int(metrics[0].split('=')[-1]), tcc=float(metrics[2].split('=')[-1]), wmc=int(metrics[1].split('=')[-1]))														
							print created
						break
				
				#gets back newest version of file
				c = 'git -C "'+repo_path+'" checkout -- '+file_path		
				subprocess.check_output(c, shell=True)
			except:
				print ''
				print traceback.format_exc().splitlines()[-1]