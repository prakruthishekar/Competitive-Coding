def getMaxBarrier(initialEnergy, th):
    low = 0
    high = max(initialEnergy)
    
    while low <= high:
        midpoint = (low + high) // 2
        total_energy = 0
        
        for energy in initialEnergy:
            final_energy = max(energy - midpoint, 0)
            total_energy += final_energy
        
        if total_energy >= th:
            low = midpoint + 1
        else:
            high = midpoint - 1
    
    return low - 1


print(getMaxBarrier([5,2,13,10], 8))
print(getMaxBarrier([3,9,7,6], 6))
