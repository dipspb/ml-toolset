import os
from IPython.lib import passwd

c.NotebookApp.ip = '*'
c.NotebookApp.port = int(os.getenv('PORT', 8888))
c.NotebookApp.open_browser = False
c.MultiKernelManager.default_kernel_name = 'python'
c.NotebookApp.iopub_data_rate_limit = 10000000000

# sets a password if PASSWORD is set in the environment
if 'PASSWORD' in os.environ:
  c.NotebookApp.password = passwd(os.environ['PASSWORD'])
  del os.environ['PASSWORD']

