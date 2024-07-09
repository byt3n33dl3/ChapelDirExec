# ChapelDirExec

<a href="https://github.com/pxcs/ChapelDirExec/"><p align="center">
<img src="/img/cde.png">
</p></a>

## Welcome to **CDE** project

- If you want to report a problem, open un [Issue](https://github.com/pxcs/ChapelDirExec/issues) 
- If you want to contribute, open a [Pull Request](https://github.com/pxcs/ChapelDirExec/pulls)
- If you want to discuss, open a [Discussion](https://github.com/pxcs/ChapelDirExec/discussions)

# Installation
please see the **packages** and **repo** [here!](https://github.com/pxcs/ChapelDirExec/)

## Requirements
**ChapelDirExec** uses **libssh** - The SSH Library [libssh](http://www.libssh.org/)

## Build

Requirements:

* `make`
* `gcc` compiler
* `libssh-dev`

```bash
git clone --depth=1 https://github.com/pxcs/ChapelDirExec.git
cd ChapelDirExec
make
make install
```

## Static build

Requirements:

* `cmake`
* `gcc` compiler
* `make`
* `libssl-dev`
* `libz-dev`

```bash
git clone --depth=1 https://github.com/pxcs/ChapelDirExec.git
cd ChapelDirExec
bash static-build.sh
make install
```

**Credit** to [@matricali](https://github.com/matricali/) and *Hydra*
