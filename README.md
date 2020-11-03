# git-conceal
Github secrets detector

## To add to your Github Repository:
### In your pre-commit hook, add:

git diff --name-only --diff-filter=d --staged > dir/to/base/folder/files.txt

tar cfvz ../../..(some number of ../ then folder of project name) project.tar

docker run -v dir/to/tar/tarfile:/app << docker image name>> 
