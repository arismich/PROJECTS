def gp(msg="Quick update"):
    import os
    os.system('git add .')
    os.system(f'git commit -m "{msg}"')
    os.system('git push')

gp("Hello again")
