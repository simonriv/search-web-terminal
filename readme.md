# search-web-terminal

## Getting Started

Simple terminal program to open the browser and generate a search.

## Requeriments

you must have [Python](https://www.python.org/downloads/) installed.

And before you can start editing it you need to install some python libraries first:

### Jedi

```sh
pip3 install jedi
```

```sh
pip3 install jedi-language-server
```

### pylint

```sh
pip3 install pylint
```

### Nvim

```nvim
CocInstall coc-python coc-jedi
```

## Content

### How to install

1. you must first clone the [repository](https://github.com/simonriv/search-web-terminal).
2. copy the dist folder and move it to the place where you prefer to have the application I have it in "C:\Program Files".
3. añade a tu path la ruta donde esta la carpeta del programa ejemplo "C:\Program Files\search"

Now you can use it using the word search.

### How to use

using the word `search` you can pass as an argument an address, for example:

```sh
search www.github.com/simonriv
```

this will open firefox and run the address you passed as argument, if you don't type the www there is no problem the software will complete it.

you can also search by terms, for example:

```sh
search hello world in python
```

This will Google what you have typed.

