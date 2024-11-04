from azure.devops.v7_1.git.models import GitRepositoryCreateOptions

def create_repo(organization,git_client, project, input):
        with open(input,'r') as file:
            for line in file:
                repo_name = line.strip()
                print(repo_name)
                if repo_name:
                    create_options = GitRepositoryCreateOptions(name=repo_name)
                    try: 
                        new_repo = git_client.create_repository(git_repository_to_create=create_options, project=project)
                        print(f"Repositorio '{new_repo.name}' creado con éxito. ID: {new_repo.id}")
                    except Exception as e: 
                        print(f"Error al crear el repositorio '{repo_name}': {e}")
            


   


    




    





