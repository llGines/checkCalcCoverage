# mycalc
Project destined to test pytest-cov, Python Coverage capabilities and local runner

read our wiki about testing "https://github.com/iPronics/iPronics-PRL/wiki/Intro-to-automated-testing"

more in  https://docs.pytest.org/en/7.4.x/

coverage: https://coverage.readthedocs.io/en/7.4.0/

Clone this repo with "git clone git clone git@github.com:llGines/checkCalcCoverage.git --depth=1"

navigate to parent folder and install this project with 
"python3 -m pip install -e ."

test files must start with test_ or end woth _test

run test with pytest
run coverage with "pytest --cov-report term-missing --cov=mycalc"
run pytest coverag with pytest --cov 

tests must be located in /test directory

