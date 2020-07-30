Command	Description
git log [--oneline]	
git status	
git show	
git show-ref	
git checkout	
git pull origin master | [beanch_name]	

git commit push origin master	
git branch	Shows branches
git tag | Git tag -l	Shows all tags. Tags can be used to show software releases
git show-branch --all	
gitk 	Opens visual branch helper
git checkout master	Changes to master branch
git branch header	Creates 'header' branch
git tag -a [tag_name] -m "message"	
git push origin --tags	Pushes tags to remote repository
Git push origin [master] | [branch_name]	
git tag -d [tag_name]	Removes current tag
git push origin :refs/tags/tag_name	Removes tag remotely and references
git log --all --graph --decorate --oneline	Special command to show branches in a compressed way
git config --global alias.blog "log --all --graph --decorate --oneline"	
git commit -am "commit message"	Commits and adds all files currently existing in working area
git add .	Adds all files in working area to staging area
git clone	
git log --graph	
git merge [branch_name]	
git reset --hard	
git rm	
ssh-keygen -t rsa -b 4096 -C "tu@email.com"	
eval $(ssh-agent -s)
ssh-add  ~\.ssh\id_rsa
git remote add origin <https:url>	
git remote -v	
git remote set-url origin	
git diff	
git remote add upstream [url]	For forked versions that have been rebased by my current repository
git rebase master	From a specific branch use rebase to bring changes from a branch into another
git stash | git stash pop	Saves into temporary memory WIP (Work In Progress)
git stash branch [branch_name]	Saves stashed work into a new branch
git stash drop	Removes stashed work
git clean --dry-run	Removes unnecessary files from current repository, only deleted things that can be indexed
git cherry-pick	Brings specific commit into desired branch
git commit -amend	Commits new changes to latest commit
git reflog	Visualizes everything previously done from in repository
git reset --SOFT --HARD  | git reset HEAD@{4}	Soft preserves staging area
git grep -n [word] | -c [Count]	Finds occurrences of words
git log -s "word to find in commit messages"	Displays commits whose word appears in commit message
git shortlog	
git shortlog -sn -all
git blame [file_name]	
git blame -c [file_name] [-Lxx,yy]
git [command] --help	
git branch [-r] [-a]	
