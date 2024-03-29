# Tire pressure monitoring kata in Python

[![CI](https://github.com/Coding-Cuddles/tire-pressure-monitoring-python-kata/actions/workflows/main.yml/badge.svg)](https://github.com/Coding-Cuddles/tire-pressure-monitoring-python-kata/actions/workflows/main.yml)
[![Replit](https://img.shields.io/badge/Try%20with%20Replit-black?logo=replit)](https://replit.com/new/github/Coding-Cuddles/tire-pressure-monitoring-python-kata)

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

## Usage

You can import this project into [Replit](https://replit.com), and it will
handle all dependencies automatically.

### Prerequisites

* [Python 3.8+](https://www.python.org/)
* [pytest](https://pytest.org)

### Run main

```console
make run
```

### Run tests

```console
make test
```

## Credits and references

* <https://github.com/emilybache/Racing-Car-Katas/tree/main/Python/TirePressureMonitoringSystem>
