function loc --description "Better mlocate"
	if test ! -z $TMUX
		set -l FZF "fzf-tmux -u --height 20%"
	else 
		set -l FZF "fzf"
	end
# TODO
# do update first?
	updatedb --output=$HOME/.mlocate.db --require-visibility 0
	locate --database=$HOME/.mlocate.db --all --ignore-case --null $argv | grep -a --null --invert-match --extended-regexp '~$' | eval $FZF --read0 -0 -1 -m > $TMPDIR/fzf.result
	cat $TMPDIR/fzf.result
end
