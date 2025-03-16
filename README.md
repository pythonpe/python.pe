# Python Peru's Website

## Install build tools

To build, first you need to install graphviz:

1. macOS with Homebrew

```sh
brew install graphviz
```

2. macOS with MacPorts

```sh
sudo port install graphviz
```

3. apt-based Linux distribution

```sh
sudo apt install graphviz
```

Then make sure you have installed node and npm

1. macOS with Homebrew

```sh
brew install node
```

2. macOS with MacPorts

```sh
sudo port install nodejs21 npm10
```

3. apt-based Linux distribution

```sh
sudo apt install nodejs npm
```

Install sketchviz

```sh
npm i
```

Install `uv`, follow the instructions in their documentation
https://docs.astral.sh/uv/getting-started/installation/, `uv` will handle all
the dependencies and the python installation as well. So we don't need to
install `python` separately.

Then install all the necessary packages (make sure to change to the root
directory of the project):

```shell
uv sync
```

## Building the site

You can build the html files of the blog by running the following command:

```shell
uv run poe build
```

Then you can serve the files locally using this command:

```sh
uv run ablog serve
```
