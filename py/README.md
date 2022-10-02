# `README.md` for `sooty-tern/py`

## ❄ Environment setup

Clone this repo and navigate to `sooty-tern/py`. Run

```
conda env create -f sooty-term.yml
```

to install the conda virtual environment. Activate it with

```
conda activate sooty-tern
```

Next, run

```
pip install -e .
```

to install the local `py/ai` module. See [here](https://goodresearch.dev/setup.html#pip-install-your-package) for more details.

## 🌸 Script inputs and outputs

### 📁 `holos/scripts`

#### 👩‍💻 `get_hub.py`

- Input: **nothing**
- Output:
  - Folders:
    - `holos/data/tsv`
    - `holos/data/html/`
  - Files:
    - `holos/data/tsv/hub.tsv`
    - `holos/data/html/hub.html`

#### 👩‍💻 `get_volcanoe_pages.py`

- Input:
  - Folder: `holos/data/tsv/hub.tsv`
- Output:
  - Folder: `holos/data/html/volcano_pages`
  - Files: `{volcano id}.html`

#### 👩‍💻 `parse_profiles.py`

- Input:
  - Folder: `holos/data/html/volcano_pages/`
  - Files: `{volcano id}.html`
- Output:
  - Folder: `holos/data/tsv/`
  - File: `profiles.tsv`

### 👩‍💻 `parse_availability.py`

- Input:
  - Folder: `holos/data/html/volcano_pages/`
  - File: `{volcano id}.html`
- Output:
  - Folder: `holos`

### 📁 `pleistos/scripts`

## ❄ Script run order

## 🌸 Data

- [Global Volcanism Program](https://volcano.si.edu/)
  - [Holocene Volcano List](https://volcano.si.edu/volcanolist_holocene.cfm)
  - [Pleistocene Volano List](https://volcano.si.edu/volcanolist_pleistocene.cfm)
  - [Database updates](https://volcano.si.edu/gvp_votw.cfm#log)

## ❄ Reading

- [How to Pass Arguments to a Python Script from the Command Line | OpenSourceOptions](https://opensourceoptions.com/blog/how-to-pass-arguments-to-a-python-script-from-the-command-line/)
