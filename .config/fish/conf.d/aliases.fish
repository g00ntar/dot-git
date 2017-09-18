# Navigation
function ..	; cd .. ; end
function ...	; cd ../.. ; end
function ....	; cd ../../.. ; end
function .....	; cd ../../../.. ; end

# Utilities
function g	; git $argv ; end
function grep	; command grep --color=auto $argv ; end

alias rm 'command grm --interactive --verbose'
alias chmox='chmod +x'

alias dfree="df -P -kHl"
alias myip="dig +short myip.opendns.com @resolver1.opendns.com"
