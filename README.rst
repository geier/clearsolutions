Clear Solutions in Jupyter Notebooks
====================================

This extension for nbconvert allows to clear cells tagged with `solution`.

Install via `pip install .`, create config file and include the following line::

        c.Exporter.preprocessors = ['clearsolutions.ClearSolutionsPreprocessor']

run nbconvert::

        jupyter nbconvert notebook.ipynb --to notebook --config path_to_config.py
