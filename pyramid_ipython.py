from IPython.terminal.embed import InteractiveShellEmbed

def ipython_shell_runner(env, help):
    IPShell = InteractiveShellEmbed(banner2=help + '\n', user_ns=env)
    IPShell()
