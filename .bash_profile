#
# ~/.bash_profile
#
if [ -z "${DISPLAY}" ] && [ "${XDG_VTNR}" -eq 1 ]; then
  exec startx
fi

if [ -f ~/.local/share/bash-completion/.git-completion.bash ]; then
  . ~/.local/share/bash-completion/.git-completion.bash
fi

