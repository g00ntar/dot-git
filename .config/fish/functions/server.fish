function server -d 'Start a HTTP server in the current dir, optionally specifying the port'
    if test $argv[1]
        set port $argv[1]
    else
        set port 8000
    end

    xdg-open "http://localhost:$port/" &

    python3 -m http.server "$port"
end

