# Navigation
function ..	; cd .. ; end
function ...	; cd ../.. ; end
function ....	; cd ../../.. ; end
function .....	; cd ../../../.. ; end

# Utilities
function g	; git $argv ; end
function grep	; command grep --color=auto $argv ; end

alias chmox='chmod +x'

alias dfree="df -P -kHl"
alias myip="curl https://api.ipify.org"
alias ungz="gunzip -kr"

# File size
alias fs="stat -f \"%z bytes\""
