# Brazilian Energy Companies — Risk, Return & Correlation Analysis with Python

Projeto de portfólio em **Análise de Dados aplicada ao Mercado Financeiro** que compara Petrobras, Aeris Energy, Alupar, AES Brasil, Cemig e Cesp entre março de 2021 e março de 2022.

## Pergunta central

**Como retorno, volatilidade, drawdown e correlação diferenciam as seis empresas de energia no período analisado?**

A análise é descritiva e comparativa. Não constitui recomendação de investimento.

## Dataset

A planilha original tinha 251 registros; uma duplicata exata foi removida. Após a limpeza, permanecem **250 pregões únicos**, de **22/03/2021 a 22/03/2022**, sem valores ausentes.

Para facilitar o versionamento, o dataset foi dividido em cinco arquivos CSV em `data/raw/`. O carregador do projeto concatena automaticamente as partes e reproduz a série completa.

## Principais resultados

| Empresa | Retorno | Volatilidade anualizada | Drawdown máximo |
|---|---:|---:|---:|
| Petrobras | 47,53% | 35,30% | -16,71% |
| Cemig | 29,61% | 28,46% | -19,59% |
| Alupar | 8,54% | 20,21% | -17,37% |
| AES Brasil | 5,98% | 26,48% | -21,87% |
| Cesp | -15,65% | 25,25% | -31,18% |
| Aeris Energy | -37,50% | 50,79% | -51,68% |

A maior correlação diária observada é **AES Brasil × Cemig (~0,50)**. A menor é **Petrobras × Cesp (~0,03)**.

## Competências demonstradas

- análise comparativa de ativos;
- preparação e qualidade de dados;
- retornos percentuais;
- normalização base 100;
- volatilidade anualizada;
- drawdown;
- correlação;
- análise risco-retorno;
- séries temporais;
- testes automatizados e CI.

## Estrutura

```text
├── .github/workflows/python-tests.yml
├── data/raw/
│   ├── energy_companies_prices_part1.csv
│   ├── energy_companies_prices_part2.csv
│   ├── energy_companies_prices_part3.csv
│   ├── energy_companies_prices_part4.csv
│   └── energy_companies_prices_part5.csv
├── notebooks/energy_companies_market_analysis.ipynb
├── reports/
│   ├── methodology.md
│   └── summary.json
├── src/
│   ├── analysis.py
│   ├── data_cleaning.py
│   ├── metrics.py
│   └── visualization.py
├── tests/test_metrics.py
├── requirements.txt
└── README.md
```

## Como executar

```bash
python -m venv .venv
pip install -r requirements.txt
python -m src.analysis
python -m src.visualization
pytest -q
```

## Limitações

- período de aproximadamente um ano;
- ausência de benchmark;
- ausência de dividendos e dados fundamentalistas;
- o arquivo não documenta formalmente ajustes dos preços;
- não há taxa livre de risco;
- análise histórica, sem inferência causal.

## Autor

**Pablo Sena**  
GitHub: [@pablosena28](https://github.com/pablosena28)
