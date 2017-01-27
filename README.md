# Dot Git

A git-centric way to manage your dotfiles without symlinks

## Quick Start

### Install

1. [Fork this repository](https://github.com/Snaipe/dot-git/fork), and copy its push url.
2. Run the following commands (make sure to change `your_repo_url` and `your_shell_rc`):
```bash
$ git clone --bare your_repo_url .config/dotgit`.
$ echo "alias dot='git --git-dir=\"\$HOME/.config/dotgit\" --work-tree=\"$HOME\" '" >> ~/.your_shell_rc
$ source ~/.your_shell_rc
$ dot checkout -f --
```
3. You're done! Enjoy your new git-flavored dotfile manager.

### Usage

* Add some dotfiles to your repository:

```bash
$ dot add ~/.vimrc
$ dot commit -m "vim: added my configuration"
$ dot push
```

* Edit the dotfile matching some keywords:

```bash
$ dot edit vimrc        # will edit .vimrc
$ dot edit config dot   # will edit .config/dotgit/config
```

* List all commited dotfiles:

```bash
$ dot files             # all files
$ dot files vim         # all vim-related files
```

* Write-Lock/Unlock files (needs chattr)

```bash
$ dot files .vimrc      # check the permissions on .vimrc
-rw-r--r-- '.vimrc'
$ dot lock .vimrc       # lock vimrc
[sudo] Password for user :
$ dot files .vimrc      # .vimrc now has the 'i'mmutable flag.
irw-r--r-- '.vimrc'
$ dot edit .vimrc       # dot edit will unlock the file and re-lock it after editing
```

## F.A.Q.

**Q: I need to call `dot` to draw graphs, but you thoughtlessly
   replaced it with an alias. What do I do?**  
A: I don't know about you, but I only *need* to call dot once every full moon, so
   when I do, I just call `\dot`, which bypasses alias expansion. You're welcome.  