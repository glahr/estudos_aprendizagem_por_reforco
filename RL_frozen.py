import gym
import numpy as np
import matplotlib.pyplot as plt

env = gym.make('FrozenLake8x8-v0')

# Passo 0 - Definindo parametros
alpha = 0.7 #taxa de aprendizado               
discount_factor = 0.618               
epsilon = 1                  
max_epsilon = 1
min_epsilon = 0.01         
decay = 0.00008

train_episodes = 10000
test_episodes = 100
max_steps = 200


# Passo 1 - Inicializando a Q-Table
Q = np.zeros((env.observation_space.n, env.action_space.n))

# Passo 2 - Treinando o agente
# Criando listas para controlar as recompensas e os valores de epsilon
training_rewards = []  
epsilons = []

for episode in range(train_episodes):
    #Reiniciando o ambiente a cada vez de acordo com o requisito
    state = env.reset()  
    #Inicializando o rastrador de recompensas  
    total_training_rewards = 0
    
    for step in range(max_steps):
        #Escolhendo a acao dado um estado baseado em um numero aleatorio
        exp_exp_tradeoff = np.random.uniform(0, 1)
        
        ### Passo 2.1: SECOND option for choosing the initial action - exploit     
        #If the random number is larger than epsilon: employing exploitation 
        #and selecting best action 
        if exp_exp_tradeoff > epsilon:
            action = np.argmax(Q[state,:])
            
        ### STEP 2.1: FIRST option for choosing the initial action - explore       
        #Otherwise, employing exploration: choosing a random action 
        else:
            action = env.action_space.sample()
            
            
        ### STEPs 3 & 4: performing the action and getting the reward     
        #Taking the action and getting the reward and outcome state
        new_state, reward, done, info = env.step(action)
        #if reward == 0:
        #    reward = -1
        #print('reward =', reward, 'action =', action)
        env.render()
        #print('\n')        

        ### STEP 5: update the Q-table
        #Updating the Q-table using the Bellman equation
        Q[state, action] = Q[state, action] + alpha * (reward + discount_factor * np.max(Q[new_state, :]) - Q[state, action]) 
        #Increasing our total reward and updating the state
        total_training_rewards += reward      
        state = new_state         
        
        #Ending the episode
        if done == True:
            #print ("Total reward for episode {}: {}".format(episode, total_training_rewards))
            break
    
    #Cutting down on exploration by reducing the epsilon 
    #epsilon = min_epsilon + (max_epsilon - min_epsilon)*np.exp(-decay*episode)
    if episode > 0.1*train_episodes:
        if epsilon <= min_epsilon:
            epsilon = min_epsilon
        else:
            epsilon = epsilon - decay

    #Adding the total reward and reduced epsilon values
    training_rewards.append(total_training_rewards)
    epsilons.append(epsilon)
    
    

print ("Training score over time: " + str(sum(training_rewards)/train_episodes))

N = 500
cumsum, moving_aves = [0], []

for i, x in enumerate(training_rewards, 1):
    cumsum.append(cumsum[i-1] + x)
    if i>=N:
        moving_ave = (cumsum[i] - cumsum[i-N])/N
        #can do stuff with moving_ave here
        moving_aves.append(moving_ave)

#Visualizing results and total reward over all episodes
# ORIGINAL
x = range(train_episodes)
plt.plot(x, training_rewards)
plt.xlabel('Episode')
plt.ylabel('Training total reward')
plt.title('Total rewards over all episodes in training') 
plt.show()

#Visualizing results and total reward over all episodes
# MOVING AVERAGE
x = range(train_episodes)
plt.plot(moving_aves)
plt.xlabel('Episode')
plt.ylabel('Training total reward')
plt.title('Total rewards over all episodes in training')
plt.show()

#Visualizing the epsilons over all episodes
plt.plot(epsilons)
plt.xlabel('Episode')
plt.ylabel('Epsilon')
plt.title("Epsilon for episode")
plt.show()