
function fi --description "Locate a file"
	locate --database=$HOME/.mlocate.db . | fzf --query "$argv"
end