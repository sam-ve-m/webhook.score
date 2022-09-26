#!/bin/bash

fission spec init
fission env create --spec --name caf-score-val-env --image nexus.sigame.com.br/fission-async:0.1.7 --builder nexus.sigame.com.br/fission-builder-3.8:0.0.1
fission fn create --spec --name caf-score-val-fn --env caf-score-val-env --src "./func/*" --entrypoint main.caf_transaction --executortype newdeploy --maxscale 3
fission route create --spec --name caf-score-val-rt --method POST --url /webhook/caf/score-validation --function caf-score-val-fn