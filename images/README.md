<h4 align="center"> 
	🚧  Estudos em Aprendizagem por Reforço 🚀 Em construção...  🚧
</h4>

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
<p align="justify">O ramo da Inteligência Artificial, além de amplo e relativamente recente, possui uma certa complexidade e exige o entendimento prévio de diversos conceitos computacionais e técnicas de programação. Com isso em mente, múltiplas Empresas e Instituições foram criadas a fim de tornar o aprendizado de AI atrativo e dinâmico. Neste tópico, o foco será em uma Instituição específica: a OpenAI.</p>

<p align="justify">A OpenAI é uma Instituição desprovida de fins lucrativos voltada à pesquisa de Inteligência Artificial. Seu foco é fornecer o desenvolvimento de IA de forma amigável e, ainda, possui como missão beneficiar a sociedade como um todo. Abaixo, serão apresentados 2 exemplos de destaque desenvolvidos pela equipe da OpenAI. 
	O primeiro projeto é a resolução do cubo de Rubik utilizando-se uma mão robótica.</p>

| Rubik's Cube |
| ------------ |
| <img src="https://cdn.openai.com/solving-rubiks-cube/images/dr.jpg" width="500">|
| Fonte: Fonte: OpenAI.
Disponível em < https://openai.com/blog/solving-rubiks-cube/ >. Acesso em: 27 fev. 2021. |

<p align="justify">De certo, resolver o cubo de Rubik já não é uma tarefa fácil nem para um humano, o qual apenas é capaz de resolvê-lo devido sua capacidade de manipular objetos e operar com as mãos, resultado de milhares de anos de evolução. Com isso em mente, a OpenAI enfrentou o desafio de, além de desenvolver um algoritmo capaz de aprender a executar tal tarefa, construir uma mão robótica o mais próximo possível da mão humana. A abordagem utilizada consistiu em centenas de ambientes de simulação que possibilitaram a aprendizagem da mão robótica a realizar as tarefas desejadas, não apenas no mundo virtual, mas também no mundo real. No contexto computacional, mais especificamente no que se refere ao algoritmo de aprendizado por reforço do projeto, a técnica estabelecida para o processo foi a “Randomização automática de domínio” - técnica já desenvolvida pela própria OpenAI - a qual fundamenta-se na criação de ambientes aleatórios com complexidades diferenciadas e cada vez mais complexas, de forma que a mão robótica venha a lidar com situações nunca vistas antes. Nesse sentido, a mão foi testada em diversos cenários adversos para constatação de sua capacidade e habilidade, tais como: presença de vento, utilização de luvas, interferência por objetos, testes de elasticidade, fricção, tamanho e massa variável do cubo. Apesar de ainda não ser capaz de resolver o cubo 100% das vezes, é esperado que , em breve,  o conjunto mão robótica e algoritmo de aprendizagem por reforço sejam totalmente eficientes nos mais variados ambientes e complexas situações.</p>

## Entendendo RL
<p align="justify">Para uma compreensão geral do funcionamento de um algoritmo de RL, é necessário entender os principais conceitos que o envolvem. Entre eles, têm-se o agente, a recompensa, a ação, o ambiente e o estado. Basicamente, a relação prática e teórica de todos esses conceitos leva ao objetivo final do RL: fazer um objeto (agente), seja ele físico ou virtual aprender a fazer algo (tarefas humanas). O agente aprende por meio da interação com o ambiente, sem um conhecimento prévio do que deve realizar. As recompensas (r:(S × A) → R) , as quais podem ser  positivas ou negativas, são “feedbacks” do ambiente sobre o comportamento do agente. A ideia geral de um algoritmo de RL é fazer com que essas recompensas sejam maximizadas, ou seja, quanto maior for a recompensa de determinada ação, melhor a ação tomada é para o aprendizado. Já o ambiente pode ser um ambiente real ou um ambiente de simulação. O agente deve estar preparado para um ambiente de constantes mudanças, não para um ambiente estagnado.</p>

>“ _Aprendizado por reforço é uma abordagem computacional para entender e automatizar o aprendizado direcionado a objetivos e tomada de decisão. É distinguido de outras abordagens computacionais pela ênfase no aprendizado de um agente pela interação direta com o ambiente, sem depender de uma supervisão exemplar ou completar modelos de ambientes_” (Richard S. Sutton and Andrew G. Barto, 2015, p.29).

![Aprendizado por reforço](https://github.com/glahr/estudos_aprendizagem_por_reforco/blob/main/aprendizado%20por%20reforco.png?raw=true)

#### Simbologia:

:small_orange_diamond: s → estado<br />
:small_orange_diamond: a →  ação<br />
:small_orange_diamond: S → conjunto de todos os estados não terminais<br />
:small_orange_diamond: S+ →  conjunto de todos os estados, incluindo o estado terminal<br />
:small_orange_diamond: A(s) →  conjunto de ações para o estado s<br />
:small_orange_diamond: R →  conjunto de possíveis recompensas<br />
:small_orange_diamond: 𝑦 → desconto<br />

<p align="justify">Durante o  funcionamento de um algoritmo de Reinforcement Learning,  o agente encontra-se em um certo estado. Em seguida, realiza uma determinada ação, passando a outro estado. Por fim, recebe uma recompensa. O objetivo é maximizar o conjunto de tais recompensas, para que o agente tenha resultados melhores e mais próximos o possível do esperado. Pode-se dizer que, a princípio, os testes realizados com o agente devem “falhar”, com o propósito de que o agente identifique o que não se deve fazer e, assim, obter resultados futuros mais precisos e eficientes. Basicamente, o agente irá aprender com seus erros e acertos, assim como um ser humano durante toda a sua vida. Uma equação que podemos utilizar para lidar com a modelagem em aprendizado por reforço é a chamada equação de Bellman, vamos verificar na próxima seção.</p>

## Processo de decisão de Markov e Equação de Bellman

<p align="justify">Em Aprendizado por Reforço, o processo que normalmente sustenta a aplicação é o Processo de decisão de Markov (Markov decision process - MDP), o qual é caracterizado pela estocasticidade. O processo consiste em um conjunto de estados, ações, modelo de transição e recompensas, representando por: <T,S,,A,R(s)>, em que T - P(s’| s,a) - é a probabilidade de dado agente mover para o estado s’ de s executando determinada ação a. Para auxiliar tal processo de decisão, é utilizada a equação de Bellman.
Contextualizando, Richard Ernest Bellman foi um grande contribuidor no ramo da matemática e da computação devido à invenção da programação dinâmica. Sua equação tem grande importância, no sentido de otimização de valores em uma função.
A seguir, temos a equação (1) - representa a relação de um valor de estado e dos valores de estados sucessores - e a equação (2), em que é calculado o valor representante de tomar determinada ação a em um estado s, sob uma política pi : </p>


<img src="https://render.githubusercontent.com/render/math?math=Q(s,a) = Q(s,a) + \alpha [R(s',a)+\gamma max_{a'} Q'(s',a') - Q(s,a)]">



### Pré-requisitos
<p align="justify">Antes de começar, você vai precisar ter instalado em sua máquina as seguintes...</p>





```python
import numpy as np 
```

