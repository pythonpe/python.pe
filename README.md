# Python Peru's Website


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
apt install graphviz
```

Make sure you have Python 3.12 installed. Then install `poetry`:

```sh
pip install -U poetry
```

Then install all the necessary packages (make sure to change to the root directory of the project):

```sh
poetry install
```

You can build the html files of the blog by running the following command:

```sh
poetry run ablog build
```

Then you can serve the files locally using this command:
```sh
poetry run ablog serve
```
