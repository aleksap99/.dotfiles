alias encmount="encfs ~/.private ~/origin"
alias encunmount="fusermount -u ~/origin"
alias n="nvim"
alias showports="sudo ss -tuplwn | grep LISTEN"
alias notes="cd ~/Projects/Notes/IdleRunner; nvim Notes.md"
alias todos="cd ~/Projects/Notes/IdleRunner; nvim Todos.md"

alias cd..='cd ..'
alias pdw="pwd"

alias rg="rg --sort path"
alias mirror="sudo reflector -f 30 -l 30 --number 10 --verbose --save /etc/pacman.d/mirrorlist"
alias jctl="journalctl -p 3 -xb"
alias ls='exa --icons'
alias la='exa -a --icons'
alias ll='exa -al'
alias lt='exa -aT'
alias gs='git status'
alias ydl="youtube-dl --extract-audio --audio-format mp3 "
