#!/usr/bin/env zsh

autoload -U add-zsh-hook
_tfenv_autoload(){
  if [[ $(find ./ -maxdepth 1 -name "*.tf") ]]; then
    autotfenv
  fi
}

add-zsh-hook chpwd _tfenv_autoload
