# AG002
Repositório destinado aos códigos para resolução da Avaliação Global (AG002) do Instituto Nacional de Telecomunicações - INATEL.

Este trabalho foi desenvolvido pelos alunos dos cursos de graduação em Engenharia de Software <a href="https://github.com/jvoliveirag">João Victor de Oliveira Gomes Ribeiro</a> e Engenharia da Computação <a href="https://github.com/juvillela12">Júlia da Silva Villela</a>.

## Objetivo 🎯
 Utilizar dos  conhecimentos  de  Programação,  Bancos  de  Dados  e  Inteligência  Artificial  para,  a  partir do conjunto de dados proposto, treinar, avaliar e disponibilizar um modelo de aprendizado de máquina para classificar dados relacionados a crédito.

 ## Conjunto de dados 📚
 - O <a href="https://raw.githubusercontent.com/marcelovca90-inatel/AG002/main/statlog-germancredit.sql">conjunto de dados</a> apresenta 1000 amostras;
 - 20  atributos  que  podem ser utilizados para classificar bons e maus candidatos a empréstimo;
 - O conjunto de dados foi obtido do <a href="https://archive.ics.uci.edu/ml/datasets/South+German+Credit+%28UPDATE%29">UCI Machine Learning Repository</a>;
 - Os atributos estão em alemão, e os dados estão codificados de acordo com uma <a href="https://raw.githubusercontent.com/marcelovca90-inatel/AG002/main/codetable.txt">codetable</a>.

## Tecnologias e recursos 🚀
- MySql
- Python (v3.10.4)
    - Pandas
    - Scikit learn
- Decision Tree

## Como executar ⚙️
1. Clone este repositório em sua máquina;
2. No terminal, no diretório do arquivo "main.py", digite o seguinte comando:
```
python main.py
```
3. Ao executar serão exibidas as métricas e, em seguida, serão solicitados os valores para realizar a predição do empréstimo;
4. Alguns valores "pré-definidos" podem ser encontrados como comentário no arquivo "inputs" e usados como exemplo.

### OBS.: O Vídeo contendo a explicação do projeto encontra-se <a href="https://vimeo.com/772784740">aqui</a>.