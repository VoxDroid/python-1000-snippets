# 0308 - Molecular Dynamics Cheatsheet

## Quick Commands
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Tips
- Use **velocity Verlet** integration for good energy conservation.
- The **Lennard-Jones potential** is common for simple atomistic interactions: \( V(r)=4\varepsilon[(\sigma/r)^{12}-(\sigma/r)^6] \).
- Use small timesteps (e.g., dt=0.001) to maintain stability.
- Compute kinetic energy from velocities and potential energy from pairwise interactions.
