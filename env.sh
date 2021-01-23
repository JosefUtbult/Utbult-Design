export FLASK_APP="`pwd`/app.py"
export FLASK_ENV=development
export SEND_FILE_MAX_AGE_DEFAULT=0

ln -sfn "`pwd`/categories/" "`pwd`/templates/"
ln -sfn "`pwd`/categories/" "`pwd`/static/"
