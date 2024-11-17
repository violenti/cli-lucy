from azure.devops.v7_1.build.models import BuildDefinition, BuildRepository, AgentPoolQueue
import time

"""
def read_repos(input):
    with open(input, 'r') as f:
        repos = [line.strip() for line in f if line.strip()]  
    return repos
"""
def create_build(project,build_client,input):
    
    yaml_path = "azure-pipelines.yml"

    with open(input,'r') as file:
        for line in file:
            repo_name = line.strip()

            build_definition = BuildDefinition(
                name=repo_name,
                repository=BuildRepository(
                    id=repo_name,
                    name=repo_name,
                    type='TfsGit',  # Para repositorios en Azure DevOps Git
                    default_branch = f'refs/heads/main'
                ),
                process={
                    'yamlFilename': yaml_path
                },
                queue=AgentPoolQueue(
                    name="Azure Pipelines" # Nombre del pool de agentes
                )
                )
            try:

                pipeline = build_client.create_definition(build_definition, project)
                print(f"Pipeline {repo_name} created successfully")
                time.sleep(1)
            except Exception as e: 
                    print(f"Error to created the pipeline  '{repo_name}': {e}")
               