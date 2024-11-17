from azure.devops.v7_1.git.models import GitRepositoryCreateOptions
from check_file import load_repo_names


def create_repo(organization,git_client, project, input):
    
    try:
        repo_names = load_repo_names(input)
        if  not repo_names:
            print("The file is not valid")
            return
        for repo_name in repo_names:        
            create_options = GitRepositoryCreateOptions(name=repo_name)
            new_repo = git_client.create_repository(git_repository_to_create=create_options, project=project)
            print(f"Repository '{new_repo.name}' created successfully. ID: {new_repo.id}")
    except FileNotFoundError as e: 
           print(e)
    except Exception as e:
         print(f"unexpected error: {e}")




   


    




    





