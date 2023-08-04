# importing os module
import os

doc_dir = "docs/"
doc_filenames = [
    "install-jupyter-notebook-and-pandas",
    "pandas-series",
    "pandas-dataframes",
    "pull-data-from-pandas-dataframes",
    "how-to-count-data-in-a-dataframe",
    "add-new-columns-to-dataframe",
    "remove-columns-and-rows",
    "grab-rows-points-subsets-from-dataframe",
    "how-to-make-conditional-selections",
    "multiple-conditional-selections",
    "how-to-change-and-reset-index",
    "how-to-fix-incomplete-data",
    "pandas-dataframe-group-by",
    "how-to-count-unique-data-in-columns",
    "how-to-apply-functions-to-dataframes",
    "apply-functions-to-multiple-columns",
    "sorting-and-ordering-data",
    "histograms-with-matplotlib",
    "area-plots-with-matplotlib",
    "bar-charts-with-matplotlib",
    "line-charts-with-matplotlib",
    "scatterplots-with-matplotlib",
    "box-plots-with-matplotlib",
    "hex-bin-plots-with-matplotlib",
    "density-and-kde-plots-with-matplotlib",
    "intro-to-linear-regression-models",
    "train-test-split-for-linear-regression",
    "linear-regression-and-residuals"
]

# DOCS
# Create dir 
dir = './docs/'
if not (os.path.exists(dir) and os.path.isdir(dir)):
    os.mkdir(dir)

# Create doc files
for name in doc_filenames:
    f = open(dir + name + '.md', 'w')
    f.write('# ' + name.replace("-", " ").title())

## PYTHON
# Create py dir
py_dir = './code/'
if not (os.path.exists(py_dir) and os.path.isdir(py_dir)):
    os.mkdir(py_dir)

# Create py files
for name in doc_filenames:
    py_name = name.replace("-", "_")
    with open(py_dir + py_name + '.py', 'w') as f:
        pass
