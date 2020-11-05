# git-conceal
This application is a Github secrets detector. It runs a check for various regex patterns and high entropy strings. On commit, this scan will run and print the secrets that were detected, The user is then prompted to see if they want to continue with the commit.

### To add this scan to your repository, add the following commands to your pre-commit hook.
NOTE: You pre-commit hook is likely in the file path .git/hooks/pre-commit

```shell
#!/bin/sh
git diff --name-only --diff-filter=d --staged > files.txt
tar cfvz project.tar ../<< PROJECT_FOLDER_NAME >>
docker pull sydneyward/git-conceal:latest
docker run -v "$(pwd)/project.tar":/app/project.tar sydneyward/git-conceal:latest project.tar << PROJECT_FOLDER_NAME >>
rm -f files.txt project.tar
exec 0< /dev/tty
read -p "Would you like to proceed with the commit? [y|anything else] " response
if [ "$response" != "y" ]; then
  echo "Commit aborted."
  exit 1
fi
```


### Contributers
* Sydney Ward
* Reagan Davis
* Divya Gubba
* Anton Joseph
* Matthew Geise
* Prathyusha Thiruvuri
* Akhil Gangidi
