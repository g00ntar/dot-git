function dockerip -d "Get container IP"
  command docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $argv
end
