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

### 📁 `holos/scripts` and `pleistos/scripts`

#### 👩‍💻 `get_hub.py`

- Input:
  - **nothing**
- Output:
  - Folders:
    - `/data/tsv/`
    - `/data/html/`
  - Files:
    - `/data/tsv/hub.tsv`
    - `/data/tsv/hub.tsv`

#### 👩‍💻 `get_volcano_pages.py`

- Input:
  - File:
    - `/data/tsv/hub.tsv`
- Output:
  - Folder:
    - `/data/html/volcano_pages`
  - Files:
    - `/data/html/volcano_pages/{volcano id}.html`

#### 👩‍💻 `parse_profiles.py`

- Input:
  - File:
    - `/data/html/volcano_pages/{volcano id}.html`
- Output:
  - File:
    - `/data/tsv/profiles.tsv`

### 👩‍💻 `parse_availability.py`

- Input:
  - File:
    - `/data/html/volcano_pages/{volcano id}.html`
- Output:
  - File:
    - `/data/tsv/availability.tsv`

## ❄ Script run order

First, run

```
get_hub.py -> get_volcano_pages.pys
```

Then you can run either

```
parse_profiles
```

or

```
parse_availability
```
