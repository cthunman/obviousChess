
PATH=$PATH:$HOME:$MVN_BIN:/.rvm/bin:/usr/local/mysql/bin # Add RVM to PATH fo rscripting

PS1='\[\e[0;32m\]\u\[\e[m\] \[\e[0;36m\]\w\[\e[m\] \[\e[0;31m\]\$ \[\e[m\]\[\e[0;35m\]'

# export PATH=/usr/local/apache-maven-3.x.y/bin:$PATH

export CLICOLOR=1
export LSCOLORS=fxGxCxDxBxegedabagaced

alias ls="ls -laG"
alias tail="tail -f -n 1000"

function modbash() {
    vim ~/.bashrc
}

