#!/bin/sh

# pip install kaggle
# pip install requests
export KAGGLE_USERNAME=hogehoge
export KAGGLE_KEY=fugafuga

if [ ! -e /Users/{user_name}/{project_name}/result ]; then
  echo "This is your first execution."
  kaggle kernels list --competition home-credit-default-risk --sort-by 'dateCreated' > /Users/{user_name}/{project_name}/result
  echo "Now, first result can be gained."
else
  mv /Users/{user_name}/{project_name}/result /Users/{user_name}/{project_name}/pastResult
  kaggle kernels list --competition home-credit-default-risk --sort-by 'dateCreated' > /Users/{user_name}/{project_name}/result
  python /Users/{user_name}/{project_name}/index.py
fi
