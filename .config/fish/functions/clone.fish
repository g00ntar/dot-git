function clone --description "clone something and cd into it."
    git clone --depth=1 $argv[1]
    cd (basename $argv[1] | sed 's/.git$//')
end