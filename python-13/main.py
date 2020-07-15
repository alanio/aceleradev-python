# .travis.yml
config = """
language: python
python:
    - "2.7"
    - "3.7"
    - "pypy"
    - "pypy3"
jobs:
    include:
    - stage: test
install:
    - pip install -r requirements.txt
    - pip install .
script: pytest
"""