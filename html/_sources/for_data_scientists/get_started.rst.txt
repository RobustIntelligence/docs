Get Started
================================

First, make sure you have everything set up correctly to run RIME:

.. toctree::
   :maxdepth: 1

   /for_data_scientists/get_started/setup.md


Then, check out one of our **Google Colab** tutorials for a quick introduction into running RIME.

Each notebook illustrates how to use RIME to validate, protect, and monitor your ML pipeline across a wide range of tasks
(from classification to ranking) and data modalities (Tabular, NLP, and Images). 
The datasets and models used in these examples come from well-known public sources like
`UCI ML <https://www.kaggle.com/datasets/uciml/adult-census-income>`_ or
`arXiv <https://www.kaggle.com/datasets/Cornell-University/arxiv?select=arxiv-metadata-oai-snapshot.json>`_.
In these notebooks, we walk through the steps of setting up RIME with an example dataset/model;
we run Stress Testing and then the AI Firewall.

Tabular Notebooks
^^^^^^^^^^^^^^^^^
* |Fraud_notebook|
* |NYC_notebook|
* |Movie_notebook|

NLP Notebooks
^^^^^^^^^^^^^^^^^
* |ArXiv_notebook|
* :doc:`how_to_guides/common_use_cases/adversarial_nlp`

CV Notebooks
^^^^^^^^^^^^^^^^^
* |Animals_notebook|

We also provide a lightweight template so that you can easily plug in your own dataset and model.

Custom Notebooks
^^^^^^^^^^^^^^^^
* |Custom_notebook|


.. |Fraud_notebook| raw:: html

    <a class="reference external" href="https://colab.research.google.com/drive/1qytdRPqE1hsJ2aKrCW3WvaBoVWdKLeL6" target="_blank">Fraud Detection (Binary Classification)</a>

.. |NYC_notebook| raw:: html

    <a class="reference external" href="https://colab.research.google.com/drive/1xbBQo0P57PfdeJz1cZacuGNpTknewKe7" target="_blank">NYC Taxi Dataset (Regression)</a>

.. |Movie_notebook| raw:: html

    <a class="reference external" href="https://colab.research.google.com/drive/1a5EEO4Ax0Ly3dLFuBP0BuqtKUdMupoGi" target="_blank">Movie Recommendations (Ranking)</a>

.. |ArXiv_notebook| raw:: html

    <a class="reference external" href="https://colab.research.google.com/drive/1IwN3aLeCCAzWl8MCk35wpyYYdu7Y1JgI" target="_blank">ArXiv Dataset (NLP, Classification)</a>

.. |Animals_notebook| raw:: html

    <a class="reference external" href="https://colab.research.google.com/drive/1ul-WPOfpqEF6Te_SLKsP9PptpTXeYbPT" target="_blank">Animals with Attributes 2 (Images, Classification)</a>

.. |Custom_notebook| raw:: html

    <a class="reference external" href="https://colab.research.google.com/drive/1bW0gdXep4BSBchuVaBUx4OtzZ3TYNm_p" target="_blank">Use RIME with your Own Dataset/Model</a>
