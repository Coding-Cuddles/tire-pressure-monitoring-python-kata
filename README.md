# Tire pressure monitoring kata in Python

[![CI](https://github.com/Coding-Cuddles/tire-pressure-monitoring-python-kata/actions/workflows/main.yml/badge.svg)](https://github.com/Coding-Cuddles/tire-pressure-monitoring-python-kata/actions/workflows/main.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Practice characterization testing against inherited tire-pressure monitoring code. Setup is
complete when the existing test passes.

## Overview

This kata complements [Clean Code: Advanced TDD, Ep. 23](https://cleancoders.com/episode/clean-code-episode-23-p1).

This repository contains two exercises designed to improve your skills in
test-driven development. It represents code you inherited from a legacy code
base.

As a first step, try to get some kind of test in place before you change the
class at all. If the tests are hard to write, is that because of the problems
with SOLID principles?

### Exercise 1

Write the unit tests for the `Alarm` class. The `Alarm` class is designed to
monitor tire pressure and set an alarm if the pressure falls outside of the
expected range.

The `Sensor` class provided for the exercise simulates the behaviour of a real
tire sensor, providing random but realistic values.

You can choose to use stubs, mocks, or none at all. If you do, you are free to
use the mocking tool that you prefer.

> **Note**
>
> If you decide to use mocks, we recommend using the
> [unittest.mock](https://docs.python.org/3/library/unittest.mock.html)
> mock object library.

### Exercise 2

Use one of the mocking patterns: Self-Shunt, Test-Specific Subclass, or Humble
Object. If you used one of them already, use another one.

## Prerequisites

Required:

- [Git](https://git-scm.com/downloads)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

Optional:

- [GNU Make](https://www.gnu.org/software/make/), for shorter commands. Every required task also
  has a direct `uv` command.

You do not need to install Python or pytest separately. `uv` installs a compatible Python version
and the locked project dependencies when needed.

## Set up the kata

1. Clone the repository:

   ```console
   git clone https://github.com/Coding-Cuddles/tire-pressure-monitoring-python-kata.git
   ```

2. Enter the repository directory:

   ```console
   cd tire-pressure-monitoring-python-kata
   ```

3. Run the existing test. Use Make when it is installed:

   ```console
   make test
   ```

   Otherwise, run pytest through `uv` directly:

   ```console
   uv run pytest
   ```

   The first run may install Python and the project dependencies. Setup is complete when pytest
   reports `1 passed`.

   If the command fails with `uv: command not found`, install
   [uv](https://docs.astral.sh/uv/getting-started/installation/) and repeat this step.

## Work on the kata

1. Add characterization tests to `test_alarm.py` before changing `Alarm` in `alarm.py`.

2. Run the tests after each change. Use Make when it is installed:

   ```console
   make test
   ```

   Otherwise, run pytest through `uv` directly:

   ```console
   uv run pytest
   ```

   Continue when the test run completes without failures.

## Make command reference

Make is optional. Run `make` or `make help` to list these commands in the terminal.

| Command             | Result                                  |
| ------------------- | --------------------------------------- |
| `make all`          | Run the test suite                      |
| `make help`         | Show the available Make targets         |
| `make test`         | Run the test suite                      |
| `make format`       | Format tracked Python files             |
| `make format-check` | Check formatting without changing files |
| `make clean`        | Remove generated caches                 |

## Credits and references

- <https://github.com/emilybache/Racing-Car-Katas/tree/main/Python/TirePressureMonitoringSystem>
