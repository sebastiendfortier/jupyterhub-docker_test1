FROM jupyter/all-spark-notebook:latest

#LABEL maintainer="Luca De Feo <https://defeo.lu/>"

USER root

# APT packages
#RUN apt-get update && \
#    apt-get install -y --no-install-recommends \
#    fonts-dejavu \
#    tzdata \
#    gfortran \
#    gcc \
#    scilab \
#    pari-gp \
#    libpari-dev \
#    sagemath \
#    sagemath-jupyter \
#    libgmp-dev \
#    && apt-get clean && \
#    rm -rf /var/lib/apt/lists/*

USER $NB_UID

# Conda packages
# Sage conflicts with the latest jupyterhub, thus we must relax the pinning
#RUN conda install -c conda-forge python=3.9 --quiet --yes -n base 
RUN conda install -c conda-forge mamba --quiet --yes -n base
RUN mamba install -c conda-forge --quiet --yes  -n base\
#    'ipykernel' \
#    'r-base' \
#    'r-irkernel' \
#    'r-plyr' \
#    'r-devtools' \
#    'r-tidyverse' \
#    'r-shiny' \
#    'r-rmarkdown' \
#    'r-forecast' \
#    'r-rsqlite' \
#    'r-reshape2' \
#    'r-nycflights13' \
#    'r-caret' \
#    'r-rcurl' \
#    'r-crayon' \
#    'r-randomforest' \
#    'r-htmltools' \
#    'r-sparklyr' \
#    'r-htmlwidgets' \
#    'r-hexbin' \
    'jupyterhub'
#    'sage=8.*' \
#    'julia' && \
RUN conda clean -tip
RUN fix-permissions $CONDA_DIR

ENV CPATH=$CONDA_DIR/include

#RUN pip install \
#    pari_jupyter \
#    PySingular jupyter_kernel_singular \
#    scilab-kernel && \
RUN  fix-permissions $CONDA_DIR

# Fix SageMath kernel
USER root
#RUN sed -i 's/"\/usr\/bin\/sage"/"env", "PATH=\/usr\/local\/sbin:\/usr\/local\/bin:\/usr\/sbin:\/usr\/bin:\/sbin:\/bin", "\/usr\/bin\/sage"/' /usr/share/jupyter/kernels/sagemath/kernel.json
USER $NB_UID

# Add conda env hook
COPY ./conda-activate.sh /usr/local/bin/before-notebook.d/
