#20

# 1, 2 ------------------------------------------------------------------------------------------------

from math import lcm

Modules = {'rx' : ['O', {}, []]}

with open('i20.txt', 'r') as f:
    
    for line in f:
        module, children = line.strip().split(' -> ')
        children = tuple(children.split(', '))
        if (type := module[0]) == '%':
            Modules[module[1:]] = ['F', False, children]
        elif type == '&':
            Modules[module[1:]] = ['C', {}, children]
        else:
            Modules['broadcaster'] = ['B', children]

for key, value in  Modules.items():
    for c in value[-1]:
        module = Modules[c]
        if module[0] == 'C':
            module[1][key] = False

#for key, value in Modules.items(): print(key, ' : ', value)

times = 1000 * 10 # erase * 10 for #1
totalLows, totalHighs = 0, 0
rxConjuctions = {}
rxLowPulseIteration = 1

for i in range(1, times + 1):
    currentModules = [ ('broadcaster', False, module) for module in Modules['broadcaster'][1] ]
    lows, highs = 1 + len(currentModules), 0

    while currentModules:
        modules = currentModules[:]
        currentModules.clear()

        for sender, pulse, module in modules:
            if pulse == False and (module in ('js','zb','bs','rr')):
                if not module in rxConjuctions:
                    rxLowPulseIteration = lcm(rxLowPulseIteration, i)
                    rxConjuctions[module] = i

            current = Modules[module]

            if current[0] == 'F':
                if not pulse:
                    if current[1]:
                        currentModules.extend([(module, False, child) for child in current[-1]])
                        lows += len(current[-1])
                    else:
                        currentModules.extend([(module, True, child) for child in current[-1]])
                        highs += len(current[-1])
                    
                    current[1] = not current[1]
            else:
                current[1][sender] = pulse
                if all(current[1].values()):
                    currentModules.extend([(module, False, child) for child in current[-1]])
                    lows += len(current[-1])
                else:
                    currentModules.extend([(module, True, child) for child in current[-1]])
                    highs += len(current[-1])

    totalLows += lows
    totalHighs += highs

print(totalLows * totalHighs)
print(rxLowPulseIteration)

#684125385
#225872806380073