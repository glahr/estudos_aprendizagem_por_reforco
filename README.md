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
<p align="justify">Para compreender a importância do Aprendizado por Reforço (Reinforcement Learning - RL) , é importante salientar que o RL é conhecido como modelo de aprendizado semi-supervisionado em Aprendizado de Máquina (Machine Learning), método inserido no campo da Inteligência Artificial, isto é, o estudo em que máquinas são utilizadas com o propósito de apreenderem e raciocinarem o mais próximo possível da mente humana. Mas, afinal, o que é inteligência? O conceito pode ser definido como o conjunto de competências caracterizado por: adaptação, reconhecimento, aprendizado, interpretação, tomada de decisão e raciocínio. Tudo isso, será de suma importância no entendimento e aplicação do Aprendizado por reforço. No universo da robótica, a importância do RL deve-se ao fato da possibilidade de estratégia, movimentação e controle e, de modo ascendente, suas aplicações e métodos de uso têm criado raízes e grandes resultados ao meio acadêmico, científico, industrial, comercial e educacional.</p>

## Motivação
<p align="justify">Levando em consideração o contexto motivacional, tem-se abaixo o Nybble - um gato robô realista desenvolvido pela Companhia “Petoi” - capaz de correr, andar, equilibrar-se igual a um animal de verdade e, ainda, executar incríveis truques programáveis. Além de ser um projeto inovador e exploratório no sentido tecnológico, o gato Nybble é uma forma lúdica e divertida de se explorar e estudar Reinforcement Learning.</p>

| Nybble | Nybble em movimento |
| ------------ | ------------- |
| <img src="https://www.thisiscolossal.com/wp-content/uploads/2019/04/Nybble_03.jpg" width="500"> | <img src="https://www.thisiscolossal.com/wp-content/uploads/2019/04/nybble-2.gif" width="500">|
| Fonte: Página Colossal.
Disponível em <https://www.thisiscolossal.com/2019/04/nybble/>. Acesso em: 09 fev. 2021. |

## Entendendo RL
<p align="justify">Para uma compreensão geral do funcionamento de um algoritmo de RL, é necessário entender os principais conceitos que o envolvem. Entre eles, têm-se o agente, a recompensa, a ação, o ambiente e o estado. Basicamente, a relação prática e teórica de todos esses conceitos leva ao objetivo final do RL: fazer um objeto (agente), seja ele físico ou virtual aprender a fazer algo (tarefas humanas). O agente aprende por meio da interação com o ambiente, sem um conhecimento prévio do que deve realizar. As recompensas (r:(S × A) → R) , as quais podem ser  positivas ou negativas, são “feedbacks” do ambiente sobre o comportamento do agente. A ideia geral de um algoritmo de RL é fazer com que essas recompensas sejam maximizadas, ou seja, quanto maior for a recompensa de determinada ação, melhor a ação tomada é para o aprendizado. Já o ambiente pode ser um ambiente real ou um ambiente de simulação. O agente deve estar preparado para um ambiente de constantes mudanças, não para um ambiente estagnado.</p>

>“ _Aprendizado por reforço é uma abordagem computacional para entender e automatizar o aprendizado direcionado a objetivos e tomada de decisão. É distinguido de outras abordagens computacionais pela ênfase no aprendizado de um agente pela interação direta com o ambiente, sem depender de uma supervisão exemplar ou completar modelos de ambientes_” (Richard S. Sutton and Andrew G. Barto, 2015, p.29).


```python
import numpy as np 
```

<img src="https://render.githubusercontent.com/render/math?math=Q(s,a) = Q(s,a) + \alpha [R(s',a) + \gamma max_{a'} Q'(s',a') - Q(s,a)]">
