# Estudos Aprendizagem por Reforço
<p align="center">
 <a href="#introducao">Introdução</a> •
 <a href="#motivacao">Motivação</a> • 
 <a href="#rl">Entendendo RL</a> • 
 <a href="#markov">Decisão de Markov</a> • 
 <a href="#bellman">Equação de Bellman</a> • 
 <a href="#industria">Indústria</a>  • 
 <a href="#exemplo">Exemplo Prático</a> • 
</p>

## Introdução
<p align="left">Para compreender a importância do Aprendizado por Reforço (Reinforcement Learning - RL) , é importante salientar que o RL é conhecido como modelo de aprendizado semi-supervisionado em Aprendizado de Máquina (Machine Learning), método inserido no campo da Inteligência Artificial, isto é, o estudo em que máquinas são utilizadas com o propósito de apreenderem e raciocinarem o mais próximo possível da mente humana. Mas, afinal, o que é inteligência? O conceito pode ser definido como o conjunto de competências caracterizado por: adaptação, reconhecimento, aprendizado, interpretação, tomada de decisão e raciocínio. Tudo isso, será de suma importância no entendimento e aplicação do Aprendizado por reforço. No universo da robótica, a importância do RL deve-se ao fato da possibilidade de estratégia, movimentação e controle e, de modo ascendente, suas aplicações e métodos de uso têm criado raízes e grandes resultados ao meio acadêmico, científico, industrial, comercial e educacional.</p>

## Motivação
<p align="left">Levando em consideração o contexto motivacional, tem-se abaixo o Nybble - um gato robô realista desenvolvido pela Companhia “Petoi” - capaz de correr, andar, equilibrar-se igual a um animal de verdade e, ainda, executar incríveis truques programáveis. Além de ser um projeto inovador e exploratório no sentido tecnológico, o gato Nybble é uma forma lúdica e divertida de se explorar e estudar Reinforcement Learning.</p>

| ![nybble.jpg](https://www.thisiscolossal.com/wp-content/uploads/2019/04/Nybble_03.jpg) | 
|:--:| 
| Fonte: Página Colossal.
Disponível em <https://www.thisiscolossal.com/2019/04/nybble/>. Acesso em: 09 fev. 2021. |

| ![nybbleGif.jpg](https://www.thisiscolossal.com/wp-content/uploads/2019/04/nybble-2.gif) | 
|:--:| 
| Fonte: Página Colossal.
Disponível em <https://www.thisiscolossal.com/2019/04/nybble/>. Acesso em: 09 fev. 2021. |


```python
import numpy as np 
```
