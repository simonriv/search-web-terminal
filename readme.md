# search-web-terminal

## Getting Started

Simple terminal program to open the browser and generate a search in windows.

## Content

### How to install

1. you must first clone the [repository](https://github.com/simonriv/search-web-terminal).
2. Open an instance of your installed terminal or windows powershell as administrator and go to the repository you just cloned, then run the installation.ps1 file.
3. then close and reopen the terminal to refresh the environment variables.

If the installation mentions that I can't add the path to the path you will have to do it manually.
Now you can use it using the word search.

### How to use

using the word `search` and passing the parameters `--browser` and `--engine` you can create a configuration file with your search preferences, these preferences are the browser you use and the search engine, in the browser are the following options:

* chrome
* opera
* firefox
* brave
* edge
* explorer

and in the search engine these are the options:

* Google
* Bing
* DuckDuckGo
* Yahoo

you can also pass the parameters with the diminutive `-b` `-e`, for example:

```sh
search --browser firefox --engine google

search -b opera -e bing
```

using the word `search` you can pass as an argument an address, for example:

```sh
search www.github.com/simonriv
```

this will open your previously configured browser and run the address you passed as an argument, if you don't type the www no problem the software will complete it.

you can also search by terms, for example:

```sh
search hello world in python
```

This will search your previously configured search engine for what you have typed.

