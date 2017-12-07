
# coding: utf-8

# In[ ]:





# # Web scraping

# - ## [Python Wars](Python Wars.ipynb)
# - ## Download of courses' files

# In[ ]:


import os
import requests

path = "."

for i in range(1,15):
    print('Downloading week %s...' %i )
    URL = "https://engineering.purdue.edu/~ee562/wk"+str(i)+".pdf"
    res = requests.get(URL)
    webFile = open(os.path.join(path, os.path.basename(URL)), 'w+')
    for chunk in res.iter_content(2^25): # 2^11 = 2 KB, 2^21 = 2 MB, 2^25 = 32 MB 
        webFile.write(chunk)
    webFile.close()


# # Jupyter
# 
# ### Jupyter - Automatic creation of html and py files 
# - Set up Jupyter to create html and py files when saving [Reference][best_practices]
# 
# [best_practices]:https://www.svds.com/tbt-jupyter-notebook-best-practices-data-science/?utm_source=kdnuggets&utm_medium=referral

# In[ ]:


get_ipython().magic(u'jupyter notebook --generate-config')
ifile = open("~/.jupyter/jupyter_notebook_config.py")
c = get_config()
### If you want to auto-save .html and .py versions of your notebook:
# modified from: https://github.com/ipython/ipython/issues/8009
import os
from subprocess import check_call

def post_save(model, os_path, contents_manager):
    """post-save hook for converting notebooks to .py scripts"""
    if model['type'] != 'notebook':
        return # only do this for notebooks
    d, fname = os.path.split(os_path)
    check_call(['jupyter', 'nbconvert', '--to', 'script', fname], cwd=d)
    check_call(['jupyter', 'nbconvert', '--to', 'html', fname], cwd=d)
c.FileContentsManager.post_save_hook = post_save


# # Misc
# 
# ### Getting list of files and subdirectories [Reference link][#list_files]
# 
# [#list_files]:<https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory>

# In[ ]:


"""Solution top 1"""
import os
path = "/Users/jesusenriquealdanasigona/Documents/Documents - Jesus’s Mac mini/Github/nanoHUB_roles/nanohub/Literature support/1 Escience"
arr_txt = [filename for filename in os.listdir(path) if (".pdf") in filename] 

arr_txt[:5]

