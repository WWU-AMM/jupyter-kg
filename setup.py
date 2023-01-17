from setuptools import setup

setup(name='jupyter-kg',
      version='0.1',
      description='Simple Graph +  SparQL examples in Jupyter',
      url='http://github.com/WWU-AMM/jupyter-kg',
      license='BSD',
      packages=['jupyter_kg'],
      install_requires=['rdflib', 'jupyter', 'notebook', 'rich', 'ipywidgets', 'ipycytoscape', 'networkx'],
      zip_safe=False)