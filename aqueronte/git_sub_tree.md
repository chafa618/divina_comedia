Git Subtree - Ayuda al manejo de múlitples repositorios en uno, pero a diferencia de submodules permite manejar la data de cada repo de forma separada. 

git subtree lets you nest one repository inside another as a sub-directory. It is one of several ways Git projects can manage project dependencies.

There are several reasons why you might find subtree better to use:

- Management of a simple workflow is easy.
- Older version of git are supported (even before v1.5.2).
- The sub-project’s code is available right after the clone of - the super project is done.
- subtree does not require users of your repository to learn - anything new, they can ignore the fact that you are using - subtree to manage dependencies.
- subtree does not add new metadata files like submodules does - (i.e. .gitmodule).
- Contents of the module can be modified without having a - separate repository copy of the dependency somewhere else.
- In my opinion the drawbacks are acceptable:

#### Contras:

You must learn about a new merge strategy (i.e. subtree).
Contributing code back upstream for the sub-projects is slightly more complicated.
The responsibility of not mixing super and sub-project code in commits lies with you.


## How_to?
1) Agregar repo local
2) Agregar repo local como subtree del padre
3) Pull/push al padre



### Cómo agregar un repo como ST del repo principal?

Desde el padre, agregamos como remoto el repo ST:
1. Agregar el repo hijo como local

```{bash}
git remote add <local-repo-name> <subtree-url>
```

2. Luego agregamos el repo hijo como subtree del repo padre
con:

```{bash}
git subtree add --prefix=<local-repo-name> --squash <subtree-repo-name> master
```

* Se usa el flag --squash para que los cambios ingresen en un solo commit.

3. Para pullear cambios del padre
``` 
git subtree pull --prefix=<local-repo-name> --squash <subtree-repo-name> master
```

4. Para pushear: 
```
git subtree push --prefix=<local-repo-name> --squash <subtree-repo-name> master
```

#### Comandos
```
git subtree add -P <prefix> <commit>
git subtree add -P <prefix> <repository> <ref>
git subtree pull -P <prefix> <repository> <ref>
git subtree push -P <prefix> <repository> <ref>
git subtree merge -P <prefix> <commit>
git subtree split -P <prefix> [OPTIONS] [<commit>]
```

#### Manual: 
https://manpages.debian.org/testing/git-man/git-subtree.1.en.html

#### Buen Material:
https://medium.com/@v/git-subtrees-a-tutorial-6ff568381844

#### A Realy good video: 
https://www.youtube.com/watch?v=81kFGyn9Un0