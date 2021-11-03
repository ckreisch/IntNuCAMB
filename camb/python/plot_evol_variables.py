#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
#
#Load the data
Intnu = np.genfromtxt('../Int_mass_nu_evol_var_k_40.txt',dtype=[('tau','f8'),('a','f8'),('de_CDM','f8'),('de_bar','f8'),('de_gam','f8'),('theta_gam','f8'),('pi_gam','f8'),('de_nu_mass','f8'),('theta_nu_mass','f8'),('pi_nu_mass','f8'),('de_nu_nomass','f8'),('theta_nu_nomass','f8'),('pi_nu_nomass','f8'),('Phi','f8'),('Psi','f8')])
LCDM = np.genfromtxt('../NonInt_mass_nu_evol_var_k_40.txt',dtype=[('tau','f8'),('a','f8'),('de_CDM','f8'),('de_bar','f8'),('de_gam','f8'),('theta_gam','f8'),('pi_gam','f8'),('de_nu_mass','f8'),('theta_nu_mass','f8'),('pi_nu_mass','f8'),('de_nu_nomass','f8'),('theta_nu_nomass','f8'),('pi_nu_nomass','f8'),('Phi','f8'),('Psi','f8')])


#Extract the variables
tau_int = Intnu['tau']
de_nu_int = Intnu['de_nu_mass']
theta_nu_int = Intnu['theta_nu_mass']
pi_nu_int = Intnu['pi_nu_mass']
phi_int  = Intnu['Phi']
psi_int = Intnu['Psi']

tau_nint = LCDM['tau']
de_nu_nint = LCDM['de_nu_mass']
theta_nu_nint = LCDM['theta_nu_mass']
pi_nu_nint = LCDM['pi_nu_mass']
phi_nint  = LCDM['Phi']
psi_nint = LCDM['Psi']

#Set the plot
ax = plt.subplot(221)
ax.set_xscale('log')
#ax.set_yscale('log')
ax.set_xlim(1E-3,2)
ax.plot(tau_int,de_nu_int,'g-',linewidth = 2.0)
ax.plot(tau_nint,de_nu_nint,'g--',linewidth = 1.0)
leg = ax.legend(('$\\delta_{\\nu,{\\rm int}}$','$\\delta_{\\nu,\\Lambda{\\rm CDM}}$'),loc='upper left')
ax.set_xlabel('$\\tau$',size = 18)

ax2 = plt.subplot(222)
ax2.set_xscale('log')
#ax2.set_yscale('log')
ax2.set_xlim(1E-3,2)
ax2.plot(tau_int,theta_nu_int,'r-',linewidth = 2.0)
ax2.plot(tau_nint,theta_nu_nint,'r--',linewidth = 1.0)
leg = ax2.legend(('$\\theta_{\\nu,{\\rm int}}$','$\\theta_{\\nu,\\Lambda{\\rm CDM}}$'),loc='upper left')
ax2.set_xlabel('$\\tau$',size = 18)

ax3 = plt.subplot(223)
ax3.set_xscale('log')
#ax3.set_yscale('log')
ax3.set_xlim(1E-3,2)
ax3.plot(tau_int,pi_nu_int,'r-',linewidth = 2.0)
ax3.plot(tau_nint,pi_nu_nint,'r--',linewidth = 1.0)
leg = ax3.legend(('$\\pi_{\\nu,{\\rm int}}$','$\\pi_{\\nu,\\Lambda{\\rm CDM}}$'),loc='lower left')
ax3.set_xlabel('$\\tau$',size = 18)

ax4 = plt.subplot(224)
ax4.set_xscale('log')
#ax4.set_yscale('log')
ax4.set_xlim(1E-3,2)
ax4.plot(tau_int,phi_int - psi_int,'r-',linewidth = 2.0)
ax4.plot(tau_nint,phi_nint - psi_nint,'r--',linewidth = 1.0)
leg = ax4.legend(('$(\\Phi-\\Psi)_{\\rm int}$','$(\\Phi-\\Psi)_{\\Lambda{\\rm CDM}}$'),loc='upper left')
ax4.set_xlabel('$\\tau$',size = 18)

#Show it
plt.show()
