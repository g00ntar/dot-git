function loc --description "Better mlocate"
# TODO
# do update first?
	updatedb --output=$HOME/.mlocate.db
	locate --database=$HOME/.mlocate.db --all --ignore-case --null $argv | grep --null --invert-match --extended-regexp '~$' | fzf --read0 -0 -1 -m
end
