# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

# User specific environment and startup programs

PATH=$PATH:$HOME/bin

export PATH

local_remote() {
    read -p "create local and remote git repository push all files in current directory? y/*" verify
    case "$verify" in
        yes|y)
            echo -n "..."
            ;;
        *)
            echo -n "you didn't enter y or n"
            exit
            ;;
    esac
    repo_name=$1
   
    dir_name=`basename $(pwd)`
   
    if [ "$repo_name" = "" ]; then
        echo "Repo name (hit enter to use '$dir_name')?"
        read repo_name
    fi
   
    if [ "$repo_name" = "" ]; then
        repo_name=$dir_name
    fi
   
    username=`git config github.user`
    if [ "$username" = "" ]; then
        echo "Could not find username, run 'git config --global github.user <username>'"
        invalid_credentials=1
    fi
   
    token=`git config github.token`
    if [ "$token" = "" ]; then
        echo "Could not find token, run 'git config --global github.token <token>'"
        invalid_credentials=1
    fi
   
    if [ "$invalid_credentials" == "1" ]; then
        return 1
    fi
 
    echo -n "Creating local Github repository '$repo_name' ..."
    git init && git add . && git cm -m 'init commit' > /dev/null 2>&1
    echo " done."
   
    echo -n "Creating Github remote repository '$repo_name' ..."
    curl -u "$username:$token" https://api.github.com/user/repos -d '{"name":"'$repo_name'"}' > /dev/null 2>&1
    echo " done."
   
    echo -n "Pushing local code to remote ..."
    git remote add origin git@github.com:$username/$repo_name.git > /dev/null 2>&1
    git push -u origin master > /dev/null 2>&1
    echo " done."
}

remote_create() {
    read -p "simply create remote git repository? y/*" verify
    case "$verify" in
        yes|y)
            echo -n "..."
            ;;
        *)
            echo -n "you didn't enter y or n"
            exit
            ;;
    esac

    if [ $1 ]
    then
        repo_name=$1
    else
        echo -n "Repo name? "
        read repo_name
        while [ -z "$repo_name"]
        do
            echo -n "you didn't enter repo name"
            read repo_name
        done
    fi
   
    username=`git config github.user`
    token=`git config github.token`
    echo -n "creating remote git repository ... "
    curl -u "$username:$token" https://api.github.com/user/repos -d '{"name":"'$repo_name'"}' > /dev/null 2>&1
    git remote add origin git@github.com:eduOSS/$repo_name.git > /dev/null 2>&1
    git push -u origin master > /dev/null 2>&1
    echo 'done.'
}

git_push(){
    read -p "pushing all files to remote repository? y/*" verify
    case "$verify" in
        yes|y)
            echo -n "..."
            ;;
        *)
            echo -n "you didn't enter y or n"
            exit
            ;;
    esac

    if [ $1 ]
    then
        massage=$1
    else
        echo -n "plz comment, the default is quick_flush: " # -n for supresses newline
        read massage
        if [ -z "$massage" ] #check if massage is empty
        then
            echo -n "use the default comment"
            massage=quick_flush 
        fi
    fi
    
    echo -n "pushing all files to remote repository ..."
    git add . && git cm -m $massage && git push > /dev/null 2>&1
    echo 'done.'
}
