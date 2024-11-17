# Lucy &#x1F40D;


Lucy  is a Python CLI for automatization of Azure Devops.


# Feature 
    
* Create a repository from a list of names in a file
* Create  a Pipeline from a list of names in a file
* List repositories and save them to a file

## Installation

Lucy use Poetry as package manager.

Please, if you  do not  Poetry installed on your computer, you can  install it by  following the instructions below:  https://python-poetry.org/docs/#installation


```bash
poetry shell

poetry install
```

## Usage

Lucy use your  PAT of Azure Devops

```bash
export PAT="D5xxxxxxxxxx"

```

# Commands

# Arguments and Description of `parse_args`

| Argument             | Description                                                      |
|----------------------|------------------------------------------------------------------|
| `-p`, `--project`    | The name of the Azure DevOps project. This argument is required. |
| `-o`, `--output`     | The file where results will be generated. This argument is optional. |
| `-i`, `--input`      | The input file containing the list of repositories.             |
| `-org`, `--organization` | The name of the Azure DevOps organization. This argument is required. |
| `-l`, `--list`       | Lists all repositories in the specified project. This is a **flag**. |
| `-c`, `--create`     | Creates repositories based on the provided input file. This is a **flag** 



## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)