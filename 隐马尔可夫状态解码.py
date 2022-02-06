import numpy as np
from hmmlearn import hmm

states = ['box1','box2','box3']
observations = ['black','white']
start_probability=np.array([0.3,0.5,0.2])
transition_probability=np.array([
    [0.4,0.4,0.2],
    [0.3,0.2,0.5],
    [0.2,0.6,0.2]
])
emission_probability=np.array([
    [0.2,0.8],
    [0.6,0.4],
    [0.4,0.6]
])
model=hmm.MultinomialHMM(n_components=len(states))
model.startprob_=start_probability
model.transmat_=transition_probability
model.emissionprob_=emission_probability

observation_list = np.array([0,1,0])
logprob,box_list = model.decode(observation_list.reshape(-1,1),algorithm='viterbi')
print(box_list)
for i in range(len(observation_list)):
    print(states[box_list[i]])