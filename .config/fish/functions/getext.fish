function getext
  command echo $argv[1] | awk -F . '{print $NF}'
end
