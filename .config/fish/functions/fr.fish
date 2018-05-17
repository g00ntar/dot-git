function fr
  command find ./ -iname $argv[1] -printf "%T@ %TY-%Tm-%Td %p\n" | sort -n | cut -d " " -f 2- | grep -i (echo $argv[1] | tr -d '*')
end
