# Navigation
function ..	; cd .. ; end
function ...	; cd ../.. ; end
function ....	; cd ../../.. ; end
function .....	; cd ../../../.. ; end

# Utilities
function c		; pygmentize -O style=monokai -f console256 -g $argv ; end
function grep	; command grep --color=always $argv ; end
function ls		; command ls --color=always $argv ; end
function l.		; command ls --color=always -d .* ; end

alias chmox='chmod +x'

#alias ls="ls --color=always"
alias dfree="df -P -kHl"
alias myip="curl https://api.ipify.org"
alias ungz="gunzip -kr"

# File size
alias fs="stat -f \"%z bytes\""
