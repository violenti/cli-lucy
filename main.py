from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import os,sys
import argparse
from get_repository import list_repo
from create_repository import create_repo



personal_access_token = os.environ["PAT"]


vault = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠛⢶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣦⠀⣠⡾⠛⠙⠛⠋⠀⠀⠀⠈⠉⠛⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⡇⠙⠛⠋⢀⣤⣀⠀⣀⣤⣤⡀⠀⠀⠀⠈⠻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣧⡀⢀⡤⠋⠀⠈⠉⠉⠀⠉⠳⠤⠤⠴⢦⡄⠸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀⡿⠿⠾⠀⠀⠀⠀⠀⢴⣦⡀⠀⠀⠀⣠⠟⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡟⠀⣴⡄⠀⢀⡄⠀⠀⣦⡈⠃⠀⠀⡾⣳⣄⠀⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⡶⠟⠻⠶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠿⠁⢀⡞⠁⠀⠀⣿⠗⠀⠀⠀⣟⢮⣿⣆⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⠏⠀⠀⠀⣰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠰⣯⡀⠀⠀⠀⠀⠀⠀⠀⠀⠪⣳⡵⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⡀⠀⠀⢰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣇⠀⣦⣀⠀⠈⠉⢀⣀⣰⣦⡀⠀⠀⠀⠀⠈⠉⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⣷⠀⠀⠘⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡆⠻⠦⣌⣉⣉⣁⡤⠔⠻⡇⠀⠀⠀⣀⣠⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⡾⠛⠉⠙⠛⠲⢦⣄⠀⠙⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣄⠀⠀⠲⠇⠀⠀⠀⠀⠀⠀⢀⣴⢏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣇⣀⣀⣀⡀⠀⠀⠈⣧⠀⠈⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⢀⣻⣦⣄⠀⠀⠀⠀⠀⠀⡠⠔⣿⠓⢶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⠟⠁⠀⠈⠉⠙⠳⢴⡏⠀⠀⣿⡇⠈⠙⠻⠶⠤⠴⠶⠛⠋⠹⡀⠈⠻⣶⣤⠤⠄⣀⣠⠞⠁⠀⢸⠀⠈⠙⠳⢦⣄⠀⠀⠀⠀⠀⠀⠀
⠸⣧⣤⣤⣤⣤⣀⡀⠀⣷⢀⣼⠃⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣀⠀⠉⠉⠉⠉⠀⠀⢀⣴⠏⠀⠀⠀⠀⠀⠉⠻⣦⣄⠀⠀⠀⠀
⢰⡏⠀⢠⠀⠀⠈⠉⢺⠁⢈⡞⢀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠒⢦⠀⠀⠀⢸⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡄⠀⠀
⠀⠻⣦⣈⠙⠶⠤⠴⢞⣠⠞⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀⢀⣦⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠈⡆⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠈⠻⣆⠀
⠀⠀⠈⠉⠉⠛⠛⠛⠯⢤⣤⣎⣀⠀⠀⠀⢀⣀⣠⣤⣾⠛⠁⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⢻⠀⠀⠀⠈⡆⠀⠀⡀⠀⠀⠀⠀⠀⠙⣇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠛⠛⠉⠉⠠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢇⠀⠀⠀⠀⡇⠀⠀⠀⡇⠀⣰⠏⠀⠀⠀⠀⠀⠀⡿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⢃⠀⠀⠀⢸⣰⠁⠀⠀⠀⠀⠀⠀⣸⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠀⠀⠀⢸⠀⠀⢀⣸⡇⠀⠀⠀⠀⠀⠀⣰⠏⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠛⠢⣄⡀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠸⣤⠴⠛⠁⣿⠤⢤⡀⠀⢀⡼⠏⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠉⠉⠓⠒⠶⠶⠞⠁⠀⠀⠀⠀⠁⠀⠀⠀⢿⠀⠀⠈⢳⡟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⢻⠀⠀⣀⡼⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠙⠢⢄⣀⡀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⡴⠞⠋⠀⠀⡇⠛⣻⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⠀⠀⠀⠈⠉⠉⠛⠛⠛⠛⠛⠉⠉⠉⠀⠀⠀⠀⠀⠀⡟⠛⠋⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡖⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⢰⡟⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠁⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⣸⠏⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣧⣄⡀⠀⠀⠀⠀⣀⡼⠏⠀⠀⠀⠀⢻⡖⠶⡤⠤⠤⠤⠶⠛⠶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⠉⠙⠛⠛⣿⠋⠀⠀⠀⠀⠀⠀⠘⠻⠶⠿⠶⣦⣀⣀⠀⠀⠀⢉⣻⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⣀⣀⣠⣴⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀
"""
print (vault)

def parse_args(): 
    """_summary_
    """
    parser = argparse.ArgumentParser(epilog='\tExample:\r\npython'
                                    + sys.argv[0] +
                                    "-i repository.txt")
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-p', '--project', help="project name of your azure devops",
                       type=str, required=True)
    parser.add_argument('-o','--output',
                        help="file generate",
                        required=False)
    parser.add_argument('-i', '--input',help="file from will your list of repository")
    parser.add_argument('-org', '--organization', help="file from will your list of repository",
                       type=str, required=True)
    parser.add_argument('-l', '--list', help="list all repositories",
                        action='store_true')
    parser.add_argument('-c', '--create', help="create repositories",
                        action='store_true')
    return parser.parse_args()

args = parse_args()



def main():
    """_summary_

    Args:
        args (_type_, optional): _description_. Defaults to None.
    """
    project = args.project
    organization_url = args.organization
    output = args.output
    input = args.input
    credentials = BasicAuthentication('', personal_access_token)
    connection = Connection(base_url=organization_url, creds=credentials)
    git_client = connection.clients.get_git_client()
    if args.list and args.create is False :
        list_repos = list_repo(organization_url, git_client, project,output)
    elif args.create and args.list is False:
       create = create_repo(organization_url,git_client,project, args.input)
       #print("command not found")
    '''
    #repository = args.input
    if project or organization_url or repository is None:
        print ("Please, the values project, organization and repository are requiered")
    else: 
        with open(repository,encoding='utf-8') as file:
            for line in file:
                repo_name = line.split()
                time.sleep(1)
                list_repository = create_repo(organization_url,project,repo_name)
    '''
if __name__ == '__main__':
    main()