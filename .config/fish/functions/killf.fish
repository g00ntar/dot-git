function killf
	if test ! -z $TMUX
		set -l FZF "fzf-tmux -r"
	else 
		set -l FZF "fzf"
	end
	if ps -ef | sed 1d | eval $FZF -m | awk '{print $2}' > $TMPDIR/fzf.result
		kill -9 (cat $TMPDIR/fzf.result)
	end
end	

