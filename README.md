# Quadratic Equation Solver

This is the first lab for SDM which allow us to solve quadratic equations faster

## Install

1. First of all, you need be sure that you have this software installed:
  - python v3.x
  - git

2. Secondary, clone repository
```bash
  git clone https://github.com/kcholombytko/sdm-lab1
```
3. Thirdly, open directory
```bash
  cd sdm-lab1
```
4. Fourthly, run script
```bash
  python3 main.py
```

## How to use

Here is two variation of program:
1. Interactive
2. Non-interactive

Main script will give you menu with options

In interactive variation program will ask you to input values

```
a = 0
a can't be zero
a = 6
b = 5
c = 0
Equation is: (6.0) x^2 + (5.0) x + (0) = 0
There are 2 roots
x1 = 0.0, x2 = -1.2
```

In noninteractive you need to have file with numbers which will satisfy this regex: "\d\s\d\s\d\n". Example: 6 5 0

```
Equation is: (6.0) x^2 + (5.0) x + (0) = 0
There are 2 roots
x1 = 0.0, x2 = -1.2
```

[revert commit](https://github.com/SokolyukMisha/SDM_FirstLab/commit/a1b521d89f4ce82ff09f667edf386e8cac11fe94)
