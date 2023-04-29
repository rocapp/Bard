#!/usr/bin/env bash

export BARD_TOKEN=$(cat ./SESSION_robbie)

ipython -i code_feedback.py
