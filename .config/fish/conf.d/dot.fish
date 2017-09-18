function dot --description 'dotGIT function'
	git --git-dir="$HOME/.config/dotgit/repo" --work-tree="$HOME" $argv;
end
