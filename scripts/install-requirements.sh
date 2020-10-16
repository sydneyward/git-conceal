path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P)
cd $path

hooks=$( ls hooks | tr " " "\n")
for hook in $hooks
do
  chmod +x hooks/$hook
  ln -f hooks/$hook ../.git/hooks/$hook
done
