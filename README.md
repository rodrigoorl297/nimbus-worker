# Nimbus Worker

[![CI](https://img.shields.io/badge/CI-GitHub_Actions-black)](.github/workflows/ci.yml)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

Worker com fila em memoria, retry e dead-letter — recorte de backend assincrono para **logistica / tracking**.

operacoes nao enxergam atrasos de entrega ate o cliente reclamar. Em producao isso viraria Redis/SQS; aqui o contrato de confiabilidade fica visivel em poucas classes.

## What recruiters should notice

- Padrao de job processor (tentativas, DLQ, handler).
- Teste cobrindo falha forçada.
- Documento de reliability, nao so o codigo.

## Run

```bash
python -m venv .venv
.venv/Scripts/activate
pip install -e ".[dev]"
python -m worker.cli
pytest -q
```
