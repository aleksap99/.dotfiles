# If not running interactively, don't do anything
[[ $- != *i* ]] && return

export HISTCONTROL=ignoreboth:erasedups
export EDITOR='nvim'
export VISUAL='nvim'
export GOPATH=$HOME/go
export PATH="$PATH:$HOME/.local/bin:$HOME/.cargo/bin/:/opt/aseprite:/opt/quick_notes/:$GOPATH/bin"

bind "set completion-ignore-case on"

HISTSIZE=10000
HISTFILESIZE=10000

alias b="cd ~/Projects/EchoRealms/backend-old/echorealms"
alias f="cd ~/Projects/EchoRealms/react"
alias encmount="encfs ~/.private ~/origin"
alias encunmount="fusermount -u ~/origin"
alias n="nvim"

alias cd..='cd ..'
alias pdw="pwd"

alias rg="rg --sort path"
alias mirror="sudo reflector -f 30 -l 30 --number 10 --verbose --save /etc/pacman.d/mirrorlist"
alias jctl="journalctl -p 3 -xb"

ex ()
{
  if [ -f $1 ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1   ;;
      *.tar.gz)    tar xzf $1   ;;
      *.bz2)       bunzip2 $1   ;;
      *.rar)       unrar x $1   ;;
      *.gz)        gunzip $1    ;;
      *.tar)       tar xf $1    ;;
      *.tbz2)      tar xjf $1   ;;
      *.tgz)       tar xzf $1   ;;
      *.zip)       unzip $1     ;;
      *.Z)         uncompress $1;;
      *.7z)        7z x $1      ;;
      *.deb)       ar x $1      ;;
      *.tar.xz)    tar xf $1    ;;
      *.tar.zst)   tar xf $1    ;;
      *)           echo "'$1' cannot be extracted via ex()" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}

alias gs='git status'


export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# starship prompt
eval "$(starship init bash)"
if [ -f ~/.bash_profile ]; then
    . ~/.bash_profile
fi

# export stuff
export SDKMAN_DIR="$HOME/.sdkman"
[[ -s "$HOME/.sdkman/bin/sdkman-init.sh" ]] && source "$HOME/.sdkman/bin/sdkman-init.sh"

