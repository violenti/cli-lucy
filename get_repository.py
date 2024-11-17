
def list_repo(organization, git_client, project, output):
    '''
       list repository of an azure devops project
    '''
    try:
        repos = git_client.get_repositories(project=project)
        if not repos:
            print(f"No repositories found in the project '{project}'.")
            return
        with open(output,'w') as file:
            for repo in repos:
                file.write(repo.name + "\n")

    except Exception as e:
        print(f"Error listing repositories: {e}")
   