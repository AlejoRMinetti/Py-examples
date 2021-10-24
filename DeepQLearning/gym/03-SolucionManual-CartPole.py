"""
Observation & Space example in CartPole-v0
http://gym.openai.com/docs/
"""
import gym

# change games: CartPole-v0, MountainCar-v0, MsPacman-v0 or Hopper-v1
env = gym.make('CartPole-v0')

# mover segun angulo del palito

for i_episode in range(20):
    observation = env.reset()
    for t in range(1000):
        env.render()
        # print(observation)
        action = env.action_space.sample()

        # solucion hardcodeada
        action = int(observation[2] > 0.0 and observation[3] > 0.0)

        observation, reward, done, info = env.step(action) 
        # reward siempre = 1

        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break

env.close()


