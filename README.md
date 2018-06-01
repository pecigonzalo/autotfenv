# AutoTFEnv

Helper tool to be used with [tfenv](https://github.com/kamatama41/tfenv), adds terraform version autoloading functionality on ZSH.

## How it works?

When you enter a directory containing `.tf` files, it will detect if there is a explicit version set, and load prompt you to load it.

## Installation

Install python helper using `pip` or `pipsi`

```
 pipenv install -e git+git@github.com:pecigonzalo/autotfenv.git
```

Now you can run `autotfenv` on any folder to check if the current `tfenv` version if the same as the one declared on the `.tf` files.

I have included a ZSH autoloader helper (`bin/autload.zsh`), that you can use to automatically check on folder change if there are `.tf` files, and if there are, trigger `autotfenv`.

To install it, simply source the file directly or using any ZSH framework.

EG:
```
zplug "github.com:pecigonzalo/autotfenv", use:"bin/autoload.zsh"
```

## Development
