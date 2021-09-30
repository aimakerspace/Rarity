<!---
Copyright 2021 AI Singapore. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

<p align="center">
      <img alt="Rarity" src="docs/source/imgs/rarity_logo.png" width=200 height=100/>
</p>

<p align="center">
    <a href="https://img.shields.io/badge/python-3.6%2B-blue" target="_blank" rel="noopener noreferrer">
        <img alt="Python" src="https://img.shields.io/badge/python-3.8%2B-blue"/>
    </a>
    <a href="https://pypi.org/project/rarity/" target="_blank" rel="noopener noreferrer">
        <img alt="PyPI" src="https://img.shields.io/badge/pypi-v1.0-orange"/>
    </a>
    <a href="http://www.apache.org/licenses/LICENSE-2.0" target="_blank" rel="noopener noreferrer">
        <img alt="License" src="https://img.shields.io/badge/license-Apache%202.0-blue"/>
    </a>
    <a href="" target="_blank" rel="noopener noreferrer">
        <img alt="Docummentation" src="https://img.shields.io/badge/documentation-%20Rarity%20-blueviolet"/>
    </a>
    <a href="https://community.aisingapore.org/groups/mlops-data-and-infra-engineering/" target="_blank" rel="noopener noreferrer">
        <img alt="Community" src="https://img.shields.io/badge/community-AISG%20Forum-brightgreen"/>
    </a>
</p>
<br>

**Rarity** is a diagnostic library for tabular data with minimal setup to enable deep dive into datasets identifying features
that could have potentially influenced the model prediction performance. It is meant to be used at post model training phase to ease the understanding on
miss predictions and carry out systematic analysis to identify the gap between actual values versus prediction values. The auto-generated gap analysis
is presented as a dash web application with flexible parameters at several feature components.

The inputs needed to auto-generate gap analysis report with **Rarity** are solely depending on features, yTrue and yPred values. Rarity is therefore a model anogstic package and can be used to inspect miss predictions on tabular data generated by any model framework.


<br>

# Supported Analysis Type
Rarity currently supports tasks related to

- **Regression**
- **Binary Classifciation**
- **Multiclass Classification**

It can also be used to conduct **bimodal analysis**. As it is used to inspect miss predictions in details down to the granularity at each data index level, multiple modal analysis won't be ideal for repetition at individual data index for each model. Therefore, the package supports upto 2 model miss prediction gap analysis for side-by-side comparison benefiting more during the post model training and final phase of model fine-tuning stage.


<br>

# Core Feature Components
There are five core feature components covered in the auto-generated gap analysis report by **Rarity**:

- **General Metrics** : covers general metrics used to evaluate model performance.
- **Miss Predictions** : presents miss predictions scatter plot by index number
- **Loss Clusters** : covers clustering info on offset values (regression) and logloss values (classification)
- **xFeature Distribution** : distribution plots ranked by kl-divergence score
- **Similarities** : tabulated info listing top-n data points based on similarities in features with reference to data index specified by user

**Counter-Factuals** is also included under **Similarities** component tab for classification task to better compare data points with most similar features but show different prediction outcomes. For futher details on how the feature components are displayed in the web application, please checkout more examples under section [Feature Introduction]() in the package documentation.

<br>

[![Rarity Demo](https://github.com/aimakerspace/Rarity/raw/master/docs/source/imgs/gen-metrics-reg.png)](https://user-images.githubusercontent.com/35646492/135389621-e175596c-122e-4bb8-86c6-dc360668a500.mp4)

<br>

# Installation
**Rarity** has been tested on `Python 3.6+`. It is advisable to create a `Virtual Environment` to use along with **Rarity**.

For details guide on how to create virtual environment, you can refer to this [user guide](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).
After creation of the virtual environment, activate it and proceed with one of the following steps.

### From PyPI
```
    pip install rarity
```

### From Source
```
    git clone https://github.com/aimakerspace/rarity.git
    cd rarity
    pip install -e .
```


<br>

# Quick Start
**Rarity** is developed with minimum setup in mind in order for users to focus more on actual modelling works and decide appropriate fine-tuning strategy after
quick overview on the state of miss-prediction at post model training phase. Users can compile the required inputs and prediction outcomes via one of the following mentioned methods and spin up the dash web application to see the final gap analysis report produced by **Rarity**.

## Simplest mode with mininum code
After cloning **Rarity** repository, place `xFeatures`, `yTrue` and `yPred files` into `configs/csv_data` folder as illustrated in example below

```

    rarity
    ├── configs
    │   ├── csv_data
    │   │   ├── <example_user_xFeatures>.csv
    │   │   ├── <example_user_yTrue>.csv
    │   │   ├── <example_user_yPred_model_x>.csv
    │   │   └── <example_user_yPred_model_y>.csv
    │   │
    │   └── configs.py
    ...
    │ 
    ├── auto_gap_analysis.py


```

Then open `configs.py` file and update the first section to define the required meta data.

```python

    # ****************************************************************************************************************************************
    # To be updated by user accordingly if to run this script using saved csv files
    # Replace 'example_xxx.csv' with user's file name
    xFeature_filename = 'example_user_xFeatures.csv'
    yTrue_filename = 'example_user_yTrue.csv'
    yPred_filename = ['example_user_yPred_model_x.csv', 'example_user_yPred_model_y.csv']  # can be single file or max 2 files, wrap in a list

    # model name must be listed according to the same sequence of the yPred_filename list above in order to
    # indicate the prediction outputs are generated by the mentioned model
    MODEL_NAME_LIST = ['example_model_x', 'example_model_y']  # can be single model or max bi-modal, wrap in a list
    ANALYSIS_TYPE = 'Regression'  # Supported analysis types : 'Regression', 'Binary Classification', 'Multiclass Classification'
    ANALYSIS_TITLE = 'example_Customer Churn Prediction'
    PORT = 8000  # Defaults to 8000, user can re-define to a new port number of choice
    # ****************************************************************************************************************************************


```

After uploading files to `configs/csv_data` folder and updating `configs/configs.py` file, open terminal and make sure you are in the **Rarity** project root folder. A file named `auto_gap_analysis.py` is already in the root folder upon installation. Then run the following line of code in the terminal

```
    python auto_gap_analysis.py
```

A window will be open in the web browser and you will see the gap analysis report is generated for you by **Rarity**. Below is an example generated for Bimodal analysis on Regression task.

<br>
<p align="center">
      <img alt="Rarity" src="docs/source/imgs/gen-metrics-reg.png" width=85%/>
</p>
<br>


## Using CSVDataLoader
After installation, open terminal and run the following codes :

```python

    from rarity import GapAnalyzer
    from rarity.data_loader import CSVDataLoader

    # define the file paths
    xFeatures_file = 'example_xFeatures.csv'
    yTrue_file = 'example_yTrue.csv'
    yPred_file_list = ['example_yPreds_model_xx.csv', 'example_yPreds_rf.csv']
    model_names_list = ['model_xx', 'model_yy']

    # specify which port to use, if not provided, default port is set to 8000
    preferred_port = 8866

    # collate all files using dataloader to transform them into the input format that can be processed by various internal function calls
    data_loader = CSVDataLoader(xFeatures_file, yTrue_file, yPred_file_list, model_names_list, '<analysis_type>')  # example : '<analysis_type>' => 'Regression'
    analyzer = GapAnalyzer(data_loader, '<analysis_title>', preferred_port)  # example: '<analysis_title>' => 'Customer Churn Prediction'
    analyzer.run()


```
with additional adjustments as follows :
```diff
! replacement of example files to your own file names
! define `model_names_list`, `analysis_type` and `analysis_title` accordingly
```
<br>

## Using DataframeLoader
To use `DataframeLoader`, it is assumed that you already have some inital dataframes tap-out in earlier runs in the terminal and would like to continue analysing the miss-predictions after model training. The `DataframeLoader` api call is meant for inline analysis if you prefer not to collate base info using csv files. You may collate all the `xFeatures`, `yTrue` and `yPreds` dataframes into the right input format using `DataframeLoader` as demonstrated below :

```python

    from rarity import GapAnalyzer
    from rarity.data_loader import DataframeLoader

    # define the file paths
    xFeatures_df = <xfeatures_stored_in_pd.DataFrame>
    yTrue_df = <yTrue_stored_in_pd.DataFrame/Series>
    yPred_df_model_xx = <yPred_generated_by_model_xx_stored_in_pd.DataFrame>
    yPred_df_model_yy = <yPred_generated_by_model_yy_stored_in_pd.DataFrame>
    yPred_list = [yPred_df_model_xx, yPred_df_model_yy]
    model_names_list = ['model_xx', 'model_yy']

    # specify which port to use, if not provided, default port is set to 8000
    preferred_port = 8866

    # collate all files using dataloader to transform them into the input format that can be processed by various internal function calls
    data_loader = DataframeLoader(xFeatures_df, yTrue_df, yPred_list, model_names_list, '<analysis_type>')  # example : '<analysis_type>' => 'Regression'
    analyzer = GapAnalyzer(data_loader, '<analysis_title>', preferred_port)  # example: '<analysis_title>' => 'Customer Churn Prediction'
    analyzer.run()


```

<br>

# Supports
- Package documentation : Full version of the package documentation can be found [HERE]()
- Community : For interest on AI Singapore program, kindly head to our AISG community channels [HERE](https://community.aisingapore.org/groups/mlops-data-and-infra-engineering/)

<br>

# Acknowledgement

The developer team would like to express our gratitude to the program office for the support given to the development and release of this data dianogstic library <sup>#</sup>. Special thanks to [AI Singapore](https://aisingapore.org) making the development works of the package feasible.


### Program Office
This project is supported by the `National Research Foundation (NRF), Singapore` under its `AI Singapore Programme` (AISG-RP-2019-050).


### Developers
Yap Siew Lin (Core developer), Jeanne Choo (ex-AISG), Chong Wei Yih (ex-AISG)

<br>

<sup>*# Any opinions, findings and conclusions or recommendations expressed in this material are those of the author(s) and do not reflect the views of National Research Foundation, Singapore.*</sup>
