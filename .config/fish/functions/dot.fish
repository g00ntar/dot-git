function dot --description 'dotGIT function'
	begin
    	set -lx PATH $PATH $HOME/.config/dotgit/bin
    	git --git-dir="$HOME/.config/dotgit/repo" --work-tree="$HOME" $argv;
	end
end
