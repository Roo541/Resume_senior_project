import numpy as np
from random import randint
import random
import matplotlib.pyplot as plt
import copy
import math
import csv, sys

import agents

#global stuff
tmax = int(1e4)

i_g = 100
i_ba = 10000

agent_kind_A = [200., 100.  , 50,    50, 25  ]
agent_kind_B = [25,    50   , 50,  100., 200.]

agents.my_preferences = np.array(60*[agent_kind_A] + 40*[agent_kind_B])
num_agents = len(agents.my_preferences)

agents.my_preferences *= 1
agents.goods[:] = i_g
agents.Bank_Account[:] = i_ba

agent_names = num_agents*["ia"]

t, old, agentU = agents.Market(agent_names, tmax)

for i in range(tmax):
	for j in range(agents.Numgoods):
		if agents.box[j][i] == 0:
			agents.box[j][i] = agents.box[j][i-1]
print agents.box[4][:]


for i in range(num_agents):
	print '  -- ', agents.goods[i], agents.marginal_utilities(i, agents.goods[i]), agent_names[i], i, agents.Bank_Account[i], agents.my_utilities[i](i, agents.goods[i])
print agents.Bank_Account[:num_agents]

for i in range(num_agents):
        marginal = agents.marginal_utilities(i, agents.goods[i])
        for g in range(agents.Numgoods):
                print 'agent', i, 'good', g, 'mu', marginal[g]/agents.box[g].mean()

#Saves Data onto Excel file
filename_base = sys.argv[0][:-3]
myFile = open(filename_base+'.csv', 'w')
with myFile:
        writer = csv.writer(myFile, lineterminator='\n')
        writer.writerow(('Initial Conditions', 'goods = %d' %i_g, 'Bank_Account = %d' %i_ba,))
        writer.writerow(())
        writer.writerow(('Initial Preferences',))
        for i in range(num_agents):
			writer.writerow(('Agent_%d' %i, agents.my_preferences[i]))
        writer.writerow(())
        writer.writerow(('Goods for each Agent', 'g_0', 'g_1', 'g_2', 'g_3', 'g_4',))
        for i in range(num_agents):
                writer.writerow(('Agent_%d' %i,  agents.goods[i][0],agents.goods[i][1], agents.goods[i][2], agents.goods[i][3], agents.goods[i][4]))
        writer.writerow(())
        writer.writerow(('Bank Accounts', 'Dollars',))
        for i in range(num_agents):
                writer.writerow(('Agent_%d' %i, agents.Bank_Account[i]))
        writer.writerow(())
        writer.writerow(('Prices of Goods', 'Avg over past 50',))
        for i in range(agents.Numgoods):
                writer.writerow(('good_%d' %i, agents.box[i].mean()))
        writer.writerow(())
        writer.writerow(('Money Utility', 'g_0', 'g_1', 'g_2', 'g_3', 'g_4',))
        for i in range(num_agents):
                marginal = agents.marginal_utilities(i, agents.goods[i])
                writer.writerow(('Agent_%d' %i, marginal[0]/np.average(agents.box[0][-50:]), marginal[1]/np.average(agents.box[1][-50:]), marginal[2]/np.average(agents.box[2][-50:]), marginal[3]/np.average(agents.box[3][-50:]), marginal[4]/np.average(agents.box[4][-50:]),))
        writer.writerow(())
        writer.writerow(('Marginal Utility', 'g_0', 'g_1', 'g_2', 'g_3', 'g_4',))
        for i in range(num_agents):
                marginal = agents.marginal_utilities(i, agents.goods[i])
                writer.writerow(('Agent_%d' %i, marginal[0], marginal[1], marginal[2], marginal[3], marginal[4]))

#graphing smart agents utility
for i in range(num_agents):
                style = ':'
                if agent_names[i] == 'intelligent_agent' or agent_names[i] == 'ia':
                        style = 'k-'
                if agent_names[i] == 'IQ':
                        style = 'r--'
                if agent_names[i] == 'S2':
                        style = 'g--'
                if agent_names[i] == 'S3':
                        style = 'b-.'
		plt.plot(agentU[i][:], style, label = agent_names[i]) 
		plt.title('smart agents utility')
		plt.xlabel('time')
		plt.ylabel('utils')
plt.legend()
plt.savefig(filename_base+'Utility.png', dpi=150)
# ~ for i in range(tmax):
	# ~ if agents.box[0][i] == 0:
		# ~ agents.box[0][i] = agents.box[0][i-1]
# ~ print agents.box[0][:]

average_0 = np.average(agents.box[0][-50:])
print 'The average price for good_0 is ', average_0

plt.figure()
t = np.arange(0,tmax, 1)
plt.plot(t, agents.box[0][:], label = 'good 0 price')
plt.legend()

# ~ for g in range(5):
	# ~ plt.figure('Utility vs. good')
	# ~ gmax = tmax
	# ~ g0 = np.arange(0.0, gmax, 1.0)
	# ~ u0 = np.zeros_like(g0)
	# ~ agent_to_plot = 3
	# ~ for i in range(len(g0)):
		# ~ goods[agent_to_plot][:] = 0
		# ~ goods[agent_to_plot][g] = g0[i]
		# ~ u0[i] = Utility1(agent_to_plot, goods[agent_to_plot])

	# ~ plt.plot(g0, u0, label='$U(g_%d)$' % g)
	# ~ plt.legend(loc='best')
	# ~ plt.xlabel('amount of good')
	# ~ plt.ylabel('utility')

	# ~ plt.figure('Marginal utility')
	# ~ plt.plot(g0[1:], np.diff(u0), label=r'$\frac{\partial U}{\partial g_%d}$' % g)
	# ~ plt.xlabel('amount of good %d' % g)
	# ~ plt.legend(loc='best')
	# ~ plt.ylabel(r'marginal utility $\frac{\partial U}{\partial g_i}$')


plt.savefig(filename_base+'good_0.png', dpi=150)
plt.show()
#search past 10 rounds for highest bid and lowest ask of all goods
# ~ hi = 0
# ~ low = 1000000
# ~ for item in old[t-2:]:
	# ~ for i in range(len(my_agents)):
		# ~ a,b,c = item[i]
		# ~ if a == 'bid' and b > hi:
			# ~ hi = max(hi, b)
		# ~ if a == 'ask' and b < low:
			# ~ low = min(low, b)
# ~ print hi, low, old[t-2:]

