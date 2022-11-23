# If not running interactively, don't do anything
[[ $- != *i* ]] && return

export HISTCONTROL=ignoreboth:erasedups
export EDITOR='nvim'
export VISUAL='nvim'
export GOPATH=$HOME/go
export PATH="$PATH:$HOME/.local/bin:$HOME/.cargo/bin/:/opt/aseprite:/opt/quick_notes/:$GOPATH/bin"

#PS1="\[\e[0;38;5;203m\]┌\[\e[0;38;5;203m\][\[\e[0;38;5;203m\]\h\[\e[0;38;5;203m\]] \[\e[0;4;38;5;38m\]\w \[\e[0;4;38;5;77m\]\$\[\e[0m\]\n\[\e[0;38;5;203m\]└■|\[\e[0m\]"

# ignore upper and lowercase when TAB completion
bind "set completion-ignore-case on"

# increase bash history size
HISTSIZE=10000
HISTFILESIZE=10000


#********************************************************************#
#-------------------------All types of Alias-------------------------#
#____________________________________________________________________#


# custom QoL
alias b="cd ~/Projects/EchoRealms/backend-old/echorealms"
alias f="cd ~/Projects/EchoRealms/react"

# fix obvious typo's
alias cd..='cd ..'
alias pdw="pwd"
alias udpate='sudo pacman -Syu'
alias upate='sudo pacman -Syu'
alias updte='sudo pacman -Syu'
alias updqte='sudo pacman -Syu'

# list
alias ls='exa --icons'
alias la='exa -a --icons'
alias ll='exa -al'
alias lt='exa -aT'

# ripgrep
alias rg="rg --sort path"

# xplr
alias xx="xplr"

# rm
alias rm="rm -I"

# nvim
alias n="nvim"

# buku
#alias b="buku --suggest"
#alias buku_list="buku -p"

# Colorize the grep command output
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

# readable output
alias df='df -h'

# free
alias free="free -mt"

# continue download
alias wget="wget -c"

# pacman
alias pacman='sudo pacman --color auto'
alias update='sudo pacman -Syu'
alias psearch='sudo pacman -Ss'
alias install='sudo pacman -S'
alias uninstall='sudo pacman -Rcns'
alias pklist='sudo pacman -Qe'  				# show package list
alias pcc='sudo pacman -Sc' 						# clear package cache
alias cleanup='sudo pacman -Rns $(pacman -Qtdq)' # cleanup orphaned packages

# grub
alias update-grub="sudo grub-mkconfig -o /boot/grub/grub.cfg"

# fonts
alias update-fonts='sudo fc-cache -fv'
alias font-search='fc-list | rg'

#find the name of the selected program
alias find_name="xprop | grep \"WM_CLASS\""

# youtube-dl
alias yta-aac="youtube-dl --extract-audio --audio-format aac "
alias yta-best="youtube-dl --extract-audio --audio-format best "
alias yta-flac="youtube-dl --extract-audio --audio-format flac "
alias yta-m4a="youtube-dl --extract-audio --audio-format m4a "
alias yta-mp3="youtube-dl --extract-audio --audio-format mp3 "
alias yta-wav="youtube-dl --extract-audio --audio-format wav "
alias ytv="youtube-dl --external-downloader=aria2c --external-downloader-args '--min-split-size=1M --max-connection-per-server=16 --max-concurrent-downloads=16 --split=16' "
alias ytv-best="youtube-dl -f bestvideo+bestaudio --external-downloader=aria2c --external-downloader-args --external-downloader=aria2c --external-downloader-args '--min-split-size=1M --max-connection-per-server=16 --max-concurrent-downloads=16 --split=16' "
alias ytv-480="youtube-dl -f 'bestvideo[height=480]+bestaudio' --external-downloader=aria2c --external-downloader-args '--min-split-size=1M --max-connection-per-server=16 --max-concurrent-downloads=16 --split=16' "

# cpu microcode
alias microcode='grep . /sys/devices/system/cpu/vulnerabilities/*' # check vulnerabilities microcode

# get the fastest mirrors
alias mirror="sudo reflector -f 30 -l 30 --number 10 --verbose --save /etc/pacman.d/mirrorlist"

# get the error messages from journalctl
alias jctl="journalctl -p 3 -xb"

# list of all installed desktops - xsessions desktops
alias xd="ls /usr/share/xsessions"

#********************************************************************#
#-------------------------END OF SECTION-----------------------------#
#____________________________________________________________________#


## ex = EXtractor for all kinds of archives
## usage: ex <file>
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

# Launch at start
#neofetch
#pfetch

# starship prompt
eval "$(starship init bash)"

# git shortucts
alias ga='git add'
alias gaa='git add .'
alias gaaa='git add --all'
alias gd='git diff'
alias gda='git diff HEAD'
alias gi='git init'
alias glg='git log --graph --oneline --decorate --all'
alias gld='git log --pretty=format:"%h %ad %s" --date=short --all'
alias gs='git status'

# export stuff
export SDKMAN_DIR="$HOME/.sdkman"
[[ -s "$HOME/.sdkman/bin/sdkman-init.sh" ]] && source "$HOME/.sdkman/bin/sdkman-init.sh"
