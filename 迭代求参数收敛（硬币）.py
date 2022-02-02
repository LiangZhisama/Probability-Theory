import numpy as np
from scipy.stats import binom

def single_iter(theta_priors,exper_results):
    counts={'A':{'H':0,'T':0},'B':{'H':0,'T':0}}
    theta_A=theta_priors['A']
    theta_B=theta_priors['B']

    for result in exper_results:
        num_heads=result['H']
        num_tails=result['T']
        P_A=binom.pmf(num_heads,num_heads+num_tails,theta_A)
        P_B=binom.pmf(num_heads,num_heads+num_tails,theta_B)
        weight_A=P_A/(P_A+P_B)
        weight_B=P_B/(P_A+P_B)
        counts['A']['H']+=weight_A*num_heads
        counts['A']['T']+=weight_A*num_tails
        counts['B']['H']+=weight_B*num_heads
        counts['B']['T']+=weight_B*num_tails

    new_theta_A=counts['A']['H']/(counts['A']['H']+counts['A']['T'])
    new_theta_B=counts['B']['H']/(counts['B']['H']+counts['B']['T'])
    return{'A':new_theta_A,'B':new_theta_B}

exper_results = np.array([{'H':6,'T':4},
                          {'H':7,'T':3},
                          {'H':8,'T':2},
                          {'H':4,'T':6},
                          {'H':3,'T':7},
                          {'H':5,'T':5}])
theta={'A':0.7,'B':0.4}
iter=0
total_iter=10000

while iter<total_iter:
    new_theta = single_iter(theta,exper_results)
    print(new_theta)
    delta_change=np.abs(theta['A']-new_theta['A'])
    if(delta_change<1e-6): 
        break
    else:
        theta = new_theta
        iter+=1

print('迭代结束，总共迭代{}轮'.format(iter))
print('最终估计的参数{}'.format(new_theta))

                             