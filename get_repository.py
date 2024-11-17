##
#import json
def list_repo(organization, git_client, project, output):
    repos = git_client.get_repositories(project=project)
    with open(output,'w') as file:
        for repo in repos:
            file.write(repo.name + "\n")
   