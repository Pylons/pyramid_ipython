import IPython
from traitlets.config import Config

def ipython_shell_runner(env, help):
    c = Config()
    c.TerminalInteractiveShell.banner2 = help + '\n'
    IPython.start_ipython(argv=[], user_ns=env, config=c)
