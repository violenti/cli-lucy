##
def list_repo(organization, git_client, project):
    repos = git_client.get_repositories(project=project)
    """
    for repo in repos:
        with open("repos.txt",'w') as file:
            file.write(repo)
            f.close
    """
    print(f"Repositorios en el proyecto '{project}':")
    for repo in repos:

        print(f"- Nombre: {repo.name}, ID: {repo.id}, URL: {repo.web_url}")
    


