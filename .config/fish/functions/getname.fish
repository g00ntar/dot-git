function getname
  command echo $argv[1] | awk -v FS='.' -v OFS='.' '{NF--; print $0}'
end
