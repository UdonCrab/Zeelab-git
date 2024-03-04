import numpy as np
from gsd import hoomd

# Volume fractions
phi = np.array([0.01, 0.02, 0.03, 0.04])

# Loop through volume fractions
for i in range(len(phi)):
    
    # Construct filename
    fileprefix = 'sed_N8000_phi{:.2f}_FD'.format(phi[i])
    
    # Open gsd file
    file = hoomd.open(name=fileprefix+'.gsd', mode='r')
    
    # Open a text file
    with open(fileprefix+'.txt', 'w') as f:
    
        # Loop through frames
        for frame in file:
            
            # Read data
            N = frame.particles.N
            box = frame.configuration.box
            x = frame.particles.position
            
            # Write to text file
            f.write('{:d}\n'.format(N))
            f.write('{:.5f} {:.5f} {:.5f}\n'.format(box[0], box[1], box[2]))
            for pos in x:
                f.write('{:.5f} {:.5f} {:.5f}\n'.format(pos[0], pos[1], pos[2]))
            f.write('\n')