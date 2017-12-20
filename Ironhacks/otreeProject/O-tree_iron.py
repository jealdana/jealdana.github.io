
# coding: utf-8

# #### Steps:
# - Follow step 1 & 2 of official documentation
# - create environment 3.6
# - pip o-tree from conda 
# - activate environment
# - Continue following the next steps
# 
# The O-tree requirements from the [official setup documentation](#issue3) are:
# - Python 3
# - [PYcharm](#pycharm) (suggested)
# 
# **Pre-setting notes**   
# If you're moving from PY 2.X to 3.X and you want use anaconda library you may want to check this setup:
# - [Using (Ana)conda within PyCharm](#issue2)
# 
# **Jupyter documentation**  
# When documenting by using Jupyter Notebook you may want to look this:
# - [Conda environments not showing up in Jupyter Notebook](#issue1)  
# 
# [issue1]:<https://stackoverflow.com/questions/39604271/conda-environments-not-showing-up-in-jupyter-notebook>  
# [issue2]:<https://stackoverflow.com/questions/28390961/using-anaconda-within-pycharm>
# [issue3]:<http://otree.readthedocs.io/en/latest/install.html>
# [pycharm]:<>
# 

# In[ ]:

import django


# In[2]:

print(django.get_version())

