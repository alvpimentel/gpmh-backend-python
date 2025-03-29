#  API Python de Pesquisas pro teste da GPMH

## Requisitos
- Python 3.10+

## Funcionalidades Principais
- **Upload de arquivos** XLSX
- **Cálculo automático** de médias (nota_1 + nota_2)
- **Conversão para JSON** estruturado

## Como Executar
```bash
git clone https://github.com/alvpimentel/gpmh-backend-python.git
cd gpmh-backend-python
pip install -r requirements.txt
python3 main.py
```

## Fomarto JSON de sucesso (exemplo)
```bash
  [
  {
    "codigo_pesquisa": "GPTW#1234",
    "nota_1": 100,
    "nota_2": 120,
    "media": 110.0
  },
  {
    "codigo_pesquisa": "GPTW#5678",
    "nota_1": 96,
    "nota_2": 60,
    "media": 78.0
  },
  {
    "codigo_pesquisa": "GPTW#9101",
    "nota_1": 77,
    "nota_2": 89,
    "media": 83.0
  },
  {
    "codigo_pesquisa": "GPTW#1121",
    "nota_1": 87,
    "nota_2": 79,
    "media": 83.0
  },
  {
    "codigo_pesquisa": "GPTW#3141",
    "nota_1": 91,
    "nota_2": 82,
    "media": 86.5
  },
  {
    "codigo_pesquisa": "GPTW#5161",
    "nota_1": 59,
    "nota_2": 63,
    "media": 61.0
  }
]
```
