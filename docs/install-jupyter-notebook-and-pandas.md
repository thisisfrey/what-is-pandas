# Install Jupyter Notebook and Pandas

## Virtual Environment Setup
1. Create a virtual environment named 'virt':
```python
```
2. Activate the virtual environment:
```python
# on Windows
virt\Scripts\activate

# On macOS and Linux:
source virt/bin/activate

```
3. List installed packages in the virtual environment:
```python
pip freeze
```

4. Deactivate the virtual environment when you're done:
```python
deactivate
```

## Pandas
This code requires the pandas library for data manipulation and analysis. To install pandas, use the following command within the virtual environment:
```python
pip install pandas
```

## Jupyter Lab & Jupyter Notebook
Jupyter is a popular platform for interactive computing and data analysis. Follow these steps to set up Jupyter Lab and Jupyter Notebook within the virtual environment:

1. Install Jupyter Lab and Jupyter Notebook:
```python
pip install jupyterlab
pip install notebook
```

2. Launch JupyterLab
```python
jupyter lab
```
This will open the JupyterLab interface in your default web browser, where you can create and manage notebooks.

3. Launch Jupyter Notebook
```python
jupyter notebook
```
This command will open the Jupyter Notebook interface in your browser.